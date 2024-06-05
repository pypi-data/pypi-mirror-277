import numpy as np
import pandas as pd
from scipy import optimize
from matplotlib import pyplot as plt

class DynamicPricingIndividualModels:
    """This class fits regression models for dynamic pricing of airline ancillaries. Separate pricing models are fitted 
    for individual markets (or market groups, zones etc). A customized loss function is used to guide the training.
    Three different pricing models are always fitted and then the best model with the lowest loss is selected and stored.
    ___________________________________________________________________________________________________________________
    What this python class does is inly the second step of the whole approach. Here is a brief description of the overall
    approach: When a new customer arrives, first, a binary classification model predicts the booking probability 
    (probability of buying ancillary service). This is based on standard predictors as total fare paid for air travel,
    days before departure, number of passengers, market, trip weekday etc. Second, a regression model predicts the optimal 
    ancillary price. Based on customer's market (or market group, zone etc), a corresponding fitted pricing model is
    retrieved. Optimal ancillary price is calculated by plugging in the predicted booking probability.
    ___________________________________________________________________________________________________________________
    Peng Ye, Julian Qian, Jieying Chen, Chen-hung Wu, Yitong Zhou, Spencer De Mars, Frank Yang, and Li Zhang. 2018. 
    Customized Regression Model for Airbnb Dynamic Pricing.
    ___________________________________________________________________________________________________________________
    Args:
        c (float):            two constants to be learned via hyper-parameter tuning, 0 < c[0] < 1, 1 < c[1]
        MinPointsForOpt:      minimum number of data points (pax sessions) required for Pricing Model estimation
        MinPosPointsForOpt:   minimum number of positive data points (booked sessions) required for Pricing Model estimation
        n_fitted_pars (int):  maximum number of fitted parameters of the pricing model
        primary_var_name:     name of the variable: separate pricing model will be estimated for each of its unique values  
                              (e.g. for each market)
        secondary_var_name:   name of the variable: if the particular primary variable (e.g. particular market) does not have 
                              enough MinPointsForOpt or MinPosPointsForOpt, then the generic solution corresponding to secondary 
                              variable (e.g. market group into which this market belongs) will be used.
                              secondary_var_name   = 'None'   generic solution calculated using all sessions/rows is used
        primary_var_values:   array containing unique values of variable primary_var_name
        secondary_var_values: array containing unique values of variable secondary_var_name
    """
    def __init__(self, c, MinPointsForOpt, MinPosPointsForOpt, n_fitted_pars, primary_var_name, secondary_var_name, primary_var_values, secondary_var_values):
        self.c = c
        self.MinPointsForOpt = MinPointsForOpt
        self.MinPosPointsForOpt = MinPosPointsForOpt
        self.n_fitted_pars = n_fitted_pars
        self.primary_var_name = primary_var_name
        self.secondary_var_name = secondary_var_name
        self.primary_var_values = primary_var_values
        self.secondary_var_values = secondary_var_values

        self.n_primary_vars = len(primary_var_values)
        self.n_secondary_vars = len(secondary_var_values)

    def fit(self, DataSet):
        """Fits regression models for dynamic pricing of airline ancillaries. Separate pricing models are fitted for 
        individual values of primary variable (e.g. market). The primary variables not having enough input points
        get assigned a solution for corresponding secondary variable (e.g. market group containing the market).
        If secondary_var_name = 'None', then generic solution calculated using all sessions/rows (all markets) is used
        Args:
           DataSet:   dataframe containing input data which is used for the training. The columns are: 
                        primary_var_name (e.g. Market)
                        secondary_var_name (e.g. MarketGroup, MarketType, Zone)
                        BookingProbability - probability of buying ancillary service (output from the booking probability model)
                        AmountReport - ancillary price offered to the customer
                        PaxDidBuy - outcome vector, 1 - booked session, 0 - non-booked session
        Returns:      stores two dataframes PrimaryPriceModels, SecPriceModels. The first contains the fitted price models
                      for individual primary variables, the second for secondary variables. The columns of the 
                      dataframe PrimaryPriceModels are:
                        primary_var_name (e.g. Market)
                        secondary_var_name (e.g. MarketGroup, MarketType, Zone)
                        BestModel - name of the pricing model with the lowest loss function value. The possible values are:
                          inverse_logit - inverse logit pricing function
                          log_price_map - logistic pricing function
                          exp_price_map - exponential pricing function
                        Theta1 - value of the first fitted parameter
                        Theta2 - value of the second fitted parameter
                        Theta3 - value of the third fitted parameter
                        Loss - loss function value of the BestModel
                        AvailPoints - number of available points for pricing model estimation
                        EnoughPoints = 1 there is enough points for pricing model est., = 0 there is not enough points
                          for estimation, the fitted model for corresponding secondary variable is used           
        """
        # Loop over primary_var_values (markets,zones, etc), calculate whether there is enough points for estimation
        AvailPoints, EnoughPoints, secondary_vars = self.estimation_points(DataSet)

        self.PrimaryOptVars = np.zeros(( self.n_primary_vars, self.n_fitted_pars )) 
        PrimaryBestFit = np.zeros(self.n_primary_vars)
        PrimaryOptLosses = np.zeros(self.n_primary_vars)
        PrimaryBestModel = ["" for x in range(self.n_primary_vars)]

        # GENERIC SOLUTIONS applied to multiple primary_var_values not having enough points
        if self.secondary_var_name == 'None':  
            # Calculate one generic solution using all sessions and assign it to all var_values (markets, zones, etc) not having enough points
            Matrix = DataSet[['PaxDidBuy','BookingProbability','AmountReport']].to_numpy()
            y = Matrix[:,0]
            q = Matrix[:,1]
            P = Matrix[:,2]
            y, q, P = self.fix_pricing_model_inputs(y, q, P)
            # Calculate Starting Point for all three pricing models
            X0_IL, X0_LM, X0_EM = self.starting_point(q, P)
            # Fit individual pricing models to the data
            par_IL, par_LM, par_EM, loss_IL, loss_LM, loss_EM = self.fit_pricing_models(X0_IL, X0_LM, X0_EM, y, q, P)
            # Identify the best model, write the results
            BeFit, BeModel, self.SecOptVars, OptLoss = self.identify_best_model(loss_IL, loss_LM, loss_EM, par_IL, par_LM, par_EM)
            for i in range(self.n_primary_vars):
                if EnoughPoints[i] == 0:
                    PrimaryBestFit[i] = BeFit
                    PrimaryBestModel[i] = BeModel
                    self.PrimaryOptVars[i,:] = self.SecOptVars
                    PrimaryOptLosses[i] = OptLoss
            self.SecPriceModels = pd.DataFrame({self.secondary_var_name:['None'],'BestModel':[BeModel],'Theta1':[self.SecOptVars[0]],'Theta2':[self.SecOptVars[1]],'Theta3':[self.SecOptVars[2]],'Loss':[OptLoss]})
        else:
            # calculate generic solutions for individual secondary_var_values and assign them to all var_values (markets, zones, etc) not having enough points
            self.SecOptVars   = np.zeros(( self.n_secondary_vars, self.n_fitted_pars )) 
            SecBestFit   = np.zeros(self.n_secondary_vars)
            SecOptLosses = np.zeros(self.n_secondary_vars)
            SecBestModel = ["" for x in range(self.n_secondary_vars)]
            for i in range(self.n_secondary_vars):
                DataVarValue = DataSet[ DataSet[self.secondary_var_name] == self.secondary_var_values[i] ]
                Matrix = DataVarValue[['PaxDidBuy','BookingProbability','AmountReport']].to_numpy()
                y = Matrix[:,0]
                q = Matrix[:,1]
                P = Matrix[:,2]
                y, q, P = self.fix_pricing_model_inputs(y, q, P)
                # Calculate Starting Point for all three pricing models
                X0_IL, X0_LM, X0_EM = self.starting_point(q, P)
                # Fit individual pricing models to the data
                par_IL, par_LM, par_EM, loss_IL, loss_LM, loss_EM = self.fit_pricing_models(X0_IL, X0_LM, X0_EM, y, q, P)
                # Identify the best model, write the results
                SecBestFit[i], SecBestModel[i], self.SecOptVars[i,:], SecOptLosses[i] = self.identify_best_model(loss_IL, loss_LM, loss_EM, par_IL, par_LM, par_EM)
                for j in range(self.n_primary_vars):
                    if EnoughPoints[j] == 0 and secondary_vars[j] == self.secondary_var_values[i]:
                        PrimaryBestFit[j] = SecBestFit[i]
                        PrimaryBestModel[j] = SecBestModel[i]
                        self.PrimaryOptVars[j,:] = self.SecOptVars[i]
                        PrimaryOptLosses[j] = SecOptLosses[i]
                self.SecPriceModels = pd.DataFrame({self.secondary_var_name:self.secondary_var_values,'BestModel':SecBestModel,'Theta1':self.SecOptVars[:,0],'Theta2':self.SecOptVars[:,1],'Theta3':self.SecOptVars[:,2],'Loss':SecOptLosses})

        # SPECIFIC SOLUTIONS applied to individual primary_var_values having enough points
        for i in range(self.n_primary_vars):
            if EnoughPoints[i] == 1:
                # Data points that will be used for the estimation
                DataVarValue = DataSet[ DataSet[self.primary_var_name] == self.primary_var_values[i] ]
                Matrix = DataVarValue[['PaxDidBuy','BookingProbability','AmountReport']].to_numpy()
                y = Matrix[:,0]
                q = Matrix[:,1]
                P = Matrix[:,2]
                y, q, P = self.fix_pricing_model_inputs(y, q, P)
                # Calculate Starting Point for all three pricing models
                X0_IL, X0_LM, X0_EM = self.starting_point(q, P)
                # Fit individual pricing models to the data
                par_IL, par_LM, par_EM, loss_IL, loss_LM, loss_EM = self.fit_pricing_models(X0_IL, X0_LM, X0_EM, y, q, P)
                # Identify the best model, write the results
                PrimaryBestFit[i], PrimaryBestModel[i], self.PrimaryOptVars[i,:], PrimaryOptLosses[i] = self.identify_best_model(loss_IL, loss_LM, loss_EM, par_IL, par_LM, par_EM)

        if self.secondary_var_name == 'None':
            self.PrimaryPriceModels = pd.DataFrame({self.primary_var_name:self.primary_var_values,'BestModel':PrimaryBestModel,'Theta1':self.PrimaryOptVars[:,0],'Theta2':self.PrimaryOptVars[:,1],'Theta3':self.PrimaryOptVars[:,2],'Loss':PrimaryOptLosses,'AvailablePoints':AvailPoints,'EnoughPoints':EnoughPoints})
        else:
            self.PrimaryPriceModels = pd.DataFrame({self.primary_var_name:self.primary_var_values,'BestModel':PrimaryBestModel,'Theta1':self.PrimaryOptVars[:,0],'Theta2':self.PrimaryOptVars[:,1],'Theta3':self.PrimaryOptVars[:,2],'Loss':PrimaryOptLosses,'AvailablePoints':AvailPoints,'EnoughPoints':EnoughPoints,self.secondary_var_name:secondary_vars})
        
        self.PrimaryPriceModels.to_csv('calculated-results/fitted-primaryprice-models.csv', index=False)
        self.SecPriceModels.to_csv('calculated-results/fitted-secondaryprice-models.csv', index=False)
        return self
    
    def predict(self, DataSet):
        """Calculates optimum prices for all customers/data rows in the dataset. If the dataset contains new values of 
        primary_var_name (e.g. Market), then a solution for corresponding secondary_var_name (e.g. market group 
        containing the market) is used. If secondary_var_name = 'None', then generic solution calculated using 
        all sessions/rows (all markets) is used.
        Args:
           DataSet:   dataframe containing input data which is used for the prediction. The columns are: 
                        primary_var_name (e.g. Market)
                        secondary_var_name (e.g. MarketGroup, MarketType, Zone)
                        BookingProbability - probability of buying ancillary service (output from the booking probability model)
                        AmountReport - ancillary price offered to the customer
                        PaxDidBuy - outcome vector, 1 - booked session, 0 - non-booked session
        Returns:
           OptPrice (float): OptPrice[i] - calculated optimum price for the i-th row of DataSet
        """
        nrow = len( DataSet['PaxDidBuy'] )
        OptPrice = np.zeros(nrow)
        for i in range(nrow):
            # Retrieve booking probability of the j-th customer
            q = DataSet['BookingProbability'][i]
            # Retrieve var_value
            var_value  = DataSet[self.primary_var_name][i]
            if var_value in self.primary_var_values:          # specific solution is used
                # Retrieve var_index
                var_index  = self.primary_var_values.index(var_value)
                # Retrieve best pricing model name and its fitted parameters
                best_model = self.PrimaryPriceModels['BestModel'][var_index]
                Theta = self.PrimaryOptVars[var_index,:]
            else:                                # generic solution calculated using all sessions/rows is used
                # Retrieve best pricing model name and its fitted parameters
                if self.secondary_var_name == 'None':
                    best_model = self.SecPriceModels['BestModel'][0]
                    Theta = self.SecOptVars 
                else:
                    var_value  = DataSet[self.secondary_var_name][i]
                    var_index  = self.secondary_var_values.index(var_value)
                    best_model = self.SecPriceModels['BestModel'][var_index]
                    Theta = self.SecOptVars[var_index,:]
            if best_model == "inv_logit":
                OptPrice[i] = self.inv_logit( Theta[0:self.n_fitted_pars-1], q )
            elif best_model == "log_price_map":
                OptPrice[i] = self.log_price_map( Theta, q )
            else:
                OptPrice[i] = self.exp_price_map( Theta, q )
            
        return OptPrice

    def estimation_points(self, DataSet):
        """Determines whether there is enough points for pricing model estimation.
        Loops over all values of primary_var_name (e.g. Market), for each of its unique values
        determines the corresponding value of secondary_var_name (e.g. MarketGroup, MarketType, Zone)
        Args:
            DataSet:  dataframe containing input data which is used for the training. The columns are: 
                        primary_var_name (e.g. Market)
                        secondary_var_name (e.g. MarketGroup, MarketType, Zone)
                        BookingProbability - probability of buying ancillary service (output from the booking probability model)
                        AmountReport - ancillary price offered to the customer
                        PaxDidBuy - outcome vector, 1 - booked session, 0 - non-booked session
        Returns:
            AvailPoints (float):        AvailPoints[i] - number of available points for pricing model estimation
            EnoughPoints (float):       EnoughPoints[i] = 1 there is enough points for pricing model est., = 0 otherwise
            secondary_vars (str):       secondary_vars[i] - secondary_var_value corresponding to primary_var_values[i]
        """
        EnoughPoints = np.zeros(self.n_primary_vars)
        AvailPoints = np.zeros(self.n_primary_vars)
        secondary_vars = ["" for x in range(self.n_primary_vars)]

        # Loop over var_values (markets,zones, etc), calculate whether there is enough points for estimation
        for i in range(self.n_primary_vars):
            # Data points that will be used for the estimation
            DataVarValue = DataSet[ DataSet[self.primary_var_name] == self.primary_var_values[i] ]
            Matrix = DataVarValue[['PaxDidBuy','BookingProbability','AmountReport']].to_numpy()
            y = Matrix[:,0]
            AvailPoints[i] = len(y)
            if len(y) >= self.MinPointsForOpt and np.sum(y) >= self.MinPosPointsForOpt:
                EnoughPoints[i] = 1
            if self.secondary_var_name == 'None':
                secondary_vars[i] = 'None'
            else:
                secondary_vars[i] = DataVarValue[self.secondary_var_name].iloc[0]
        AvailPoints  = np.around(AvailPoints , decimals=0)
        EnoughPoints = np.around(EnoughPoints, decimals=0)     
        return AvailPoints, EnoughPoints, secondary_vars
    
    def fix_pricing_model_inputs(self, y, q, P):
        """Fixes problems with extreme values of booking probability and with cases
        where there is no booked session.
        Args:
            y (float):    y[i] = 1 booked session, y[i] = 0 non-booked session
            q (float):    q[i] - booking probability of the session (output of the booking probability model)
            P (float):    P[i] - price offered to the customer
        Returns:
            y, q, P
        """
        # Identify and fix points with purchase probability close to 0
        q[ q < 0.01 ] = 0.01
        # Identify and fix points with purchase probability close to 1
        q[ q > 0.99 ] = 0.99
        if len( y[ y > 0 ] ) == 0:
            # no booked session in the input data, we'll create one booked session (y=1)
            # with offered price equal to mean offered price and purchase probability
            # equal to maximim purchase probability
            y = np.concatenate( ( y , np.array([1])          ), axis=0 )
            P = np.concatenate( ( P , np.array([np.mean(P)]) ), axis=0 )
            if np.max(q) - np.min(q) > 0.1:
                q = np.concatenate( ( q , np.array([np.max(q)])  ), axis=0 )
            else:
                q = np.concatenate( ( q , np.array([0.5])  ), axis=0 )
        return y, q, P
    
    def starting_point(self, q, P):
        """Given the vector of purchase probabiities and offered ancillary prices, calculates starting point
        coordinates for all three pricing models.
        Args:
            q (float):     q[i] - booking probability of the session (output of the booking probability model)
            P (float):     P[i] - price offered to the customer
        Returns:
            X0_IL (float): starting point coordinates for Inverse Logit Model
            X0_LM (float): starting point coordinates for Logistic Price Mapping Model
            X0_EM (float): starting point coordinates for Exponential Price Mapping Model
        """
        X0_IL = np.zeros(2)
        X0_LM = np.zeros(3)
        X0_EM = np.zeros(3)
        Pmax  = np.max(P)
        Pmin  = np.min(P)
        qmax  = np.max(q)
        qmin  = np.min(q)
  
        # 1: Inverse Logit Model
        xmin = np.log( qmin / ( 1 - qmin) )
        xmax = np.log( qmax / ( 1 - qmax) )
        X0_IL[0] = Pmin - xmin * ( (Pmax - Pmin) / (xmax - xmin) )
        X0_IL[1] = (Pmax - Pmin) / (xmax - xmin)
  
        # 2: Logistic Price Mapping Model
        X0_LM[0] = 2 * np.mean(P)
        X0_LM[1] = 3
        X0_LM[2] = np.mean(q)
  
        # 3: Exponential Price Mapping Model
        X0_EM[0] = Pmax - qmax**2 * ( (Pmax - Pmin) / (qmax**2 - qmin**2) )
        X0_EM[1] = (Pmax - Pmin) / (qmax**2 - qmin**2)
        X0_EM[2] = 2
    
        return X0_IL, X0_LM, X0_EM
    
    def fit_pricing_models(self, X0_IL, X0_LM, X0_EM, y, q, P):
       
       """Fits three pricing models to the data.
       Args:
            X0_IL (float):   starting point for the fitting of Inverse Logit Model
            X0_LM (float):   starting point for the fitting of Logistic Price Mapping Model
            X0_EM (float):   starting point for the fitting of Exponential Price Mapping Model
            y (float):       y[i] = 1 booked session, y[i] = 0 non-booked session
            q (float):       q[i] - booking probability of the session (output of the booking probability model)
            P (float):       P[i] - price offered to the customer
       Returns:
            par_IL (float):  vector of fitted parameters of the Inverse Logit Model
            par_LM (float):  vector of fitted parameters of the Logistic Price Mapping Model
            par_EM (float):  vector of fitted parameters of the Exponential Price Mapping Model
            loss_IL (float): optimum loss function value of the Inverse Logit Model
            loss_LM (float): optimum loss function value of the Logistic Price Mapping Model
            loss_EM (float): optimum loss function value of the Exponential Price Mapping Model
       """
       # Estimate model 1: Inverse Logit Model
       res_IL  = optimize.minimize(self.loss_inv_logit    , X0_IL, args=(y,q,P), method='BFGS', jac=self.grad_inv_logit)
       par_IL  = res_IL.x
       loss_IL = self.loss_inv_logit(par_IL, y, q, P)
    
       # Estimate model 2: Logistic Price Mapping Model
       res_LM  = optimize.minimize(self.loss_log_price_map, X0_LM, args=(y,q,P), method='BFGS', jac=self.grad_log_price_map)
       par_LM  = res_LM.x
       loss_LM = self.loss_log_price_map(par_LM, y, q, P)
    
       # Estimate model 3: Exponential Price Mapping Model
       res_EM  = optimize.minimize(self.loss_exp_price_map, X0_EM, args=(y,q,P), method='BFGS', jac=self.grad_exp_price_map)
       par_EM  = res_EM.x
       loss_EM = self.loss_exp_price_map(par_EM, y, q, P)
    
       return par_IL, par_LM, par_EM, loss_IL, loss_LM, loss_EM
    
    def identify_best_model(self, loss_IL, loss_LM, loss_EM, par_IL, par_LM, par_EM):
        """Identifies the best pricing model as the model with lowest value of loss function.
        Args:
           loss_IL (float): optimum loss function value of the Inverse Logit Model
           loss_LM (float): optimum loss function value of the Logistic Price Mapping Model
           loss_EM (float): optimum loss function value of the Exponential Price Mapping Model
           par_IL (float):  vector of fitted parameters of the Inverse Logit Model
           par_LM (float):  vector of fitted parameters of the Logistic Price Mapping Model
           par_EM (float):  vector of fitted parameters of the Exponential Price Mapping Model
        Returns:
           BestMod (float): best pricing model index (0,1,2)
           BestModel (str): best pricing model name
           OptVars (float): vector of fitted parameters of the best pricing model
           OptLoss (float): loss function value of the best pricing model
        """
        LossFunValues = np.array([loss_IL, loss_LM, loss_EM])
        BestMod = np.argmin(LossFunValues)
        OptVars = np.zeros(self.n_fitted_pars)
        if BestMod == 0:
            OptVars[0:self.n_fitted_pars-1] = par_IL
            OptLoss   = loss_IL
            BestModel = "inv_logit"
        elif BestMod == 1:
            OptVars[0:self.n_fitted_pars] = par_LM
            OptLoss   = loss_LM
            BestModel = "log_price_map"
        else:
            OptVars[0:self.n_fitted_pars] = par_EM
            OptLoss   = loss_EM
            BestModel = "exp_price_map"
        
        return BestMod, BestModel, OptVars, OptLoss

    def plus(self, x):
        """well known plus function
        """
        return max(x,0)

    def lower_price_bound(self, P, y):
        """lower price bound needed for the calculation of loss function
        Args:
            P (float):       price offered to the customer
            y (float):       y = 1 booked session, y = 0 non-booked session
        Returns:
            lower price bound
        """
        return y*P + (1-y)*self.c[0]*P

    def upper_price_bound(self, P, y):
        """upper price bound needed for the calculation of loss function
        Args:
            P (float):       price offered to the customer
            y (float):       y = 1 booked session, y = 0 non-booked session
        Returns:
            upper price bound
        """
        return (1-y)*P + y*self.c[1]*P

    def inv_logit(self, theta, q):
        """inverse logit pricing function
        Args:
            theta (float):   vector containing pricing function parameters
            q (float):       booking probability of the session (output of the booking probability model)
        Returns:
            inverse logit pricing function value
        """
        return theta[0] + theta[1] * np.log( q / (1-q) )

    def log_price_map(self, theta, q):
        """logistic pricing function
        Args:
            theta (float):   vector containing pricing function parameters
            q (float):       booking probability of the session (output of the booking probability model)
        Returns:
            logistic pricing function value
        """
        return theta[0] / ( 1 + np.exp( - ( theta[1] + theta[2] * q ) ) )

    def exp_price_map(self, theta, q):
        """exponential pricing function
        Args:
            theta (float):   vector containing pricing function parameters
            q (float):       booking probability of the session (output of the booking probability model)
        Returns:
            exponential pricing function value
        """
        return theta[0] + theta[1] * q**theta[2]

    def loss_inv_logit(self, X, y, q, P):
        """Inverse Logit Model: Given the current vector X and other parameters, calculates the loss function value.
        Args:
           X (float):    vector of optimization variables to be learned by minimizing loss
           y (float):    y[i] = 1 booked session, y[i] = 0 non-booked session
           q (float):    q[i] - booking probability of the session (output of the booking probability model)
           P (float):    P[i] - price offered to the customer
        Returns:
           Loss (float): loss function value at X 
        """
        # Number of data points / sessions / lines of the data file
        N = len(y)
        Loss  = 0
        for i in range(N):
            PricingFunction = self.inv_logit(X,q[i])
            Loss += self.plus( self.lower_price_bound(P[i],y[i]) - PricingFunction ) + self.plus( PricingFunction - self.upper_price_bound(P[i],y[i]) )   
        return Loss

    def grad_inv_logit(self, X, y, q, P):
        """Inverse Logit Model: Given the current vector X and other parameters, calculates the gradient of loss function.
        Args:
           X (float):    vector of optimization variables to be learned by minimizing loss
           y (float):    y[i] = 1 booked session, y[i] = 0 non-booked session
           q (float):    q[i] - booking probability of the session (output of the booking probability model)
           P (float):    P[i] - price offered to the customer
        Returns:
           LossGr (float): gradient of Loss function at X 
        """
        # Number of data points / sessions / lines of the data file
        N = len(y)
        # Number of optimization variables
        n_opt = len(X)
        LossGr = np.zeros(n_opt)
        for i in range(N):
            PricingFunction = self.inv_logit(X,q[i])
            if self.lower_price_bound(P[i],y[i]) - PricingFunction > 0:
                LossGr[0] += - 1
                LossGr[1] += - 1 * np.log( q[i]/(1-q[i]) )    
            if PricingFunction - self.upper_price_bound(P[i],y[i]) > 0:
                LossGr[0] += + 1
                LossGr[1] += + 1 * np.log( q[i]/(1-q[i]) )      
        return LossGr

    def loss_log_price_map(self, X, y, q, P):
        """Logistic Price Mapping Model: Given the current vector X and other parameters, calculates the loss function value.
        Args:
           X (float):    vector of optimization variables to be learned by minimizing loss
           y (float):    y[i] = 1 booked session, y[i] = 0 non-booked session
           q (float):    q[i] - booking probability of the session (output of the booking probability model)
           P (float):    P[i] - price offered to the customer
        Returns:
           Loss (float): loss function value at X 
        """
        # Number of data points / sessions / lines of the data file
        N = len(y)
        Loss  = 0
        for i in range(N):
            PricingFunction = self.log_price_map(X,q[i])
            Loss += self.plus( self.lower_price_bound(P[i],y[i]) - PricingFunction ) + self.plus( PricingFunction - self.upper_price_bound(P[i],y[i]) ) 
        return Loss

    def grad_log_price_map(self, X, y, q, P):
        """Logistic Price Mapping Model: Given the current vector X and other parameters, calculates the gradient of loss function.
        Args:
           X (float):    vector of optimization variables to be learned by minimizing loss
           y (float):    y[i] = 1 booked session, y[i] = 0 non-booked session
           q (float):    q[i] - booking probability of the session (output of the booking probability model)
           P (float):    P[i] - price offered to the customer
        Returns:
           LossGr (float): gradient of Loss function at X 
        """
        # Number of data points / sessions / lines of the data file
        N = len(y)
        # Number of optimization variables
        n_opt = len(X)
        LossGr = np.zeros(n_opt)
        for i in range(N):
            PricingFunction = self.log_price_map(X,q[i])
            EE = np.exp( - ( X[1] + X[2] * q[i] ) )
            if self.lower_price_bound(P[i],y[i]) - PricingFunction > 0:
                LossGr[0] += - 1 / ( 1 + EE )
                LossGr[1] += - ( X[0] * 1    * EE ) / ( 1 + EE )**2
                LossGr[2] += - ( X[0] * q[i] * EE ) / ( 1 + EE )**2
            if PricingFunction - self.upper_price_bound(P[i],y[i]) > 0:
                LossGr[0] += + 1 / ( 1 + EE )
                LossGr[1] += + ( X[0] * 1    * EE ) / ( 1 + EE )**2
                LossGr[2] += + ( X[0] * q[i] * EE ) / ( 1 + EE )**2
        return LossGr

    def loss_exp_price_map(self, X, y, q, P):
        """Exponential Price Mapping Model: Given the current vector X and other parameters, calculates the loss function value.
        Args:
           X (float):    vector of optimization variables to be learned by minimizing loss
           y (float):    y[i] = 1 booked session, y[i] = 0 non-booked session
           q (float):    q[i] - booking probability of the session (output of the booking probability model)
           P (float):    P[i] - price offered to the customer
        Returns:
           Loss (float): loss function value at X 
        """
        # Number of data points / sessions / lines of the data file
        N = len(y)
        Loss  = 0
        for i in range(N):
            PricingFunction = self.exp_price_map(X,q[i])
            Loss += self.plus( self.lower_price_bound(P[i],y[i]) - PricingFunction ) + self.plus( PricingFunction - self.upper_price_bound(P[i],y[i]) ) 
        return Loss

    def grad_exp_price_map(self, X, y, q, P):
        """Exponential Price Mapping Model: Given the current vector X and other parameters, calculates the gradient of loss function.
        Args:
           X (float):    vector of optimization variables to be learned by minimizing loss
           y (float):    y[i] = 1 booked session, y[i] = 0 non-booked session
           q (float):    q[i] - booking probability of the session (output of the booking probability model)
           P (float):    P[i] - price offered to the customer
        Returns:
        LossGr (float): gradient of Loss function at X 
        """
        # Number of data points / sessions / lines of the data file
        N = len(y)
        # Number of optimization variables
        n_opt = len(X)
        LossGr = np.zeros(n_opt)
        for i in range(N):
            PricingFunction = self.exp_price_map(X,q[i])
            if self.lower_price_bound(P[i],y[i]) - PricingFunction > 0:
                LossGr[0] += - 1 
                LossGr[1] += - q[i]**X[2]
                LossGr[2] += - X[1] * np.log( q[i] ) * q[i]**X[2]
            if PricingFunction - self.upper_price_bound(P[i],y[i]) > 0:
                LossGr[0] += + 1 
                LossGr[1] += + q[i]**X[2]
                LossGr[2] += + X[1] * np.log( q[i] ) * q[i]**X[2]      
        return LossGr