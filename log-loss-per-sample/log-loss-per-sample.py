import math

def log_loss(y_true, y_pred, eps=1e-15):
    """
    Compute per-sample log loss.
    """
    # Write code here

    L = []

    for y, y_p in zip(y_true, y_pred):
        # clip trước
        y_p = min(max(y_p, eps), 1 - eps)

        loss = -(y * math.log(y_p) +
                 (1 - y) * math.log(1 - y_p))

        L.append(loss)

    return L