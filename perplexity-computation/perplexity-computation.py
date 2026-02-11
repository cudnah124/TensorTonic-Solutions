import math
def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    # Write code here
    total_log_prob = 0
    N = len(actual_tokens)

    for i in range(N):
        p_actual = prob_distributions[i][actual_tokens[i]]

        total_log_prob += math.log(p_actual)
    
    cross_entrophy = - total_log_prob / N

    return math.exp(cross_entrophy)
    
