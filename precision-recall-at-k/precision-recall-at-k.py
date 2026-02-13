def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    res = [0, 0]

    for i in recommended[:k]:
        if i in relevant:
            res[0] += 1
            res[1] += 1
    
    return [res[0] / len(recommended[:k]), res[1] / len(relevant)]