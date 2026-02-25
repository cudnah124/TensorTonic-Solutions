def discount_returns(rewards, gamma):
    """
    Compute the discounted return at every timestep.
    """
    # Write code here

    G = rewards.copy()

    for i in range(len(G) - 2, -1, -1):
        G[i] = rewards[i] + gamma * G[i + 1]

    return G
    