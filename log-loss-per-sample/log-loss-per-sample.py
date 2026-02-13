import math

def log_loss(y_true, y_pred, eps=1e-15):
    """
    Compute per-sample log loss.
    """
    # Write code here
    return [-(y * math.log(min(max(y_p, eps), 1-eps)) + (1 - y) * math.log(1 - min(max(y_p, eps), 1-eps))) for y, y_p in zip(y_true, y_pred)]