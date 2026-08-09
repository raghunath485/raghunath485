"""Data loading utilities."""

import pandas as pd
from pathlib import Path


def load_data(filepath: str = None) -> pd.DataFrame:
    """Load data from CSV file or return sample data."""
    if filepath and Path(filepath).exists():
        return pd.read_csv(filepath)
    return pd.DataFrame(
        {
            "feature1": [1, 2, 3, 4, 5],
            "feature2": [2, 3, 4, 5, 6],
            "target": [0, 1, 0, 1, 0],
        }
    )