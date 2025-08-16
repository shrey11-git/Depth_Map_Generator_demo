"""
Test Script for `gui.py` (DepthMapGUI)
This test covers:
- GUI widget initialization and layout.
- Button behavior and UI state switching between steps.
- The entire pipeline: loading, interpolation, visualization, and report generation.
- Uses mocking for heavy functions to avoid real computation or file generation.
"""

import pytest
import sys
from PyQt6.QtWidgets import QApplication
from unittest.mock import patch, MagicMock
from gui import DepthMapGUI


@pytest.fixture(scope="module")
def app():
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    yield app


def test_gui_initialization(app):
    gui = DepthMapGUI()
    assert gui.windowTitle() == "Depth Map Generator"
    assert gui.current_step == 1
    assert gui.load_button.text().startswith("Click here to load")
    assert gui.preview_box.toPlainText().startswith("Preview")


@patch("gui.load_and_clean_data")
@patch("gui.interpolate_and_save")
@patch("gui.visualize_all")
@patch("gui.generate_report")
def test_generate_visualizations_success(mock_report, mock_visualize, mock_interpolate, mock_loader, app):
    gui = DepthMapGUI()

    gui.selected_file = "dummy.csv"

    mock_loader.return_value = ("cleaned_dummy.csv", "Mock Summary")

    gui.generate_visualizations()

    assert gui.progress.value() == 100
    assert " All steps completed successfully!" in gui.feedback_box.toPlainText()
    assert gui.finish_btn.isEnabled()

    mock_loader.assert_called_once()
    mock_interpolate.assert_called_once()
    mock_visualize.assert_called_once()
    mock_report.assert_called_once()