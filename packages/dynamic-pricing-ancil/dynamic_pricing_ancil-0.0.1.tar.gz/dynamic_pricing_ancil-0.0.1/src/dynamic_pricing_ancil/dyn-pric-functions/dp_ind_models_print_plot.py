import numpy as np
from matplotlib import pyplot as plt

def plot_graph(y, q, P, params, loss, model, var_val):
    N = len(y)
    Pmax = np.max(P)
    Pmin = np.min(P)
    if N > 1000:
        ind = np.random.choice( N, 1000 )
        y = y[ind]
        q = q[ind]
        P = P[ind]
        N = 1000
        
    loss = np.around(loss, decimals=1)
    npoints = 1000
    probs  = np.linspace(0.001,0.999,num=npoints)
    prices = []
    if model == "inv_logit":
        for i in range(npoints):
            prices.append( inv_logit(params,probs[i]) )
        StringToBePrinted = var_val + ", Inverse Logit, loss = " + str(loss)
        plt.title(StringToBePrinted)
    elif model == "log_price_map":
        for i in range(npoints):
            prices.append( log_price_map(params,probs[i]) )
        StringToBePrinted = var_val + ", Logistic Price Map., loss = " + str(loss)
        plt.title(StringToBePrinted)
    else:
        for i in range(npoints):
            prices.append( exp_price_map(params,probs[i]) )
        StringToBePrinted = var_val + ", Exponential Price Map., loss = " + str(loss)
        plt.title(StringToBePrinted)
        
    plt.xlabel("Purchase probability")
    plt.ylabel("Ancillary Price")
    for i in range(N):
        if y[i] == 0:
            plt.scatter(q[i],P[i],color = "red")
        else:
            plt.scatter(q[i],P[i],color = "green")
    plt.xlim(0, 1)
    plt.ylim(0.9*Pmin, 1.1*Pmax)
    plt.plot(probs, prices)
    plt.show()
    
def print_price_models(var_values, BestModel, OptVars):
    """Print of a matrix in a format required by numpy
    
    Args:
        var_values (str): Vector containing unique values of variable var_name
        BestModel (str):  Vector containing best pricing model name (for individual var_values) 
        OptVars (float):  Matrix of fitted parameters of the best pricing model (for individual var_values)
        
    Returns:
        string (str):     String - python list - containing all input values   
    """
    nrow = OptVars.shape[0]    # number of rows
    ncol = OptVars.shape[1]    # number of columns
    string = "PriceModels" + " = [["
    for i in range(nrow):
        string += "'" + var_values[i] + "'"
        string +=  ", "
        string += "'" + BestModel[i] + "'"
        string +=  ", "
        for j in range(ncol):
            string += str(OptVars[i][j])
            if j < ncol-1:
                string +=  ", "
            else:
                if i < nrow-1:
                    string +=  "], \n["
                else:
                    string +=  "]]"          
    return string   

def inv_logit(theta, q):
    return theta[0] + theta[1] * np.log( q / (1-q) )

def log_price_map(theta, q):
    return theta[0] / ( 1 + np.exp( - ( theta[1] + theta[2] * q ) ) )

def exp_price_map(theta, q):
    return theta[0] + theta[1] * q**theta[2]