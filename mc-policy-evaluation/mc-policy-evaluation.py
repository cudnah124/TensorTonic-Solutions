import numpy as np

def mc_policy_evaluation(episodes, gamma, n_states):
    """
    Returns: V (NumPy array of shape (n_states,))
    """
    # Write code here
    V = np.zeros(n_states)
    returns = [[] for _ in range(n_states)]

    for ep in episodes:
        T = len(ep)
        
        G = np.zeros(T)
        
        
        running = 0
        for t in reversed(range(T)):
            s, r = ep[t]
            running = r + gamma * running
            G[t] = running

        visited = set()
        for t in range(T):
            s, _ = ep[t]

            if s not in visited:
                returns[s].append(G[t])
                visited.add(s)

    for s in range(n_states):
        if len(returns[s]) > 0:
            V[s] = np.mean(returns[s])

    return V
    
            
