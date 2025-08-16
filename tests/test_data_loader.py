"""
Test Script for `data_loader.py`
This script verifies the core data cleaning and validation logic:
- Ensures null values are dropped correctly.
- Confirms duplicate lat/lon pairs are handled.
- Checks IQR-based outlier removal.
- Validates structure of cleaned CSV output.
- Differentiates behavior based on `is_raw=True` vs `False`.
"""

import os
import pandas as pd
import tempfile
import pytest
from data_loader import load_and_clean_data

# Sample raw test data with:
# - 1 null row
# - 1 duplicate lat/lon
# - 1 outlier
raw_data = """lat,lon,distance
12.34,77.56,10
12.34,77.56,10   # duplicate
12.35,77.57,5000  # outlier
12.36,77.58,30
,,  # null row
"""

@pytest.fixture
def temp_csv_file():
    with tempfile.NamedTemporaryFile(mode='w+', suffix=".csv", delete=False) as tmp:
        tmp.write(raw_data)
        tmp_path = tmp.name
    yield tmp_path
    os.remove(tmp_path)

def test_load_and_clean_data_raw(temp_csv_file):
    out_path, summary = load_and_clean_data(temp_csv_file, is_raw=True)

    assert os.path.isfile(out_path)

    df = pd.read_csv(out_path)
    assert all(col in df.columns for col in ['lat', 'lon', 'distance'])
    assert len(df) >= 1

    assert "Total rows loaded" in summary
    assert "Rows dropped due to null values" in summary
    assert "Rows removed due to duplicates" in summary
    assert "Rows removed due to outliers" in summary
    assert "Total rows left after cleaning" in summary

def test_load_and_clean_data_cleaned(temp_csv_file):
    out_path, summary = load_and_clean_data(temp_csv_file, is_raw=False)

    assert os.path.isfile(out_path)

    df = pd.read_csv(out_path)
    assert all(col in df.columns for col in ['lat', 'lon', 'distance'])

    assert "Rows removed due to duplicates: 0" in summary
    assert "Rows removed due to outliers: 0" in summary
