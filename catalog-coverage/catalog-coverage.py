def catalog_coverage(recommendations, n_items):
    """
    Compute the catalog coverage of a recommender system.
    """
    # Write code here
    travel = []
    for recommendation in recommendations:
        for item in recommendation:
            if item not in travel:
                travel.append(item)

    return len(travel) / n_items