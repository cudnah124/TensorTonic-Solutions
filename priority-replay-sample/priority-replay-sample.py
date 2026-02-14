def priority_replay_sample(priorities, alpha, beta):
    """
    Compute sampling probabilities and importance sampling weights for PER.
    """
    # Write code
    # Step 1: scale priorities
    scaled = [p ** alpha for p in priorities]
    total = sum(scaled)

    # Step 2: sampling probabilities
    probs = [s / total for s in scaled]

    # Step 3: importance weights
    N = len(priorities)
    weights = [((1 / N) * (1 / p)) ** beta for p in probs]

    # Step 4: normalize weights
    max_w = max(weights)
    weights = [w / max_w for w in weights]

    return [probs, weights] 
