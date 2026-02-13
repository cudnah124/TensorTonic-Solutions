import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    N = len(seqs)
    
    if max_len is None:
        L = max((len(s) for s in seqs), default=0)
    else:
        L = max_len

    new_seqs = np.full((N, L), pad_value)
    for i in range(N):
      length = min(len(seqs[i]), L)
      new_seqs[i, :length] = seqs[i][:length]
    return new_seqs
      
