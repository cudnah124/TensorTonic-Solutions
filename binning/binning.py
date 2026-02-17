def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    # Write code here
    min_values = min(values)
    max_values = max(values)

    if min_values == max_values:
        return [0] * len(values)
        
    w = (max_values - min_values) / num_bins
    
    return [min(int((i - min_values) / w), num_bins - 1) for i in values]