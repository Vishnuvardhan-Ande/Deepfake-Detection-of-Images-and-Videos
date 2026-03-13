from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def calculate_metrics(y_true, y_pred):
    return {
        "accuracy": "Not available (no evaluation dataset loaded)",
        "precision": "N/A",
        "recall": "N/A"
    }
def metrics():
    # Replace with real saved validation data
    y_true = [0,1,0,1]
    y_pred = [0,1,0,0]

    from metrics import calculate_metrics
    return calculate_metrics(y_true, y_pred)