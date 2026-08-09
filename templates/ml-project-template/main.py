"""
ML Project Template
A boilerplate for machine learning and data science projects.
"""

from src.data_loader import load_data
from src.model import train_model, evaluate_model


def main():
    """Entry point for the ML pipeline."""
    print("Starting ML pipeline...")
    data = load_data()
    model, metrics = train_model(data)
    evaluate_model(model, data)
    print("Pipeline completed!")


if __name__ == "__main__":
    main()