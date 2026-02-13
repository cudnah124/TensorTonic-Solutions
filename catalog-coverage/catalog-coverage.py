def catalog_coverage(recommendations, n_items):
    """
    Compute the catalog coverage of a recommender system.
    """
    # Write code here
    travel = set()

    for recommendation in recommendations:
        for item in recommendation:
            travel.add(item)

    return len(travel) / n_items