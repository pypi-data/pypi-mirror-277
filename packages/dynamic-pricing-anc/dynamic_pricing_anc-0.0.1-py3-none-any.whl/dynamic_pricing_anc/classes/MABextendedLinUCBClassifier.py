import numpy as np
import pandas as pd

from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils.validation import check_X_y, check_array, check_is_fitted
from sklearn.utils.multiclass import unique_labels
from sklearn import metrics

from numpy.linalg import inv
from scipy import optimize
from matplotlib import pyplot as plt

class MABextendedLinUCBClassifier(BaseEstimator, ClassifierMixin):
    """This class does dynamic pricing of airline ancillaries. A contextual multi-armed bandit approach is used, 
    in particular linUCB algorithm. A strategy for multi-armed bandit policies called extended play is implemented. 
    This strategy leverages on the assumption of monotonicity in willingness to pay by customers allowing the policy 
    to play more than one arm per round. Each arm of a bandit represents one treatment and arms/treatments are sorted 
    in ascending order. Consider having chosen arm a*. In the case of having a purchase of arm a*, we also play 
    all arms a ≤ a* and record them as purchases as well by our monotonicity assumption. Similarly, if we do not 
    have a purchase then we play all arms a ≥ a* and record them as non-purchases.
    ___________________________________________________________________________________________________________________
    Lihong Li, Wei Chu, John Langford, and Robert E. Schapire. 2012. A Contextual-Bandit Approach to Personalized 
    News Article Recommendation.
    ___________________________________________________________________________________________________________________
    Args:
        alpha        - constant of the LinUCB algorithm
        n_predictors - number of predictors
        n_arms       - number of arms/treatments
    """
    def __init__(self, alpha, n_predictors, n_arms):
        self.alpha = alpha
        self.n_predictors = n_predictors
        self.n_arms = n_arms
        
        # B matrix containing ridge regression vectors of disjoint linear models - each arm initialized with zero vector
        self.B = np.zeros(( self.n_predictors, self.n_arms ))
        # A matrix containing ridge regression matrices of individual arms - each arm initialized with identity matrix
        self.A = np.zeros(( self.n_predictors*self.n_arms, self.n_predictors ))
        for a in range(self.n_arms):
            self.A[ a*self.n_predictors : (a+1)*self.n_predictors , : ] = np.identity(self.n_predictors)

    def fit(self, X, y, IsSell):
        """Fits ridge regression matrix and vector for each arm of the bandit
        Args:
           X (float):     matrix the columns of which represent individual predictor variables
                          X[t,:] - predictors for the t-th customer
                          X[t,:] = [ f_1, f_2,…, f_N, AP0, AP1,..., AP_n_arms-1 ]
                          f_i - standard i-th feature, i=1,...,N (TotalFare, DaysBeforeDeparture etc)
                          AP_a - ancillary price for arm/treatment a, a=0,...,n_arms-1
           y (int):       vector, y[t] = a, customer was offered arm a, a = 0, 1,..., n_arms-1
                          where AP_0 < AP_1 ... < AP_n_arms-1
           IsSell (int):  vector, IsSell[t] = 1 booked session, IsSell[t] = 0 non-booked session              
        Returns:      
           self.A (float):  matrix containing ridge regression matrices of individual arms
           self.B (float):  matrix containing ridge regression vectors of individual arms 
        """
        # Check that X and y have correct shape
        X, y = check_X_y(X, y)
        # Store the classes seen during fit
        #self.classes_ = unique_labels(y)
        
        #####################################################################################################################
        # number of time periods (=number of data rows, =number of customer transactions)
        n_period = X.shape[0]
            
        for t in range(n_period):       # loop over time periods/customer transactions
            # Using t-th row of X matrix, construct Predictors matrix characterizing period t
            # a-th column: Predictors[:,a] = x_a = [1, f_1, f_2,…, f_N, AP_a ]
            Predictors = np.zeros(( self.n_predictors, self.n_arms ))
            Predictors[ 0 , : ] = np.ones(self.n_arms)
            for a in range(self.n_arms):
                Predictors[ 1 : self.n_predictors-1 , a ] = X[ t, 0 : self.n_predictors-2 ]  
            Predictors[ self.n_predictors-1 , : ] = X[ t, self.n_predictors-2 : self.n_predictors+self.n_arms-1 ]
    
            # Apply LinUCB method and calculate optimum arm
            opt_arm = self.LinUCB(Predictors)
    
            # If optimum arm is equal to randomly assigned arm, update problem matrices
            if opt_arm == y[t]:
                # Identify arms that will be played 
                if IsSell[t] > 0:
                    start_arm = 0
                    end_arm   = opt_arm+1
                else:
                    start_arm = opt_arm
                    end_arm   = self.n_arms
                # calculate rewards for individual arms
                reward = Predictors[ self.n_predictors-1 , : ] * IsSell[t]
                # Play the arms - update regression matrices and vectors
                self.update_multiple_arms(Predictors, reward, start_arm, end_arm)
        #####################################################################################################################

        self.X_ = X
        self.y_ = y
        # Return the classifier
        return self

    def predict(self, X):
        """Calculates optimum arms/treatments for all customers/data rows in the dataset.
        Args:
           X (float):     matrix the columns of which represent individual predictor variables
                          X[t,:] - predictors for the t-th customer
                          X[t,:] = [ f_1, f_2,…, f_N, AP0, AP1,..., AP_n_arms-1 ]
                          f_i - standard i-th feature, i=1,...,N (TotalFare, DaysBeforeDeparture etc)
                          AP_a - ancillary price for arm/treatment a, a=0,...,n_arms-1        
        Returns:      
           outcome (float):  vector, outcome[t] = a, a is optimum arm/treatment for customer, a = 0, 1,..., n_arms-1          
        """

        # Check if fit has been called
        check_is_fitted(self)

        # Input validation
        X = check_array(X)
        
        #####################################################################################################################
        n_period = X.shape[0] 
        outcome = np.zeros(n_period)
        for t in range(n_period):       # loop over time periods/customer transactions
            # Using t-th row of X matrix, construct Predictors matrix characterizing period t
            # a-th column: Predictors[:,a] = x_a = [1, f_1, f_2,…, f_N, AP_a ]
            Predictors = np.zeros(( self.n_predictors, self.n_arms ))
            Predictors[ 0 , : ] = np.ones(self.n_arms)
            for a in range(self.n_arms):
                Predictors[ 1 : self.n_predictors-1 , a ] = X[ t, 0 : self.n_predictors-2 ]  
            Predictors[ self.n_predictors-1 , : ] = X[ t, self.n_predictors-2 : self.n_predictors+self.n_arms-1 ]
    
            # Apply LinUCB method and calculate optimum arm
            outcome[t] = self.LinUCB(Predictors)
        #####################################################################################################################

        return outcome

    def LinUCB(self, Predictors):
        """Calculates optimum arm/treatment using the algorithm LinUCB with disjoint linear models
        Args:
            Predictors - matrix containing predictor vectors of individual arms [n_predictors, n_arms]
              a-th column: Predictors[:,a] = x_a = [1, f_1, f_2,…, f_N, AP_a ]
              f_i  - standard i-th feature, i=1,...,N (TotalFare, DaysBeforeDeparture etc)
              AP_a - ancillary price for arm/treatment a, a=0,...,n_arms-1   
        Returns:
            opt_arm - optimum arm/treatment, a=0,...,n_arms-1
        """
        price = np.zeros(self.n_arms)
        for a in range(self.n_arms):
            # ridge regression matrix of arm a
            A_arm = self.A[ a*self.n_predictors : (a+1)*self.n_predictors , : ]
            # invert the matrix of arm a
            A_arm_inv = inv(A_arm)
            # estimate new model parameters theta for arm a using ridge regression 
            theta = np.dot( A_arm_inv, self.B[:,a] )
            # calculate expected payoff of arm a
            price[a] = np.dot( theta.T, Predictors[:,a] ) + self.alpha * np.sqrt( self.xt_A_x( Predictors[:,a], A_arm_inv ) )
        
        # calculate optimum arm - the arm withthe highest expected payoff
        opt_arm = np.argmax(price)
        return opt_arm

    def update_multiple_arms(self, Predictors, reward, start_arm, end_arm):
        """Updates ridge regression matrices and vectors for multiple arms
        Args:
            Predictors - matrix containing predictor vectors of individual arms [n_predictors, n_arms]
              a-th column: Predictors[:,a] = x_a = [1, f_1, f_2,…, f_N, AP_a ]
              f_i  - standard i-th feature, i=1,...,N (TotalFare, DaysBeforeDeparture etc)
              AP_a - ancillary price for arm/treatment a, a=0,...,n_arms-1   
            reward     - vector containing rewards of individual arms, a=0,...,n_arms-1
            start_arm  - number of the lowest arm to be updated
            end_arm    - number of the highest arm to be updated
        """
        for a in range(start_arm, end_arm):
            # update ridge regression matrix for arm a
            self.A[ a*self.n_predictors : (a+1)*self.n_predictors , : ] = self.A[ a*self.n_predictors : (a+1)*self.n_predictors , : ] + self.x_xt( Predictors[:,a] )
            # update ridge regression vector for arm a
            self.B[:,a] = self.B[:,a] + reward[a] * Predictors[:,a]
    
    def xt_A_x(self, x, A):
        """Calculates product x.T * A * x
        Args:
            x - vector
            A - matrix 
        Returns:
            product x.T * A * x
        """
        return np.dot( x.T, np.dot( A, x) )

    def x_xt(self, x):
        """Calculates matrix A, A = x * x.T
        Args:
            x - vector
        Returns:
            A - matrix
        """
        N = len(x)
        A = np.zeros(( N, N ))
        for i in range(N):         
            for j in range(N):  
                A[i,j] = x[i] * x[j]
        return A