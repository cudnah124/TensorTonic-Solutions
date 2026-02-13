def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    hit = 0

    for i in recommended[:k]:
        if i in relevant:
            hit += 1
    
    return [hit / len(recommended[:k]), hit / len(relevant)]