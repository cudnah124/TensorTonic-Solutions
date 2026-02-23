def sarsa_update(q_table, state, action, reward, next_state, next_action, alpha, gamma):
    """
    Perform one SARSA update and return the updated Q-table.
    """
    # Write code here
    theta = reward + gamma * q_table[next_state][next_action] - q_table[state][action]

    q_table_new = q_table.copy()

    q_table_new[state][action] = q_table[state][action] + alpha * theta

    return q_table_new