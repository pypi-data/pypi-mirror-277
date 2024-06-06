import numpy as np
import pandas as pd
from scipy import optimize
from matplotlib import pyplot as plt

class MultipleAncillaryProductsNonlinearDemand:
    """This class considers single leg flight with a primary product (seats) and ancillary products. The capacity of 
    primary product is fixed, capacities of individual ancillary products can also be limited (e.g. better seats). 
    Total revenue is maximized by dynamically setting prices on both the primary product and the ancillary services. 
    ___________________________________________________________________________________________________________________
    We consider a set of distinct product combinations or product mixes, each product mix has a separate booking 
    probability model and demand forecast. This allows individuals to buy different product mixes based on the price. 
    For some prices, an individual may buy mix 1, for others mix 2, etc. The booking period of the flight is divided 
    into time periods. The booking probability models for individual product mixes and time periods are nonlinear, 
    they are modelled by logistic (logit) model.
    ___________________________________________________________________________________________________________________
    John G. Wilson. 2016. Jointly Optimising Prices for Primary and Multiple Ancillary Products.
    ___________________________________________________________________________________________________________________
    Args:
        n_periods (int):         number of time periods
        n_products (int):        number of Products
        n_product_mixes (int):   number of product mixes
        product_names (str):     names of individual Products
    """
    def __init__(self, n_periods, n_products, n_product_mixes, product_names):
        self.n_periods = n_periods
        self.n_products = n_products
        self.n_product_mixes = n_product_mixes
        self.product_names = product_names

    def fit(self, product_capacity, period_forecast, demand_constant, demand_sensitivity, incidence_matrix):
        """Calculates optimum prices for all products. The optimum price for a product mix containing
        more products is then given by the sumation of individual optimum product prices. Also
        calculates three dataframes containing summary results.
        Args:
            product_capacity (float):   capacities of individual Products
            period_forecast (float):    numbers of passengers in individual time periods (forecast)
            demand_constant (float):    matrix containing constant terms of purchase probability models
                                        demand_constant[t,m] - constant term of a purchase prob. model for period t and product mix m
            demand_sensitivity (float): matrix containing sensitivities of purchase probability models
                                        demand_sensitivity[t,m] - sensitivity of a purchase prob. model for period t and product mix m
            incidence_matrix (float):   incidence matrix: rows - product mixes, columns - Products
                                        incidence matrix[m,p]  = 1 if product mix m contains product p, = 0 otherwise
        Returns:
            opt_prices (float):         opt_prices[p] - calculated optimum price for the product p
        """
        self.product_capacity = product_capacity
        self.period_forecast = period_forecast
        self.demand_constant = demand_constant
        self.demand_sensitivity = demand_sensitivity
        self.incidence_matrix = incidence_matrix

        # Definition of optimization problem:
        cons = {'type':'ineq',
        'fun' : self.demand,
        'jac' : self.der_demand}
        opt = {'disp':False}

        # Starting point
        self.x0 = self.starting_point_for_optimization()

        # bounds: all prices must be positive (lower bound), no upper bound
        bnds = tuple((0, None) for _ in range(self.n_periods*self.n_products))

        # Calling the optimization solver:
        res_cons = optimize.minimize(self.revenue, self.x0, jac=self.der_revenue, bounds=bnds, constraints=cons, method='SLSQP', options=opt)
        self.opt_prices = res_cons['x']

        TotDemandProducts, OptSolutionProducts, OptSolutionProductMixes, total_revenue = self.postprocessing()

        return self.opt_prices, total_revenue, OptSolutionProducts, OptSolutionProductMixes, TotDemandProducts
    
    def revenue(self, x):
        """Calculates value of the revenue function to be maximized.
        Args:
            x (float):        current prices for individual products and time periods 
        Returns:
            Revenue (float):  total revenue per flight given the prices x, we return (-Revenue) because the solver is minimizing
        """
        # revenue(x, INC, Constant, Sensitivity, Q):
        Revenue = 0

        for t in range(self.n_periods):             # Loop over time periods

            # product prices for period t
            price_t = x[ t*self.n_products : (t+1)*self.n_products ]

            for m in range(self.n_product_mixes):   # loop over product mixes

                # price of product mix m in time period t
                price_m_t = np.dot( self.incidence_matrix[m,], price_t)
                # demand for product mix m in time period t
                exp_m_t = self.demand_constant[t,m] + self.demand_sensitivity[t,m] * price_m_t
                demand_m_t = np.exp(exp_m_t) / ( 1 + np.exp(exp_m_t) )
                Revenue = Revenue + price_m_t * demand_m_t * self.period_forecast[t]

        return -Revenue
    
    def der_revenue(self, x):
        """Calculates gradient of the revenue function.
        Args:
            x (float):         current prices for individual products and time periods 
        Returns:
            Gradient (float):  gradient of the revenue function with respect to the prices x
        """
        Gradient = np.zeros(  self.n_periods * self.n_products )

        for t in range(self.n_periods):                # Loop over time periods

            # product prices for period t
            price_t = x[ t*self.n_products : (t+1)*self.n_products ]

            for m in range(self.n_product_mixes):      # loop over product mixes

                # price of product mix m in time period t
                price_m_t = np.dot( self.incidence_matrix[m,], price_t)
                # demand for product mix m in time period t
                exp_m_t = self.demand_constant[t,m] + self.demand_sensitivity[t,m] * price_m_t
                denom_m_t = 1 + np.exp(-exp_m_t)

                for p in range(self.n_products):       # loop over products
                    u      = price_m_t * self.period_forecast[t]
                    u_diff = self.incidence_matrix[m,p] * self.period_forecast[t]
                    v      = denom_m_t
                    v_diff = - self.demand_sensitivity[t,m] * self.incidence_matrix[m,p] * np.exp(-exp_m_t)
                    Gradient[ t * self.n_products + p ] = Gradient[ t * self.n_products + p ] + ( u_diff * v - u * v_diff ) / v**2

        return -Gradient
    
    def demand(self, x):
        """Calculates values of individual product capacity constraints (product capacities must not be exceeded). 
        Nonlinear inequality constraints have to be in the form f(x) >= 0. For individual products p = 1,...,nprod, 
        we thus have: Cap[p] - Demand[p] >= 0.
        Args:
            x (float):         vector of current prices for individual products and time periods 
        Returns:
            Cap_Cons (float):  vector containing values of individual product capacity constraints given the prices x
        """
        Demand  = np.zeros( self.n_products )       # Demand for individual products as a function of x

        for t in range(self.n_periods):             # loop over time periods

            # product prices for period t
            price_t = x[ t*self.n_products : (t+1)*self.n_products ]

            for m in range(self.n_product_mixes):   # loop over product mixes

                # price of product mix m in time period t
                price_m_t = np.dot( self.incidence_matrix[m,], price_t)
                # demand for product mix m in time period t
                exp_m_t = self.demand_constant[t,m] + self.demand_sensitivity[t,m] * price_m_t
                demand_m_t = np.exp(exp_m_t) / ( 1 + np.exp(exp_m_t) )

                for p in range(self.n_products):    # loop over products
                    Demand[p] = Demand[p] + self.incidence_matrix[m,p] * demand_m_t * self.period_forecast[t]

        Cap_Cons = self.product_capacity - Demand

        return Cap_Cons
    
    def der_demand(self, x):
        """Calculates gradients of individual product capacity constraints (product capacities must not be exceeded).
        Nonlinear inequality constraints have to be in the form f(x) >= 0. For individual products p = 1,...,nprod,
        we thus have: Cap[p] - Demand[p] >= 0.
        Args:
            x (float):        current prices for individual products and time periods 
        Returns:
            Gradient (float): matrix containing gradients of individual product capacity constraints given the prices x, 
                              Gradient[p,] - gradient of p-th product capacity constraint
        """
        Gradient = np.zeros(( self.n_products, self.n_periods * self.n_products ))

        for t in range(self.n_periods):                # loop over time periods

            # product prices for period t
            price_t = x[ t*self.n_products : (t+1)*self.n_products ]

            for m in range(self.n_product_mixes):      # loop over product mixes

                # price of product mix m in time period t
                price_m_t = np.dot( self.incidence_matrix[m,], price_t)
                # demand for product mix m in time period t
                exp_m_t = self.demand_constant[t,m] + self.demand_sensitivity[t,m] * price_m_t
                denom_m_t = 1 + np.exp(-exp_m_t)

                for p in range(self.n_products):       # loop over products
                    u      = self.incidence_matrix[m,p] * self.period_forecast[t]
                    u_diff = 0
                    v      = denom_m_t
                    v_diff = - self.demand_sensitivity[t,m] * self.incidence_matrix[m,p] * np.exp(-exp_m_t)
                    Gradient[ p, t * self.n_products + p ] = Gradient[ p, t * self.n_products + p ] + ( u_diff * v - u * v_diff ) / v**2

        return -Gradient
    
    def starting_point_for_optimization(self):
        """Calculates starting point for the nonlinear optimization. Starting point must be feasible.
        In other words, capacity constaints have to be satisfied cap_constr >= 0.
        Args:

        Returns:
            start_point (float):  vector containing starting point for nonlinear optimization
        """
        start_point = np.ones(self.n_periods*self.n_products)
        cap_constr = self.demand(start_point)
        while np.min(cap_constr) <= 0:
            start_point = start_point + 1
            cap_constr = self.demand(self, start_point)

        return start_point
    
    def postprocessing(self):
        """Calculates three dataframes containing summary results and also total revenue.
        Args:

        Returns:
            TotDemandProducts        dataframe showing total product demand and available capacity
            OptSolutionProducts      dataframe containing optimum prices for individual products at individual time periods
            OptSolutionProductMixes  dataframe containing opt. prices, demands and revenues for ind. product mixes at ind. time periods
            total_revenue (float):   total revenue per flight
        """
        OptDemand      = np.zeros(  self.n_periods * self.n_product_mixes )
        OptRevenue     = np.zeros(  self.n_periods * self.n_product_mixes )
        self.OptMixPrice    = np.zeros(  self.n_periods * self.n_product_mixes )
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
                exp_m_t = self.demand_constant[t,p] + self.demand_sensitivity[t,p] * PeriodMixPrices[p]
                OptDemand[ t * self.n_product_mixes + p ]  = self.period_forecast[t] * ( np.exp(exp_m_t) / ( 1 + np.exp(exp_m_t) ) )
                OptRevenue[ t * self.n_product_mixes + p ] = OptDemand[ t * self.n_product_mixes + p ] * PeriodMixPrices[p]
                self.OptMixPrice[ t * self.n_product_mixes + p ] = PeriodMixPrices[p]
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

        total_revenue  = np.sum(OptRevenue)
        ProductDemand  = -(self.demand(self.opt_prices) - self.product_capacity)

        TimePeriodMix  = TimePeriodMix.astype(int)
        TimePeriodProd = TimePeriodProd.astype(int)
        ProductMix     = ProductMix.astype(int)
        Product        = Product.astype(int)
        Prod           = np.linspace(1, self.n_products, num=self.n_products)
        Prod           = Prod.astype(int)

        OptPric        = np.around(self.opt_prices, decimals=2)
        ProductDemand  = np.around(ProductDemand, decimals=2)
        self.OptMixPrice    = np.around(self.OptMixPrice, decimals=2)
        OptDemand      = np.around(OptDemand, decimals=2)
        OptRevenue     = np.around(OptRevenue, decimals=2)

        TotDemandProducts = pd.DataFrame({'Product':Prod,'ProductName':self.product_names,'ProductDemand':ProductDemand,'product_capacity':self.product_capacity})
        OptSolutionProducts = pd.DataFrame({'TimePeriod':TimePeriodProd,'Product':Product,'ProductName':ProductNames,'OptimumPrice':OptPric})
        OptSolutionProductMixes = pd.DataFrame({'TimePeriod':TimePeriodMix,'ProductMix':ProductMix,'ProductsInTheMix':ProdMixNames,'OptMixPrice':self.OptMixPrice,'OptimumDemand':OptDemand,'OptimumRevenue':OptRevenue})

        return TotDemandProducts, OptSolutionProducts, OptSolutionProductMixes, total_revenue
    
    def plot_optimum_prices(self):
        """Plots a graph showing how individual product prices evolve in time (in time periods).
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
        """Plots estimated booking probability models for individual products.
        """
        npoints = 50
        for m in range(self.n_product_mixes):        # Loop over product mixes
            u = list( range(m, self.n_periods * self.n_product_mixes + m, self.n_product_mixes) )
            max_plt_price = 2 * max( self.OptMixPrice[u] )
            price_mix = np.linspace(0.0, max_plt_price, num=npoints)
            plt.figure()
            for t in range(self.n_periods):          # Loop over time periods
                deman_mix = np.zeros( npoints )
                for i in range(npoints):
                    # demand for product mix m in time period t
                    exp_m_t = self.demand_constant[t,m] + self.demand_sensitivity[t,m] * price_mix[i]
                    deman_mix[i] = np.exp(exp_m_t) / ( 1 + np.exp(exp_m_t) )  
                plt_label = "time period " + str(t)
                plt.plot(price_mix, deman_mix, label=plt_label, linewidth=2)
            plt_title = "Booking Probability Model: " + self.ProdMixName[m]
            plt.xlabel("Price")
            plt.ylabel("Purchase Probability")
            plt.title(plt_title)
            plt.legend()
            plt.show()
