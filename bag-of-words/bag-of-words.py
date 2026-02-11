import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    if not vocab:
        return np.asarray(vocab, dtype = int)

    count = {}
    for i in range(len(vocab)):
        count[vocab[i]] = 0

    for i in range(len(tokens)):
        if tokens[i] in vocab:
            count[tokens[i]] += 1
    
    return np.asarray([count[i] for i in vocab], dtype = int)