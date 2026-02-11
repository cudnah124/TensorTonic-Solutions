import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Write code here
    angle_rads = np.arange(seq_len)[:, np.newaxis] / np.power(base, (2 * (np.arange(d_model)[np.newaxis, :] // 2)) / np.float32(d_model))
    
    angle_rads[:, 0::2] = np.sin(angle_rads[:, 0::2])
    
    angle_rads[:, 1::2] = np.cos(angle_rads[:, 1::2])
    
    return angle_rads