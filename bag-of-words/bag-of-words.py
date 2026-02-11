import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    vector = np.zeros(len(vocab), dtype=int)
    
    vocab_map = {word: i for i, word in enumerate(vocab)}
    
    for word in tokens:
        if word in vocab_map:
            vector[vocab_map[word]] += 1
            
    return vector