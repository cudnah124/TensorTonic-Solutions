import numpy as np

def r2_score(y_true, y_pred) -> float:
    """
    Compute R² (coefficient of determination) for 1D regression.
    Handle the constant-target edge case:
      - return 1.0 if predictions match exactly,
      - else 0.0.
    """
    # Write code here
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    y_a = np.sum((y_true - y_pred) ** 2)
    mean_y = np.mean(y_true)
    y_b = np.sum((y_true - mean_y) ** 2)

    if y_a == 0:
      return 1
    
    if y_b == 0:
      return 0
      
    return 1 - y_a / y_b 