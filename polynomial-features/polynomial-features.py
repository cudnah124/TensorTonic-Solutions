def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    # Write code here
    poly = []
    for value in values:
      ap = []
      for i in range(degree + 1):
        ap.append(value ** i)
      poly.append(ap)

    return poly