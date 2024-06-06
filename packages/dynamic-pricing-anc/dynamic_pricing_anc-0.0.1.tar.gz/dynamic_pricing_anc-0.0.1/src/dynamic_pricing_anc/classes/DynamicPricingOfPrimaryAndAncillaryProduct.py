import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy.stats import norm
from scipy.stats import poisson
from scipy.special import binom
from scipy.optimize import minimize_scalar

class DynamicPricingOfPrimaryAndAncillaryProduct:
    """This prototype considers single leg flight with a fixed capacity of primary products (seats). Total expected 
    revenue is maximized by dynamically setting prices on both the primary product and the ancillary service. 
    The booking period of the flight is divided into time periods. In each period, a random number of customers 
    arrive each of whom may belong to one of three groups: 
        1. those that only want the primary products.
        2. those that would buy the ancillary service if the price is right.
        3. those that only purchase a primary product together with the ancillary service.
    ___________________________________________________________________________________________________________________
    General stochastic formulation is implemented here which does not require specific distributional assumptions 
    on the arrival process or the underlying customers' willingness-to-pay. The multi period dynamic pricing model 
    is formulated as dynamic program. First, the optimality equation for the final period (closest to departure) 
    is solved. By backward induction, we then solve the optimality equations for the time periods 2, 3, .., n.
    ___________________________________________________________________________________________________________________
    Three different models of customers' willingness-to-pay are currently supported:
        1. probit model characterized by two estimated parameters
        2. logit model characterized by two estimated parameters
        3. generalized logit model characterized by three estimated parameters
    Three different distributionss of PAX arrivals are currently supported:
        1. poisson distribution characterized by mean demand
        2. normal distribution characterized by mean demand and demand standard deviation
        3. fixed number characterized by mean demand
    ___________________________________________________________________________________________________________________
    Fredrik Odegaard, John G. Wilson. 2016. Dynamic pricing of primary products and ancillary services  
    ___________________________________________________________________________________________________________________
    Main Inputs:
        1. Remaining capacity of the aircraft
        2. Estimated models of customer's willingness-to-pay for each time period and customer group
        3. Estimated probability distributions of arrivals of customers for each time period
        4. Estimated probability a customer belongs to group i (i = 1,2,3) in time period t
    Calculated outputs:
        1. Optimum primary price and ancillary price for each time period
        2. Optimum purchase probability for each time period
    ___________________________________________________________________________________________________________________
    Args:
        n_periods (int):     number of time periods
        dist_wtp_dir (str):  probability distribution describing PAX willingness to pay, direct problem
            dist_wtp_dir = pax_wtp_dir_probit     PROBIT model used
            dist_wtp_dir = pax_wtp_dir_logit      LOGIT model used
            dist_wtp_dir = pax_wtp_dir_gen_logit  GENERALIZED LOGIT model used
        dist_wtp_inv (str):  probability distribution describing PAX willingness to pay, inverse problem
            dist_wtp_inv = pax_wtp_inv_probit     PROBIT model used
            dist_wtp_inv = pax_wtp_inv_logit      LOGIT model used
            dist_wtp_inv = pax_wtp_inv_gen_logit  GENERALIZED LOGIT model used
        dist_arr (str): probability distribution describing PAX arrivals
            dist_arr = pax_arrivals_poisson       POISSON distribution used
            dist_arr = pax_arrivals_normal        NORMAL distribution used
            dist_arr = pax_arrivals_fixed         FIXED NUMBER distribution used
        step (float):        step to calculate uz and lz (lower and upper price bounds)
    """
    def __init__(self, n_periods, dist_wtp_dir, dist_wtp_inv, dist_arr, step=5):
        self.n_periods = n_periods
        self.dist_wtp_dir = dist_wtp_dir
        self.dist_wtp_inv = dist_wtp_inv
        self.dist_arr = dist_arr
        self.step = step

    def fit(self, capacity_remaining, mu_arr, si_arr, Nmax, Alpha, Lambda, Sigma, Delta):
        """STOCHASTIC OPTIMIZATION OF PRIMARY PRODUCTS AND ANCILLARY SERVICES (DYNAMIC PRICING).
        Args:
            capacity_remaining (float): remaining capacity of the aircraft
            mu_arr (float):             vector, mu_arr[t] - PAX arrivals in time period t: mean
            si_arr (float):             vector, si_arr[t] - PAX arrivals in time period t: second parameter
            Nmax (float):               vector, Nmax[t] - maximum number of arriving customers in time period t
            Alpha (float):              matrix, Alpha[t,i] - probability a customer in time period t belongs to group i 
            Lambda (float):             matrix, Lambda[t,i] - willingness to pay of group i customers in period t: first parameter
            Sigma (float):              matrix, Sigma[t,i] - willingness to pay of group i customers in period t: second parameter
            Delta (float):              matrix, Delta[t,i] - willingness to pay of group i customers in period t: third parameter
        Returns:
            OptPrice[:,0] (float):      optimum primary price in individual time periods 
            OptPrice[:,1] (float):      optimum ancillary price in individual time periods
            DP_Solution:                dataframe containing the calculated results
        """
        zz               = np.linspace(1.0, 79.0, num=79) / 80
        self.npoints     = len(zz)
        self.OptPrice    = np.zeros(( self.n_periods, 7 ))
        OptZ             = np.zeros(( self.n_periods, capacity_remaining ))
        ValueFun         = np.zeros(( self.n_periods, capacity_remaining ))
        ValueFun_t_min_1 = np.zeros(capacity_remaining)
        for t in range(self.n_periods):             # Loop over time periods 
            # 1. Read the input parameters characterizing period t
            alpha_t  = Alpha[t,]
            lambda_t = Lambda[t,]
            sigma_t  = Sigma[t,]
            delta_t  = Delta[t,]
            ######################
            mu_arr_t = mu_arr[t]
            si_arr_t = si_arr[t]
            Nmax_t   = Nmax[t]
            step_t   = self.step
            ######################
            ValueFun_t = np.zeros(capacity_remaining)
            
            # 2. Calculate Value Function for all values of capacity
            for c in range( 1, capacity_remaining+1 ):        # Loop over values of capacity remaining
                # Solve optimization problem for z
                Optimum = minimize_scalar(self.fun_optimality_period_t,method='bounded',bounds=(0,1),args=(step_t,alpha_t,lambda_t,sigma_t,delta_t,mu_arr_t,si_arr_t,Nmax_t,c,ValueFun_t_min_1))
                z_opt   = Optimum.x
                OptZ[t,c-1] = z_opt
                # Calculate and store values of the Value Function
                ValueFun_t[c-1] = -self.fun_optimality_period_t(z_opt,step_t,alpha_t,lambda_t,sigma_t,delta_t,mu_arr_t,si_arr_t,Nmax_t,c,ValueFun_t_min_1)
                ValueFun[t,c-1] = ValueFun_t[c-1]
                
            # Identify c with maximum value of Value Function, calculate and store optimum prices for period t
            MaxValFun = max( ValueFun_t )
            BestC     = np.argmax( ValueFun_t )
            BestC     = BestC.astype(int)
            BestZ     = OptZ[t,BestC]
            OptPrices = self.calculate_opt_prices(BestZ,step_t,alpha_t,lambda_t,sigma_t,delta_t)
            self.OptPrice[t,0] = max(OptPrices[0],0)   # p1_z
            self.OptPrice[t,1] = max(OptPrices[1],0)   # p2_z
            self.OptPrice[t,2] = MaxValFun             # maximum value of Value Function
            self.OptPrice[t,3] = BestZ                 # z value corresponding to BestC
            self.OptPrice[t,4] = BestC                 # c value with maximum value of Value Function
            self.OptPrice[t,5] = OptPrices[2]          # lz - lower primary price
            self.OptPrice[t,6] = OptPrices[3]          # uz
    
            ValueFun_t_min_1 = ValueFun_t
    
        TimePeriod = np.linspace(1, self.n_periods, num=self.n_periods)
        TimePeriod = TimePeriod.astype(int)
        DP_Solution = pd.DataFrame({'TimePeriod':TimePeriod,'PrimaryPrice':self.OptPrice[:,0],'AncillaryPrice':self.OptPrice[:,1],'PurchaseProb':self.OptPrice[:,3],'ValueFunction':self.OptPrice[:,2]})

        return self.OptPrice[:,0], self.OptPrice[:,1], DP_Solution
    
    def fun_optimality_period_t(self,z,step,alpha,lamb,sigma,delta,mu_arr,si_arr,Nmax,Cap,ValueFun):
        """Objective function to determine the optimum value of Value Function. Given the probability of sale z, 
        remaining capacity Cap, vector containing values of the Value Function from the previous time periof t-1 
        and other parameters, calculates the value of Value Function.
        Args:
            z (float):          probability of sale during a time period, parameter from (0,1)
            step (float):       increment of the iterative numerical method
            alpha (float):      alpha[i] - probability a customer belongs to group i, i=1,2,3
            lamb (float):       first parameter  of distribution describing PAX willingness to pay
            sigma (float):      second parameter of distribution describing PAX willingness to pay
            delta (float):      third parameter  of distribution describing PAX willingness to pay
            mu_arr (float):     mean of distribution describing PAX arrivals
            si_arr (float):     second parameter of distribution describing PAX arrivals
            Nmax (int):         maximum number of arriving customers in individual time periods
            Cap (int):          capacity
            ValueFun (float):   vector containing values of the Value Function from previous time period t-1: Vt-1(x), V0(x) = 0
        Returns:
            Fun (float):        value of function to be maximized (we return -Fun because we're using minimization alg.)
        """
        # 1. solve equation for uz
        uz = self.solve_for_uz(z,step,alpha,lamb,sigma,delta)
    
        # 2. calculate lz
        lz = self.solve_for_lz(z,step,alpha,lamb,sigma,delta)
    
        # 3. Solve optimization problem for p1
        Optimum = minimize_scalar(self.fun_maximize_p1, method='bounded', bounds=(lz, uz), args=(z, alpha, lamb, sigma, delta) )
        q1_z    = Optimum.x
    
        # 4. Calculate q2_z
        q2_z    = self.calculate_q2_z(q1_z,z,alpha,lamb,sigma,delta)
    
        # 5. Calculate p1_z, p2_z
        if lz < uz:
            p1_z = q1_z
            p2_z = q2_z
        else:
            p1_z = uz
            p2_z = 0
            
        # 6. Calculate pi_z
        pi_z = self.calculate_pi_z(p1_z,p2_z,z,alpha,lamb,sigma,delta)
    
        # 7. Calculate E_min_Dt
        # probability mass function
        h_t_x_z = np.zeros(Cap)
        for x in range(0, Cap ):
            h_t_x_z[x] = self.pmf_ht_x_z(Nmax,mu_arr,si_arr,z,x)
        # cumulative distribution function
        H_t_x_z  = np.cumsum(h_t_x_z)
        E_min_Dt = self.calculate_e_min_dt(h_t_x_z, H_t_x_z, Cap)
  
        # 8. Calculate Value Function
        Fun = pi_z * E_min_Dt
    
        if Cap > 1:
            for x in range(1, Cap ):
                Fun = Fun + ValueFun[Cap-x-1] * h_t_x_z[x]
            
        return -Fun
    
    def calculate_opt_prices(self,z,step,alpha,lamb,sigma,delta):
        """Calculates optimum prices for primary and ancillary products.
        Args:
            z (float):      probability of sale during a time period, parameter from (0,1)
            step (float):   increment of the iterative numerical method
            alpha (float):  alpha[i] - probability a customer belongs to group i, i=1,2,3
            lamb (float):   first parameter  of distribution describing PAX willingness to pay
            sigma (float):  second parameter of distribution describing PAX willingness to pay
            delta (float):  third parameter  of distribution describing PAX willingness to pay    
        Returns:
            p1_z (float):   price of the primary product (airfare)
            p2_z (float):   price of the secondary product (ancillary)
            lz (float):     lower price bound on primary product price
            uz (float):     upper price bound on primary product price
        """
        # 1. solve equation for uz
        uz = self.solve_for_uz(z,step,alpha,lamb,sigma,delta)
    
        # 2. calculate lz
        lz = self.solve_for_lz(z,step,alpha,lamb,sigma,delta)
    
        # 3. Solve optimization problem for p1
        Optimum = minimize_scalar(self.fun_maximize_p1, method='bounded', bounds=(lz, uz), args=(z, alpha, lamb, sigma, delta) )
        q1_z    = Optimum.x

        # 4. Calculate q2_z
        q2_z    = self.calculate_q2_z(q1_z,z,alpha,lamb,sigma,delta)
  
        # 5. Calculate p1_z, p2_z
        if lz < uz:
            p1_z = q1_z
            p2_z = q2_z
        else:
            p1_z = uz
            p2_z = 0
    
        OptPrices = np.zeros(4)
        OptPrices[0] = p1_z
        OptPrices[1] = p2_z
        OptPrices[2] = lz
        OptPrices[3] = uz
    
        return OptPrices
    
    def solve_for_uz(self, z, step, alpha, lamb, sigma, delta):
        """Calculates upper price bound uz. Given the probability of sale z and other parameters, 
        solves the equation for uz (upper price bound): 
        z=alpha1(1-F1(uz))+alpha2(1-F2(uz))+alpha3(1-F3(uz)) 
        Args:
            z (float):       probability of sale during a time period, parameter from (0,1)
            step (float):    increment of the iterative numerical method
            alpha (float):   alpha[i] - probability a customer belongs to group i, i=1,2,3
            lamb (float):    first parameter  of distribution describing PAX willingness to pay
            sigma (float):   second parameter of distribution describing PAX willingness to pay
            delta (float):   third parameter  of distribution describing PAX willingness to pay
        Returns:
            uz (float):      upper price bound
        """
        uz_L  = 0
        uz_U  = 0
        Fuz_L = 1 - z
        Fuz_U = 1 - z
        while Fuz_U >= 0:
            uz_L  = uz_U
            uz_U  = uz_L + step
            Fuz_L = Fuz_U
            F1    = self.pax_will_to_pay_direct(uz_U,lamb[0],sigma[0],delta[0])
            F2    = self.pax_will_to_pay_direct(uz_U,lamb[1],sigma[1],delta[1])
            F3    = self.pax_will_to_pay_direct(uz_U,lamb[2],sigma[2],delta[2])
            Fuz_U = alpha[0] * (1-F1) + alpha[1] * (1-F2) + alpha[2] * (1-F3) - z
        talfa   = (Fuz_L - Fuz_U) / step
        delta_z = Fuz_L / talfa
        uz      = uz_L + delta_z
        F1      = self.pax_will_to_pay_direct(uz,lamb[0],sigma[0],delta[0])
        F2      = self.pax_will_to_pay_direct(uz,lamb[1],sigma[1],delta[1])
        F3      = self.pax_will_to_pay_direct(uz,lamb[2],sigma[2],delta[2])
        Fuz     = alpha[0] * (1-F1) + alpha[1] * (1-F2) + alpha[2] * (1-F3) - z
        return uz

    def solve_for_lz(self, z, step, alpha, lamb, sigma, delta):
        """Calculates lower price bound lz. Given the probability of sale z and other parameters, 
        solves the equation for lz (lower price bound):
           lz = F-1(max{ (alpha1+alpha2-z)/(alpha1+alpha2) , 0 })
           F(x) = ( alpha1 F1(x) + alpha2 F2(x) ) / (alpha1+alpha2) , F(x) - mixture dustribution
        Args:
            z (float):        probability of sale during a time period, parameter from (0,1)
            step (float):     increment of the iterative numerical method
            alpha (float):    alpha[i] - probability a customer belongs to group i, i=1,2,3
            lamb (float):     first parameter  of distribution describing PAX willingness to pay
            sigma (float):    second parameter of distribution describing PAX willingness to pay
            delta (float):    third parameter  of distribution describing PAX willingness to pay
        Returns:
            lz (float):       lower price bound
        """
        c1   = alpha[0] / (alpha[0] + alpha[1])
        c2   = alpha[1] / (alpha[0] + alpha[1])
        prob = ( alpha[0] + alpha[1] - z ) / (alpha[0] + alpha[1])
        if prob <= 0: 
            lz  = 0
            Flz = 0
        else: 
            lz_L  = 0
            lz_U  = 0
            Flz_L = prob
            Flz_U = prob
            while Flz_U >= 0:
                lz_L  = lz_U
                lz_U  = lz_L + step
            Flz_L = Flz_U
            F1    = self.pax_will_to_pay_direct(lz_U,lamb[0],sigma[0],delta[0])
            F2    = self.pax_will_to_pay_direct(lz_U,lamb[1],sigma[1],delta[1])
            Flz_U = prob - c1 * F1 - c2 * F2
            talfa   = (Flz_L - Flz_U) / step
            delta_z = Flz_L / talfa
            lz      = lz_L + delta_z
            F1      = self.pax_will_to_pay_direct(lz,lamb[0],sigma[0],delta[0])
            F2      = self.pax_will_to_pay_direct(lz,lamb[1],sigma[1],delta[1])
            F3      = self.pax_will_to_pay_direct(lz,lamb[2],sigma[2],delta[2])
            Flz     = alpha[0] * (1-F1) + alpha[1] * (1-F2) + alpha[2] * (1-F3) - z
        return lz

    def fun_maximize_p1(self,p1,z,alpha,lamb,sigma,delta):
        """Objective function to determine optimum primary product price.
        Args:
            p1 (float):      price of the primary product (airfare)
            z (float):       probability of sale during a time period, parameter from (0,1)
            alpha (float):   alpha[i] - probability a customer belongs to group i, i=1,2,3
            lamb (float):    first parameter  of distribution describing PAX willingness to pay
            sigma (float):   second parameter of distribution describing PAX willingness to pay
            delta (float):   third parameter  of distribution describing PAX willingness to pay
        Returns:
            Fun (float):     value of function to be maximized (we return -Fun because we're using minimization alg.)
        """
        c1      = alpha[0] / (alpha[0] + alpha[1])
        c2      = alpha[1] / (alpha[0] + alpha[1])
        F1      = self.pax_will_to_pay_direct(p1,lamb[0],sigma[0],delta[0])
        F2      = self.pax_will_to_pay_direct(p1,lamb[1],sigma[1],delta[1])
        Fp1     = c1 * F1 + c2 * F2
        prob    = ( 1 - z - (alpha[0] + alpha[1]) * Fp1 ) / alpha[2]
        pr1     = self.pax_will_to_pay_inverse(prob,lamb[2],sigma[2],delta[2])
        q2_z_p1 = pr1 - p1
        pr2     = p1 + q2_z_p1
        prob2   = self.pax_will_to_pay_direct(pr2,lamb[1],sigma[1],delta[1])
        prob3   = self.pax_will_to_pay_direct(pr2,lamb[2],sigma[2],delta[2])
        Fun     = p1 + ( q2_z_p1 / z ) * ( alpha[1] * (1-prob2) + alpha[2] * (1-prob3) )
        return -Fun

    def calculate_q2_z(self,q1_z,z,alpha,lamb,sigma,delta):
        """Calculates price of the secondary product (ancillary).
        Args:
            q1_z (float):   price of the primary product (airfare)
            z (float):      probability of sale during a time period, parameter from (0,1)
            alpha (float):  alpha[i] - probability a customer belongs to group i, i=1,2,3
            lamb (float):   first parameter  of distribution describing PAX willingness to pay
            sigma (float):  second parameter of distribution describing PAX willingness to pay
            delta (float):  third parameter  of distribution describing PAX willingness to pay
        Returns:
            q2_z (float):   price of the secondary product (ancillary)
        """
        c1      = alpha[0] / (alpha[0] + alpha[1])
        c2      = alpha[1] / (alpha[0] + alpha[1])
        F1      = self.pax_will_to_pay_direct(q1_z,lamb[0],sigma[0],delta[0])
        F2      = self.pax_will_to_pay_direct(q1_z,lamb[1],sigma[1],delta[1])
        Fq1_z   = c1 * F1 + c2 * F2
        prob    = ( 1 - z - (alpha[0] + alpha[1]) * Fq1_z ) / alpha[2]
        pr1     = self.pax_will_to_pay_inverse(prob,lamb[2],sigma[2],delta[2])
        q2_z    = pr1 - q1_z
        return q2_z

    def calculate_pi_z(self,p1_z,p2_z,z,alpha,lamb,sigma,delta):
        """Calculates maximum expected revenue per customer sale.
        Args:
            p1_z (float):   price of the primary product (airfare)
            p2_z (float):   price of the secondary product (ancillary)
            z (float):      probability of sale during a time period, parameter from (0,1)
            alpha (float):  alpha[i] - probability a customer belongs to group i, i=1,2,3
            lamb (float):   first parameter  of distribution describing PAX willingness to pay
            sigma (float):  second parameter of distribution describing PAX willingness to pay
            delta (float):  third parameter  of distribution describing PAX willingness to pay
        Returns:
            pi_z (float):   maximum expected revenue per customer sale 
        """
        p       = p1_z + p2_z
        prob2   = self.pax_will_to_pay_direct(p,lamb[1],sigma[1],delta[1])
        prob3   = self.pax_will_to_pay_direct(p,lamb[2],sigma[2],delta[2])
        pi_z    = p1_z + ( p2_z / z ) * ( alpha[1] * (1-prob2) + alpha[2] * (1-prob3) )
        return pi_z
    
    def pax_will_to_pay_direct(self, x, lamb, sigma, delta):
        """Calculates the probability Prob that customer is willing to pay price <= x.
        Args:
            x (float):      price
            lamb (float):   first parameter  of distribution describing PAX willingness to pay
            sigma (float):  second parameter of distribution describing PAX willingness to pay
            delta (float):  third parameter  of distribution describing PAX willingness to pay
            dist (str):     probability distribution describing PAX willingness to pay
                dist = pax_wtp_dir_probit     PROBIT model used
                dist = pax_wtp_dir_logit      LOGIT model used
                dist = pax_wtp_dir_gen_logit  GENERALIZED LOGIT model used
        Returns:
            Prob (float):   probability that customer is willing to pay price <= x 
        """
        dist = self.dist_wtp_dir
        if dist is not None:
            return dist(x, lamb, sigma, delta)
    
    def pax_will_to_pay_inverse(self, Prob, lamb, sigma, delta):
        """Calculates the price x that corresponds to given probability Prob.
        Args:
            Prob (float):   probability that customer is willing to pay price <= x 
            lamb (float):   first parameter  of distribution describing PAX willingness to pay
            sigma (float):  second parameter of distribution describing PAX willingness to pay
            delta (float):  third parameter  of distribution describing PAX willingness to pay
            dist (str):     probability distribution describing PAX willingness to pay
                dist = pax_wtp_inv_probit     PROBIT model used
                dist = pax_wtp_inv_logit      LOGIT model used
                dist = pax_wtp_inv_gen_logit  GENERALIZED LOGIT model used
        Returns:
            x (float):      price
        """
        dist = self.dist_wtp_inv
        if dist is not None:
            return dist(Prob, lamb, sigma, delta)

    def pax_arrivals(self, n, mu_arr, si_arr):
        """Calculates the probability that the number of arriving customers is equal to n.
        Args:
            n (int):        n
            mu_arr (float): mean of distribution describing PAX arrivals
            si_arr (float): second parameter of distribution describing PAX arrivals
            dist_arr (str): probability distribution describing PAX arrivals
               dist_arr = pax_arrivals_poisson  POISSON distribution used
               dist_arr = pax_arrivals_normal   NORMAL distribution used
               dist_arr = pax_arrivals_fixed    FIXED NUMBER distribution used
        Returns:
            Pr_demand_eq_n (float): probability that the number of ariving PAX = n
        """
        dist = self.dist_arr
        if dist is not None:
            return dist(n, mu_arr, si_arr)

    def pmf_ht_x_z(self, Nmax, mu_arr, si_arr, z, x):
        """Calculates the value of probability mass function: ht(x|z) = Pr(Dt(z)=x). 
        Args:
            Nmax (int):     maximum number of arriving customers
            mu_arr (float): mean of distribution describing PAX arrivals
            si_arr (float): second parameter of distribution describing PAX arrivals
            dist_arr (str): probability distribution describing PAX arrivals
            dist_arr = pax_arrivals_poisson  POISSON distribution used
            dist_arr = pax_arrivals_normal   NORMAL distribution used
            dist_arr = pax_arrivals_fixed    FIXED NUMBER distribution used
            z (float):      probability of sale during a time period
            x (int):        we want to calculate probability that demand at period t = x, ht(x|z) = Pr(Dt(z)=x)
        Returns:
            ht_x_z (float): probability mass function value at x
        """
        ht_x_z = 0
        for n in range(x, Nmax):
            Pr_demand_eq_n = self.pax_arrivals(n, mu_arr, si_arr)
            ht_x_z = ht_x_z + binom(n, x) * z**x * (1-z)**(n-x) * Pr_demand_eq_n
        return ht_x_z   

    def calculate_e_min_dt(self, h_t_x_z, H_t_x_z, Cap):
        """Calculates the expected value of the demand.  
           Given the probability mass function and its cumulative distribution function, 
           calculates the expected value of the demand.
        Args:
            h_t_x_z (float):  probability mass function (vector), ht(x|z) = Pr(Dt(z)=x)
            H_t_x_z (float):  cumulative distribution function of h_t_x_z (vector)  
            Cap (int):        current value of capacity
        Returns:
            E_min_Dt (float): expected value of the demand E[min(Dt(z),Cap)]
        """
        E_min_Dt = 0
        for x in range(0, Cap):
            E_min_Dt = E_min_Dt + x * h_t_x_z[x] 
        E_min_Dt = E_min_Dt + Cap * ( 1 - H_t_x_z[Cap-1] )
        return E_min_Dt
    
    def plot_optimization_results(self,zz,step_t,alpha_t,lambda_t,sigma_t,delta_t,mu_arr_t,si_arr_t,Nmax_t,capacity_remaining,ValueFun_t_min_1):
        """Plots a graph showing how individual product prices evolve in time (in time periods)
        """
        ValFun  = np.zeros(self.npoints)
        p1_z    = np.zeros(self.npoints)
        p2_z    = np.zeros(self.npoints)
        for i in range(self.npoints):
            ValFun[i] = -self.fun_optimality_period_t(zz[i],step_t,alpha_t,lambda_t,sigma_t,delta_t,mu_arr_t,si_arr_t,Nmax_t,capacity_remaining,ValueFun_t_min_1)
            OptPrices = self.calculate_opt_prices(zz[i],step_t,alpha_t,lambda_t,sigma_t,delta_t)
            p1_z[i]   = OptPrices[0]
            p2_z[i]   = OptPrices[1]

        t      = np.zeros(2*self.n_periods)
        PriPrc = np.zeros(2*self.n_periods)
        AncPrc = np.zeros(2*self.n_periods)
        ProSal = np.zeros(2*self.n_periods)
        for j in range(self.n_periods):              # Loop over time periods
            t[2*j  ]  = j
            t[2*j+1]  = j+1
            PriPrc[2*j  ] = self.OptPrice[j,0]
            PriPrc[2*j+1] = self.OptPrice[j,0]
            AncPrc[2*j  ] = self.OptPrice[j,1]
            AncPrc[2*j+1] = self.OptPrice[j,1]
            ProSal[2*j  ] = self.OptPrice[j,3]
            ProSal[2*j+1] = self.OptPrice[j,3]

        plt.figure()
        plt.plot(-t, PriPrc, label='Primary Price', linewidth=2)
        plt.plot(-t, AncPrc, label='Ancillary Price', linewidth=2)
        plt.xlabel("Period Prior to Departure")
        plt.ylabel("Price")
        plt.title("Optimum Primary and Ancillary Prices")
        plt.legend()
        plt.show()

        plt.figure()
        plt.plot(-t, ProSal, label='Probability of Sale', linewidth=2)
        plt.xlabel("Period Prior to Departure")
        plt.ylabel("Probability of Sale")
        plt.title("Optimum Probability of Sale")
        plt.legend()
        plt.show()

        plt.figure()
        plt.plot(zz, p1_z, label='Primary Price', linewidth=2)
        plt.plot(zz, p2_z, label='Ancillary Price', linewidth=2)
        plt.xlabel("Probability of Sale, z")
        plt.ylabel("Price")
        plt.title("Conditional Prices Given Probability of Sale, final period")
        plt.legend()
        plt.show()

        plt.figure()
        plt.plot(zz, ValFun, label='Value Function', linewidth=2)
        plt.xlabel("Probability of Sale, z")
        plt.ylabel("Price")
        plt.title("Conditional Expected Value Given Probability of Sale, final period")
        plt.legend()
        plt.show()