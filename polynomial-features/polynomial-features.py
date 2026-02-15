def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    # Write code here
    poly = []
    for v in values:
        row = [1]
        cur = 1
        for _ in range(degree):
            cur *= v
            row.append(cur)
        poly.append(row)
    return poly