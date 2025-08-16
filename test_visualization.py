"""
Test Script for `visualization.py`
This script verifies the core plotting logic without saving outputs:
- Confirms `load_and_prepare_data()` handles NaNs and grid shape validation.
- Ensures `plot_2d()` and `plot_3d()` execute without GUI issues.
- Uses monkeypatching to bypass actual file creation and rendering.
"""

import numpy as np
import pytest
import visualization
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("Agg")


def test_load_and_prepare_data_runs_clean():
    """Test that data loads and contour levels are generated correctly."""
    lat, lon, depth_grid, levels, min_depth, max_depth = visualization.load_and_prepare_data()

    assert lat.shape == lon.shape == depth_grid.shape
    assert np.ma.is_masked(depth_grid)
    assert len(levels) >= 1
    assert min_depth >= 0
    assert max_depth >= min_depth


def test_plot_2d_executes_without_saving(monkeypatch):
    lat, lon, depth_grid, levels, min_depth, max_depth = visualization.load_and_prepare_data()

    monkeypatch.setattr(plt, "savefig", lambda *args, **kwargs: None)

    visualization.plot_2d(lat, lon, depth_grid, levels, min_depth, max_depth)


def test_plot_3d_executes_without_saving(monkeypatch):
    lat, lon, depth_grid, levels, min_depth, max_depth = visualization.load_and_prepare_data()

    monkeypatch.setattr(visualization.go.Figure, "write_image", lambda *args, **kwargs: None)

    visualization.plot_3d(lat, lon, depth_grid, levels, min_depth, max_depth)
