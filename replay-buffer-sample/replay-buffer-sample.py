import numpy as np

def replay_buffer_sample(buffer, batch_size, seed):
    """
    Sample a batch of transitions from the replay buffer.
    """
    # Write code here
    np.random.seed(seed)
    idx = np.random.choice(len(buffer), batch_size, replace=False)
    batch = [buffer[i] for i in idx]
    return batch
    