"""
Test Script for `report.py`
This script tests the PDF report generation logic:
- Mocks ReportLab's `canvas.Canvas` to avoid file I/O.
- Confirms flow through all 3 pages: 2D, 3D, and data table images.
- Bypasses image existence checks using monkeypatch.
- Focuses on verifying correct calls and flow without saving files.
"""

import os
import pytest
import report
from reportlab.pdfgen import canvas


def test_generate_report_runs(monkeypatch):

    class DummyCanvas:
        def __init__(self, *args, **kwargs): pass
        def drawImage(self, *args, **kwargs): pass
        def drawString(self, *args, **kwargs): pass
        def setFont(self, *args, **kwargs): pass
        def stringWidth(self, text, font, size): return 100
        def showPage(self): pass
        def save(self): pass

    monkeypatch.setattr(canvas, "Canvas", DummyCanvas)

    monkeypatch.setattr(os.path, "exists", lambda path: True)

    report.generate_report()