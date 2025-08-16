"""
Test Script for `interpolation.py`
This script tests the interpolation pipeline using a real cleaned CSV:
- Verifies output `.npz` and `.csv` files are created.
- Checks existence and structure of interpolated grid arrays (`lat`, `lon`, `distance`).
- Ensures consistency in array dimensions (used in plotting later).
"""

import os
import pytest
import numpy as np
import pandas as pd

from interpolation import interpolate_and_save


def test_interpolation_with_real_cleaned_data():
    cleaned_csv_path = r"Z:\_Bathymetry_Tool_\data\cleaned_data.csv"
    temp_dir = os.path.dirname(cleaned_csv_path)
    output_npz_path = os.path.join(temp_dir, "interpolated_test_output.npz")
    output_csv_path = output_npz_path.replace(".npz", ".csv")

    interpolate_and_save(cleaned_csv_path=cleaned_csv_path, output_path=output_npz_path)

    assert os.path.exists(output_npz_path), "Interpolated .npz file not found."
    assert os.path.exists(output_csv_path), "Interpolated .csv file not found."

    data = np.load(output_npz_path)
    assert "lat" in data and "lon" in data and "distance" in data, "Expected keys missing in NPZ output."
    assert data["lat"].shape == data["lon"].shape == data["distance"].shape, "Grid shape mismatch."

    print(" Interpolation output verified on real cleaned dataset.")
