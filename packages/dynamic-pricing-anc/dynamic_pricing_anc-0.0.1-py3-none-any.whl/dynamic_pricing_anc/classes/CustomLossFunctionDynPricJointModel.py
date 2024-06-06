import numpy as np
import xgboost as xgb

class CustomLossFunctionDynPricJointModel:
    """ Customized Loss Function"""
    def __init__(self, y, c):
        """
        y (float):      y[i] = 1 booked session, y[i] = 0 non-booked session
        c (float):      two constants to be learned via hyper-parameter tuning, 0 < c[0] < 1, 1 < c[1]
        """
        self.y = y
        self.c = c
    
    def strategy_grad_hess(self, predt: np.ndarray, dtrain: xgb.DMatrix):
        ''' Calculate Gradient and Hessian of the Customized Loss Function.
        predt (float):  predt[i] - predicted price for i-th customer
        P (float):      P[i] - price offered to the i-th customer
        '''
        P = dtrain.get_label()
        ###########################################
        lower_bound = self.y * P + ( 1 - self.y ) * self.c[0] * P
        upper_bound = ( 1 - self.y ) * P + self.y * self.c[1] * P
        bracket_lb = lower_bound - predt
        bracket_ub = predt - upper_bound 
        bracket_lb[ bracket_lb < 0 ] = 0
        bracket_ub[ bracket_ub < 0 ] = 0
        grad = -bracket_lb + bracket_ub
        hess = np.ones(len(grad))
        return grad, hess

    def strategy_loss(self, predt: np.ndarray, dtrain: xgb.DMatrix):
        ''' Calculate Customized Loss Function Value
        predt (float):  predt[i] - predicted price for i-th customer
        P (float):      P[i] - price offered to the i-th customer
        '''
        P = dtrain.get_label()
        ###################################
        lower_bound = self.y * P + ( 1 - self.y ) * self.c[0] * P
        upper_bound = ( 1 - self.y ) * P + self.y * self.c[1] * P
        bracket_lb = lower_bound - predt
        bracket_ub = predt - upper_bound
        bracket_lb[ bracket_lb < 0 ] = 0
        bracket_ub[ bracket_ub < 0 ] = 0
        Loss = np.sum( bracket_lb + bracket_ub )
        return 'PyStrategyLoss', float(Loss)