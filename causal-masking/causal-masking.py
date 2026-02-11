import numpy as np

def apply_causal_mask(scores, mask_value=-1e9):
    """
    scores: np.ndarray with shape (..., T, T)
    mask_value: float used to mask future positions (e.g., -1e9)
    Return: masked scores (same shape, dtype=float)
    """
    # Write code here
    
    masks = np.triu(np.zeros(scores.shape) + mask_value, k = 1)

    return scores - np.triu(scores, k = 1) + masks