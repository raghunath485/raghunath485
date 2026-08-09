"""Unit tests for the ML pipeline."""

import pytest
import pandas as pd
from src.data_loader import load_data
from src.model import train_model, evaluate_model


def test_load_data_returns_dataframe():
    """Test that load_data returns a DataFrame."""
    data = load_data()
    assert isinstance(data, pd.DataFrame)


def test_load_data_has_expected_columns():
    """Test that data has expected columns."""
    data = load_data()
    assert "feature1" in data.columns
    assert "target" in data.columns


def test_train_model_returns_model_and_metrics():
    """Test that train_model returns a model and metrics dict."""
    data = load_data()
    model, metrics = train_model(data)
    assert model is not None
    assert "train_acc" in metrics


if __name__ == "__main__":
    pytest.main([__file__, "-v"])