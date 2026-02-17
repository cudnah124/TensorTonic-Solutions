import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    # Write code here
    X = np.asarray(X)

    x_min = np.min(X, axis, keepdims = True)
    x_max = np.max(X, axis, keepdims = True)

    denom = np.maximum(x_max - x_min, eps)
    
    scaled = (X - x_min) / denom
    
    return scaled