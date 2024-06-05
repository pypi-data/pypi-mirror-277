import numpy as np
import pandas as pd
from scipy import optimize
from matplotlib import pyplot as plt

class MultipleAncillaryProductsLinearDemand:
    """This class considers single leg flight with a primary product (seats) and ancillary products. The capacity of 
    primary product is fixed, capacities of individual ancillary products can also be limited (e.g. better seats). 
    Total revenue is maximized by dynamically setting prices on both the primary product and the ancillary services. 
    ___________________________________________________________________________________________________________________
    We consider a set of distinct product combinations or product mixes, each product mix has a separate booking 
    probability model and demand forecast. This allows individuals to buy different product mixes based on the price. 
    For some prices, an individual may buy mix 1, for others mix 2, etc. The booking period of the flight is divided 
    into time periods. The booking probability models for individual product mixes and time periods are linear.
    ___________________________________________________________________________________________________________________
    John G. Wilson. 2016. Jointly Optimising Prices for Primary and Multiple Ancillary Products.
    ___________________________________________________________________________________________________________________
    Args:
        n_periods (int):         number of time periods
        n_products (int):        number of products
        n_product_mixes (int):   number of product mixes
        product_names (str):     names of individual products
    """
    def __init__(self, n_periods, n_products, n_product_mixes, product_names):
        self.n_periods = n_periods
        self.n_products = n_products
        self.n_product_mixes = n_product_mixes
        self.product_names = product_names

        # Initialize matrices and vectors characterizing the optimization problem:
        # Revenue function: (1/2)*x.T*H*x + c*x
        # Constraints:      Ax <= b
        self.H = np.zeros(( self.n_periods * self.n_products, self.n_periods * self.n_products )) 
        self.c = np.zeros(  self.n_periods * self.n_products )

        # Constraints: booking probability >= 0
        self.A_prob_0 = np.zeros(( self.n_periods * self.n_product_mixes, self.n_periods * self.n_products ))
        self.b_prob_0 = np.zeros(  self.n_periods * self.n_product_mixes )

        # Constraints: booking probability <= 1
        self.A_prob_1 = np.zeros(( self.n_periods * self.n_product_mixes, self.n_periods * self.n_products ))
        self.b_prob_1 = np.zeros(  self.n_periods * self.n_product_mixes )

        # Constraints: Optimum price >= 0
        self.A_price_0 = np.zeros(( self.n_periods * self.n_products, self.n_periods * self.n_products ))
        self.b_price_0 = np.zeros(  self.n_periods * self.n_products )

        # Capacity constraints
        self.A_cap_c = np.zeros(( self.n_products, self.n_periods * self.n_products ))
        self.b_cap_c = np.zeros(  self.n_products )

        # Starting point
        self.x0 = np.zeros(  self.n_periods * self.n_products )

    def fit(self, product_capacity, period_forecast, demand_intercept, demand_slope, incidence_matrix):
        """Calculates optimum prices for all products. The optimum price for a product mix containing
        more products is then given by the sumation of individual optimum product prices. Also
        calculates three dataframes containing summary results.
        Args:
            product_capacity (float): capacities of individual products
            period_forecast (float):  numbers of passengers in individual time periods (forecast)
            demand_intercept (float): matrix containing intercepts of purchase probability models
                                      demand_intercept[t,m] - intercept of a purchase prob. model for period t and product mix m
            demand_slope (float):     matrix containing slopes of purchase probability models
                                      demand_slope[t,m] - slope of a purchase prob. model for period t and product mix m
            incidence_matrix (float): incidence matrix: rows - product mixes, columns - products
                                      incidence matrix[m,p]  = 1 if product mix m contains product p, = 0 otherwise
        Returns:
            opt_prices (float):       opt_prices[p] - calculated optimum price for the product p
        """
        self.product_capacity = product_capacity
        self.period_forecast = period_forecast
        self.demand_intercept = demand_intercept
        self.demand_slope = demand_slope
        self.incidence_matrix = incidence_matrix
        for t in range(self.n_periods):             # Loop over time periods 
            # 1. Read the input parameters characterizing period t
            Intercept_t  = self.demand_intercept[t,]
            Slope_t = self.demand_slope[t,]
            Q_t = self.period_forecast[t]
                
            # 2. Calculate matrices and vectors characterizing period t
            H_t, c_t = self.revenue_fields(Intercept_t, Slope_t, Q_t)
            A_t, b_t = self.capacity_constraints(Intercept_t, Slope_t, Q_t)
                
            # 3. Add fields characterizing period t to the global fields
            for i in range(self.n_products):
                self.c[ t * self.n_products + i ] = c_t[i]
                self.b_cap_c[i] = self.b_cap_c[i] + b_t[i]
                self.x0[ t * self.n_products + i ] = -0.8 * ( Intercept_t[i] / Slope_t[i] )
                for j in range(self.n_products):
                    self.H[ t * self.n_products + i , t * self.n_products + j ] = H_t[ i, j ]
                    self.A_cap_c[ i , t * self.n_products + j ] = A_t[ i, j ] 
                    if i == j:
                        self.A_price_0[ t * self.n_products + i , t * self.n_products + j ] = -1
                
            # 4. Calculate matrices and vectors for simple constraints (booking probability >= 0, booking probability <= 1)
            for m in range(self.n_product_mixes):
                for p in range(self.n_products):
                    # Constraints: matrix A
                    self.A_prob_0[ t * self.n_product_mixes + m , t * self.n_products + p ] = - self.incidence_matrix[ m, p ] * self.demand_slope[t,m]
                    self.A_prob_1[ t * self.n_product_mixes + m , t * self.n_products + p ] = self.incidence_matrix[ m, p ] * self.demand_slope[t,m]
                    # Constraints: vector b
                    self.b_prob_0[ t * self.n_product_mixes + m ] = self.demand_intercept[t,m]
                    self.b_prob_1[ t * self.n_product_mixes + m ] = 1 - self.demand_intercept[t,m]

        # Add product capacities to the right hand side of capacity constraints
        self.b_cap_c = self.b_cap_c + self.product_capacity
        # Constraints: Ax <= b
        A = np.vstack( ( self.A_prob_0, self.A_prob_1, self.A_price_0, self.A_cap_c ) )
        b = np.concatenate((self.b_prob_0, self.b_prob_1, self.b_price_0, self.b_cap_c), axis=0)

        # Definition of optimization problem:
        # Minimize -Revenue: -(1/2)*x.T*H*x - c*x
        # subject to:          b - Ax >= 0
        cons = {'type':'ineq',
        'fun':lambda x: b - np.dot( A, x ),
        'jac':lambda x: -A }

        opt = {'disp':False}

        # Calling the optimization solver:
        res_cons = optimize.minimize(self.loss, self.x0, jac=self.jac, constraints=cons, method='SLSQP', options=opt)
        self.opt_prices = res_cons['x']

        TotDemandProducts, OptSolutionProducts, OptSolutionProductMixes, total_revenue = self.postprocessing()

        return self.opt_prices, total_revenue, OptSolutionProducts, OptSolutionProductMixes, TotDemandProducts
    
    def revenue_fields(self, Intercept_t, Slope_t, Q_t):
        """Calculates fields needed for the maximization of revenue
        Args:
            INC (float)         - Incidence matrix: rows - product mixes, columns - Products, INC[m,p] = 1 if product mix m contains product p, = 0 otherwise
            Intercept_t (float) - vector containing intercepts of a purchase probability model for time period t and individual product mixes
            Slope_t (float)     - vector containing slopes of a purchase probability model for time period t and individual product mixes
            Q_t (float)         - forecast demand for time period t
        Returns:
            H_t (float)         - period t matrix of the quadratic form representing the flight's revenue
            c_t (float)         - period t vector of the quadratic form representing the flight's revenue
        """
        # Initialize matrix and vector of the quadratic form for period t
        H_t  = np.zeros(( self.n_products, self.n_products )) 
        c_t  = np.zeros( self.n_products )
    
        for i in range(self.n_products):
            for j in range(self.n_products):
                for m in range(self.n_product_mixes):
                    H_t[ i, j ] = H_t[ i, j ] + self.incidence_matrix[ m, i ] * self.incidence_matrix[ m, j ] * Slope_t[m]
                        
        for i in range(self.n_products):
            for m in range(self.n_product_mixes):
                c_t[ i ] = c_t[ i ] + self.incidence_matrix[ m, i ] * Intercept_t[m]
    
        c_t = np.multiply(c_t, Q_t)
        H_t = np.multiply(H_t, 2.0 * Q_t)

        return H_t, c_t
    
    def capacity_constraints(self, Intercept_t, Slope_t, Q_t):
        """Calculates fields needed for the implementation of capacity constraints
        Args:
            INC (float)         - Incidence matrix: rows - product mixes, columns - Products, INC[m,p] = 1 if product mix m contains product p, = 0 otherwise
            Intercept_t (float) - vector containing intercepts of a purchase probability model for time period t and individual product mixes
            Slope_t (float)     - vector containing slopes of a purchase probability model for time period t and individual product mixes
            Q_t (float)         - forecast demand for time period t
        Returns:
            A_t (float)         - period t capacity constraint matrix 
            b_t (float)         - period t capacity constraint vector 
        """
        # Initialize matrix and vector of the quadratic form for period t
        A_t  = np.zeros(( self.n_products, self.n_products )) 
        b_t  = np.zeros( self.n_products )
    
        for i in range(self.n_products):         # Loop over constraints (number of constraints is equal to number of Products)
            for j in range(self.n_products):     # Loop over Products
                for m in range(self.n_product_mixes):  # Loop over product mixes
                    A_t[ i, j ] = A_t[ i, j ] + self.incidence_matrix[ m, i ] * self.incidence_matrix[ m, j ] * Slope_t[m]
    
        for i in range(self.n_products):         # Loop over constraints (number of constraints is equal to number of Products)
            for m in range(self.n_product_mixes):      # Loop over product mixes
                b_t[ i ] = b_t[ i ] - self.incidence_matrix[ m, i ] * Intercept_t[m]
    
        b_t = np.multiply(b_t, Q_t)
        A_t = np.multiply(A_t, Q_t)

        return A_t, b_t
    
    def loss(self, x):
        """Calculates loss function at x. Loss is a quadratic function of the form -(1/2)*x.T*H*x - c*x
        """
        return (-1) * ( 0.5 * np.dot( x.T, np.dot( self.H, x) ) + np.dot( self.c, x ) )

    def jac(self, x):
        """Calculates derivative of loss function at x. Loss is a quadratic function of the form -(1/2)*x.T*H*x - c*x
        """
        return (-1) * ( np.dot( x.T, self.H ) + self.c )
    
    def postprocessing(self):
        """Calculates three dataframes containing summary results and also total revenue
        Args:

        Returns:
            TotDemandProducts        dataframe showing total product demand and available capacity
            OptSolutionProducts      dataframe containing optimum prices for individual products at individual time periods
            OptSolutionProductMixes  dataframe containing opt. prices, demands and revenues for ind. product mixes at ind. time periods
            total_revenue (float):   total revenue per flight
        """
        OptDemand      = np.zeros(  self.n_periods * self.n_product_mixes )
        OptRevenue     = np.zeros(  self.n_periods * self.n_product_mixes )
        OptMixPrice    = np.zeros(  self.n_periods * self.n_product_mixes )
        TimePeriodMix  = np.zeros(  self.n_periods * self.n_product_mixes )
        TimePeriodProd = np.zeros(  self.n_periods * self.n_products )
        ProductMix     = np.zeros(  self.n_periods * self.n_product_mixes )
        Product        = np.zeros(  self.n_periods * self.n_products )
        self.PriceMatrix = np.zeros(( self.n_products , 2*self.n_periods ))
        self.tp          = np.zeros(2*self.n_periods)
        ProductNames   = ["" for x in range(self.n_periods * self.n_products)]
        self.ProdMixName    = ["" for x in range(self.n_product_mixes)]
        ProdMixNames   = ["" for x in range(self.n_periods * self.n_product_mixes)]

        for m in range(self.n_product_mixes):             # Loop over product mixes
            for p in range(self.n_products):        # Loop over Products
                if self.incidence_matrix[m,p] == 1:
                    if len( self.ProdMixName[m] ) > 0:
                        self.ProdMixName[m] = self.ProdMixName[m] + ", " + self.product_names[p]
                    else:
                        self.ProdMixName[m] = self.ProdMixName[m] + self.product_names[p]
        
        for t in range(self.n_periods):          # Loop over time periods
            PeriodMixPrices = np.dot( self.incidence_matrix, self.opt_prices[ t * self.n_products : (t+1)*self.n_products ] )
            for p in range(self.n_product_mixes):         # Loop over product mixes
                OptDemand[ t * self.n_product_mixes + p ]  = self.period_forecast[t] * ( self.demand_intercept[t,p] + self.demand_slope[t,p] * PeriodMixPrices[p] )
                OptRevenue[ t * self.n_product_mixes + p ] = OptDemand[ t * self.n_product_mixes + p ] * PeriodMixPrices[p]
                OptMixPrice[ t * self.n_product_mixes + p ] = PeriodMixPrices[p]
                TimePeriodMix[ t * self.n_product_mixes + p ] = t + 1
                ProductMix[ t * self.n_product_mixes + p ] = p + 1
                ProdMixNames[ t * self.n_product_mixes + p ] = self.ProdMixName[ p ]

        for t in range(self.n_periods):          # Loop over time periods
            self.tp[2*t  ]  = t
            self.tp[2*t+1]  = t+1
            for p in range(self.n_products):        # Loop over Products
                TimePeriodProd[ t * self.n_products + p ] = t + 1
                Product[ t * self.n_products + p ] = p + 1
                ProductNames[ t * self.n_products + p ] = self.product_names[ p ]
                self.PriceMatrix[ p , 2*t   ] = self.opt_prices[ t * self.n_products + p ]
                self.PriceMatrix[ p , 2*t+1 ] = self.opt_prices[ t * self.n_products + p ]

        total_revenue   = np.sum(OptRevenue)
        ProductDemand  = np.dot(self.A_cap_c, self.opt_prices) - self.b_cap_c + self.product_capacity
        total_revenue   = -self.loss(self.opt_prices)

        TimePeriodMix  = TimePeriodMix.astype(int)
        TimePeriodProd = TimePeriodProd.astype(int)
        ProductMix     = ProductMix.astype(int)
        Product        = Product.astype(int)
        Prod           = np.linspace(1, self.n_products, num=self.n_products)
        Prod           = Prod.astype(int)

        OptPric        = np.around(self.opt_prices, decimals=2)
        ProductDemand  = np.around(ProductDemand, decimals=2)
        OptMixPrice    = np.around(OptMixPrice, decimals=2)
        OptDemand      = np.around(OptDemand, decimals=2)
        OptRevenue     = np.around(OptRevenue, decimals=2)

        TotDemandProducts = pd.DataFrame({'Product':Prod,'ProductName':self.product_names,'ProductDemand':ProductDemand,'product_capacity':self.product_capacity})
        OptSolutionProducts = pd.DataFrame({'TimePeriod':TimePeriodProd,'Product':Product,'ProductName':ProductNames,'OptimumPrice':OptPric})
        OptSolutionProductMixes = pd.DataFrame({'TimePeriod':TimePeriodMix,'ProductMix':ProductMix,'ProductsInTheMix':ProdMixNames,'OptMixPrice':OptMixPrice,'OptimumDemand':OptDemand,'OptimumRevenue':OptRevenue})

        return TotDemandProducts, OptSolutionProducts, OptSolutionProductMixes, total_revenue
    
    def plot_optimum_prices(self):
        """Plots a graph showing how individual product prices evolve in time (in time periods)
        """
        plt.figure()
        for p in range(self.n_products):        # Loop over Products
            plt.plot(self.tp, self.PriceMatrix[p,], label=self.product_names[p], linewidth=2)
        plt.xlabel("Period Prior to Departure")
        plt.ylabel("Price")
        plt.title("Optimum Product Prices")
        plt.legend()
        plt.show()

    def plot_booking_probability_models(self):
        """Plots estimated booking probability models for individual products
        """
        for m in range(self.n_product_mixes):        # Loop over product mixes
            plt.figure()
            for t in range(self.n_periods):          # Loop over time periods
                price_mix = np.array([ 0 , -self.demand_intercept[t,m]/self.demand_slope[t,m] ])
                deman_mix = np.array([ self.demand_intercept[t,m] , 0 ])
                plt_label = "time period " + str(t)
                plt.plot(price_mix, deman_mix, label=plt_label, linewidth=2)
            plt_title = "Booking Probability Model: " + self.ProdMixName[m]
            plt.xlabel("Price")
            plt.ylabel("Purchase Probability")
            plt.title(plt_title)
            plt.legend()
            plt.show()
