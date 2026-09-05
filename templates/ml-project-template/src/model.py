"""Model training and evaluation utilities."""

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split


def train_model(data):
    """Train a logistic regression model."""
    X = data[["feature1", "feature2"]]
    y = data["target"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    model = LogisticRegression()
    model.fit(X_train, y_train)
    metrics = {"train_acc": accuracy_score(y_train, model.predict(X_train))}
    return model, metrics


def evaluate_model(model, data):
    """Evaluate the trained model."""
    X = data[["feature1", "feature2"]]
    y = data["target"]
    preds = model.predict(X)
    report = classification_report(y, preds)
    print(report)
