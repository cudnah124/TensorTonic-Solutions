def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    # Write code here
    x = sum(a * b for a, b in zip(x1, x2))

    y = math.sqrt(sum(a * a for a in x1)) * math.sqrt(sum(b * b for b in x2))

    cos = x / y
    
    return 1 - cos if label == 1 else max(0, cos - margin)