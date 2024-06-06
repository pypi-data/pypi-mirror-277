import numpy as np

def calculate_offered_price(TreatmentOrdinal, PriceMapping):
    """Calculates base price multipliers for individual booking sessions
    Args:
        TreatmentOrdinal (int):  TreatmentOrdinal[i] - value of treatment ordinal for i-th booking session
        PriceMapping (float):    PriceMapping[i] - price multiplier corresponding to the TreatmentOrdinal equal to i
                                 TreatmentOrdinal =   0     1     2     3    4
                             PriceMapping = np.array([1.0, 0.95, 1.05, 1.1, 1.12])
    Returns:
        OfferedPrice (float):    OfferedPrice[i] - price multiplier which was offered in i-th booking session
    """
    n_data = len(TreatmentOrdinal)
    OfferedPrice = np.zeros(n_data)
    for i in range(n_data):
        OfferedPrice[i] = PriceMapping[ TreatmentOrdinal[i] ]
    return OfferedPrice

def calculate_opt_price(PredictedPrice, OfferedPrice, TreatmentOrdinal, PriceMapping, Price):
    """Calculate discrete optimum base price multipliers (one of predefined price multipliers which is closest to the continuous optimum price)
    Args:
        PredictedPrice (float):  PredictedPrice[i] - estimated true continuous optimum price for i-th booking session
        OfferedPrice (float):    OfferedPrice[i] - true price which was offered in i-th booking session
        TreatmentOrdinal (int):  TreatmentOrdinal[i] - value of treatment ordinal for i-th booking session
        PriceMapping (float):    PriceMapping[i] - price multiplier corresponding to the TreatmentOrdinal equal to i
                                 TreatmentOrdinal =   0     1     2     3    4
                             PriceMapping = np.array([1.0, 0.95, 1.05, 1.1, 1.12])
        Price (float):           PriceMapping values sorted in ascending order
                                    Price = np.array([0.95, 1.0, 1.05, 1.1, 1.12])
    Returns:
        OptPrice (float):        OptPrice[i] - price multiplier which is closest to the continuous optimum price for i-th booking session
    """
    n_data = len(PredictedPrice)
    OptPrice = np.zeros(n_data)
    for i in range(n_data):
        BasePrice = OfferedPrice[i] / PriceMapping[ TreatmentOrdinal[i] ]
        istar = np.argmin( ( BasePrice * Price - PredictedPrice[i] )**2 )
        OptPrice[i] = Price[ istar ]
    return OptPrice

def calculate_uplift(TreatmentOrdinal, OfferedPrice, anc_rev, OptPrice, PriceMapping, Price):
    """Calculates four metrics.
    Args:
        TreatmentOrdinal (int):   TreatmentOrdinal[i] - treatment offered to the customer
        OfferedPrice (float):     OfferedPrice[i] - price offered to the customer
        OptPrice (float):         OptPrice[i] - predicted optimum price for i-th customer
        PriceMapping (float):     PriceMapping[i] - price multiplier corresponding to the TreatmentOrdinal equal to i
        Price (float):            PriceMapping values sorted in ascending order
    Returns:
        mean_anc_rev (float):     mean ancillary revenue
        uplift_metric (float):    uplift metric
        perc_opt_eq_off (float):  percentage of data points for which OfferedPrice == OptPrice
        uplift (float):           uplift
    """
    # Calculate discrete offered price multipliers (base price multipliers)
    OfferPrice = calculate_offered_price(TreatmentOrdinal, PriceMapping)

    # Calculate discrete optimum base price multipliers (one of predefined price multipliers which is closest to the continuous optimum price)
    opt_price = calculate_opt_price(OptPrice, OfferedPrice, TreatmentOrdinal, PriceMapping, Price)

    # Calculate mean ancillary revenue, uplift metric, percentage of data points for which OfferedPrice == OptPrice, uplift
    mean_anc_rev  = np.mean(anc_rev)
    uplift_metric = np.mean( anc_rev[ OfferPrice == opt_price ] )
    perc_opt_eq_off = np.sum( OfferPrice == opt_price ) / len(OfferedPrice)
    uplift = ( uplift_metric - mean_anc_rev ) / mean_anc_rev
    
    return mean_anc_rev, uplift_metric, perc_opt_eq_off, uplift