def hit_rate_at_k(recommendations, ground_truth, k):
    """
    Compute the hit rate at K.
    """
    # Write code here
    hit = 0
    travel = []
    for truth in ground_truth:
        for recommendation in recommendations:
            if truth[0] in recommendation[:k] and truth[0] not in travel:
                hit += 1
                travel.append(truth[0])
    
    return hit / len(ground_truth)