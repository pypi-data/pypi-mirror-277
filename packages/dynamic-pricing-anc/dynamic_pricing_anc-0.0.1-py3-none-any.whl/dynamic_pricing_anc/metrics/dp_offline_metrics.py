import numpy as np

def dp_offline_metrics(y, OffPrice, OptPrice):
    """Calculates set of five offline metrics measuring the quality of the fitted pricing models.
    Args:
        y (float):        y[i] = 1 booked session, y[i] = 0 non-booked session
        OffPrice (float): OffPrice[i] - price offered to the customer
        OptPrice (float): OptPrice[i] - calculated optimum price
    Returns:
        PDR (float):      Price Decrease Recall
        PIR (float):      Price Increase Recall
        PDP (float):      Price Decrease Precision
        PIP (float):      Price Increase Precision
        BR (float):       Booking Regret
    """
    OffPricePos  = OffPrice[ y > 0 ]
    OptPricePos  = OptPrice[ y > 0 ]
    OffPriceNeg  = OffPrice[ y == 0 ]
    OptPriceNeg  = OptPrice[ y == 0 ]
    # PDR - Price Decrease Recall: among all non-booked sessions, the percentage of 
    #       suggestions that are lower than offered prices (AmountReport).
    PDR = len( OptPriceNeg[ OptPriceNeg <  OffPriceNeg ] ) / len(OptPriceNeg)
    # PIR - Price Increase Recall: among all booked sessions, the percentage of
    #       suggestions that are higher than or equal to offered prices (AmountReport).
    PIR = len( OptPricePos[ OptPricePos >= OffPricePos ] ) / len(OptPricePos)

    # BR  - Booking Regret
    BR  = ( OffPrice - OptPrice ) / OffPrice
    BR[ BR < 0 ] = 0
    BR_median = np.median(BR)
    BR_mean   = np.mean(BR)

    yBelow = y[ OptPrice <  OffPrice ]
    yAbove = y[ OptPrice >= OffPrice ]
    # PDP - Price Decrease Precision: among all cases where OptPrice <  AmountReport, 
    #       the percentage of sessions that are non-booked.
    PDP = len( yBelow[ yBelow == 0 ] ) / len(yBelow)

        # PIP - Price Increase Precision: among all cases where OptPrice >= AmountReport,
    #       the percentage of sessions that are booked.
    PIP = len( yAbove[ yAbove == 1 ] ) / len(yAbove)
    
    OffMetrics = np.array([PDR, PIR, PDP, PIP, BR_median, BR_mean])
    
    return OffMetrics