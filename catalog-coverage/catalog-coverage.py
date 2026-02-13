def catalog_coverage(recommendations, n_items):
    """
    Compute the catalog coverage of a recommender system.
    """
    # Write code here
    travel = {item for rec in recommendations for item in rec}
    return len(travel) / n_items