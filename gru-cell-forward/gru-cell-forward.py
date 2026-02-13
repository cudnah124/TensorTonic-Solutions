import numpy as np

def _sigmoid(x):
    """Numerically stable sigmoid function"""
    return np.where(x >= 0, 1.0/(1.0+np.exp(-x)), np.exp(x)/(1.0+np.exp(x)))

def _as2d(a, feat):
    """Convert 1D array to 2D and track if conversion happened"""
    a = np.asarray(a, dtype=float)
    if a.ndim == 1:
        return a.reshape(1, feat), True
    return a, False

def gru_cell_forward(x, h_prev, params):
    """
    Implement the GRU forward pass for one time step.
    Supports shapes (D,) & (H,) or (N,D) & (N,H).
    """
    # Write code here
    h_prev = np.array(h_prev, dtype=float)
    x = np.array(x, dtype= float)
    D = x.shape[-1]
    H = h_prev.shape[-1]

    x, x_was_1d = _as2d(x, D)
    h_prev, h_was_1d = _as2d(h_prev, H)

    if not isinstance(params, dict):
        params = {
            "Wz": np.random.randn(D, H),
            "Uz": np.random.randn(H, H),
            "bz": np.zeros(H),
            "Wr": np.random.randn(D, H),
            "Ur": np.random.randn(H, H),
            "br": np.zeros(H),
            "Wh": np.random.randn(D, H),
            "Uh": np.random.randn(H, H),
            "bh": np.zeros(H),
        }

    z = _sigmoid(x @ params["Wz"] + h_prev @ params["Uz"] + params["bz"])
    r = _sigmoid(x @ params["Wr"] + h_prev @ params["Ur"] + params["br"])

    h_tilde = np.tanh(
        x @ params["Wh"] +
        (r * h_prev) @ params["Uh"] +
        params["bh"]
    )

    h = (1 - z) * h_prev + z * h_tilde

    if x_was_1d:
        h = h.reshape(-1)

    return h