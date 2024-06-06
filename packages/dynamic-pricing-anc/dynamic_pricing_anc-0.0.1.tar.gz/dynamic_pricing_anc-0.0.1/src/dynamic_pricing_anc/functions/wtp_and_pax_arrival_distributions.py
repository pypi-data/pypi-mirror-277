import numpy as np

from scipy.stats import norm
from scipy.stats import poisson
from scipy.special import binom
    
def pax_wtp_dir_probit(x, lamb, sigma, delta):
    """Calculates probability that customer is willing to pay price <= x.
    
    Direct problem, PROBIT model describing PAX willingness to pay is used.
    
    Args:
        x (float):      price
        lamb (float):   first parameter  of distribution describing PAX willingness to pay
        sigma (float):  second parameter of distribution describing PAX willingness to pay
        delta (float):  third parameter  of distribution describing PAX willingness to pay

    Returns:
        Prob (float):   probability that customer is willing to pay price <= x 

    """
    z = lamb + sigma * x
    Prob = norm.cdf(z)
    return Prob

def pax_wtp_dir_logit(x, lamb, sigma, delta):
    """Calculates probability that customer is willing to pay price <= x.
    
    Direct problem, LOGIT model describing PAX willingness to pay is used. 
    
    Args:
        x (float):      price
        lamb (float):   first parameter  of distribution describing PAX willingness to pay
        sigma (float):  second parameter of distribution describing PAX willingness to pay
        delta (float):  third parameter  of distribution describing PAX willingness to pay

    Returns:
        Prob (float):   probability that customer is willing to pay price <= x 

    """
    z = lamb + sigma * x
    Prob = 1 / ( 1 + np.exp(-z) )
    return Prob

def pax_wtp_dir_gen_logit(x, lamb, sigma, delta):
    """Calculates probability that customer is willing to pay price <= x.
    
    Direct problem, GENERALIZED LOGIT model describing PAX willingness to pay is used.
    
    Args:  
        x (float):      price
        lamb (float):   first parameter  of distribution describing PAX willingness to pay
        sigma (float):  second parameter of distribution describing PAX willingness to pay
        delta (float):  third parameter  of distribution describing PAX willingness to pay

    Returns:
        Prob (float):   probability that customer is willing to pay price <= x 

    """
    z = lamb + sigma * x
    Prob = 1 / ( 1 + np.exp(-z) )**delta
    return Prob

def pax_wtp_inv_probit(Prob, lamb, sigma, delta):
    """Calculates the price x that corresponds to given probability Prob.
    
    Inverse problem, PROBIT model describing PAX willingness to pay is used.
    
    Args:
        Prob (float):   probability that customer is willing to pay price <= x 
        lamb (float):   first parameter  of distribution describing PAX willingness to pay
        sigma (float):  second parameter of distribution describing PAX willingness to pay
        delta (float):  third parameter  of distribution describing PAX willingness to pay
    
    Returns:
        x (float):      price
    
    """
    x = ( norm.ppf(Prob) - lamb ) / sigma
    return x

def pax_wtp_inv_logit(Prob, lamb, sigma, delta):
    """Calculates the price x that corresponds to given probability Prob.
    
    Inverse problem, LOGIT model describing PAX willingness to pay is used.
    
    Args:
        Prob (float):   probability that customer is willing to pay price <= x 
        lamb (float):   first parameter  of distribution describing PAX willingness to pay
        sigma (float):  second parameter of distribution describing PAX willingness to pay
        delta (float):  third parameter  of distribution describing PAX willingness to pay
    
    Returns:
        x (float):      price
    
    """
    x = (1/sigma) * ( np.log(Prob/(1-Prob)) - lamb )
    return x

def pax_wtp_inv_gen_logit(Prob, lamb, sigma, delta):
    """Calculates the price x that corresponds to given probability Prob.
    
    Inverse problem, GENERALIZED LOGIT model describing PAX willingness to pay is used.
    
    Args:
        Prob (float):   probability that customer is willing to pay price <= x 
        lamb (float):   first parameter  of distribution describing PAX willingness to pay
        sigma (float):  second parameter of distribution describing PAX willingness to pay
        delta (float):  third parameter  of distribution describing PAX willingness to pay
    
    Returns:
        x (float):      price
    
    """
    denom = (1/Prob)**(1/delta) - 1
    x = (1/sigma) * ( np.log(1/denom) - lamb )
    return x
    
def pax_arrivals_poisson(n, mu_arr, si_arr):
    """Calculates the probability that the number of arriving customers is equal to n.
    
    POISSON distribution describing PAX arrivals is used.
 
    Args:
        n (int):        n
        mu_arr (float): mean of distribution describing PAX arrivals
        si_arr (float): second parameter of distribution describing PAX arrivals
    
    Returns:
        Pr_demand_eq_n (float): probability that the number of ariving PAX = n
    
    """
    Pr_demand_eq_n = poisson.pmf(n, mu_arr)
    return Pr_demand_eq_n

def pax_arrivals_normal(n, mu_arr, si_arr):
    """Calculates the probability that the number of arriving customers is equal to n.
    
    NORMAL distribution describing PAX arrivals is used.
 
    Args:
        n (int):        n
        mu_arr (float): mean of distribution describing PAX arrivals
        si_arr (float): second parameter of distribution describing PAX arrivals
    
    Returns:
        Pr_demand_eq_n (float): probability that the number of ariving PAX = n
    
    """
    Pr_demand_eq_n = norm.cdf( (n + 0.5 - mu_arr) / si_arr ) - norm.cdf( (n - 0.5 - mu_arr) / si_arr )
    return Pr_demand_eq_n

def pax_arrivals_fixed(n, mu_arr, si_arr):
    """Calculates the probability that the number of arriving customers is equal to n.
    
    FIXED NUMBER of arriving pax is considered.
 
    Args:
        n (int):        n
        mu_arr (float): mean of distribution describing PAX arrivals
        si_arr (float): second parameter of distribution describing PAX arrivals
    
    Returns:
        Pr_demand_eq_n (float): probability that the number of ariving PAX = n
    
    """
    if n == mu_arr:
        Pr_demand_eq_n = 1
    else:
        Pr_demand_eq_n = 0
    return Pr_demand_eq_n