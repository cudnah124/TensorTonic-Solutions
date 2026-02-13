def hit_rate_at_k(recommendations, ground_truth, k):
    """
    Compute the hit rate at K.
    """
    # Write code here
    hit = 0

    for rec, truth in zip(recommendations, ground_truth):
        if truth[0] in rec[:k]:
            hit += 1

    return hit / len(ground_truth)