def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    TP = 0
    FP = 0
    FN = 0
    for i in range(len(y_pred)):
        if y_pred[i] == y_true[i]:
            TP += 1
        if y_pred[i] != y_true[i] and y_pred[i] in y_true:
            FP += 1
        if y_pred[i] != y_true[i]:
            FN += 1
    
    return (2 * TP) / (2 * TP + FP + FN)