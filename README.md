# 🗺️ Depth Map Generator
A Python-based tool for processing raw bathymetric CSV data from Autonomous Surface Vehicles (ASVs) to generate detailed depth maps and comprehensive PDF reports.
# ※ About the Project
The Depth Map Generator is a fully automated software tool designed to process raw bathymetric data in CSV format, typically collected from Autonomous Surface Vehicles (ASVs). The tool performs data cleaning, interpolation, visualization, and report generation, producing professional 2D and 3D depth maps and a summarized PDF report. Built with a user-friendly PyQt6 interface, it supports both raw and pre-cleaned datasets, ensuring flexibility for various use cases in marine and geospatial analysis.
# ※ Key Features
- Data Cleaning: Validates and cleans CSV data by handling null values, duplicates, and outliers using an adaptive IQR-based method.
- Interpolation: Applies CloughTocher2D interpolation to generate a smooth grid from sparse bathymetric data.
- Visualization: Creates high-quality 2D contour maps with satellite basemaps and interactive 3D surface plots using Matplotlib and Plotly.
- Report Generation: Produces a three-page PDF report containing a 2D map, 3D map, and a data table with key statistics.
- User Interface: Offers a modern, frameless PyQt6 GUI with file selection, data preview, and progress tracking.
- Modular Design: Separates functionality into distinct modules for maintainability and scalability.
# ※ Tech Stack
- Programming Language: Python 3.10+
- Core Libraries:
  - pandas: Data manipulation and CSV handling
  - numpy: Numerical computations
  - scipy: CloughTocher2D interpolation
  - matplotlib: 2D contour plotting
  - plotly: Interactive 3D surface plotting
  - PyQt6: GUI development
  - ReportLab: PDF report generation
  - contextily: Satellite basemap integration
- Helper Libraries:
  - PyInstaller: Packaging the application into an executable
  - pytest: Unit testing
  - geopandas: Geospatial data support
- Package Installer: pip for installing Python packages
# ※ Project Structure
- Note: The actual source code is not included. The following structure and descriptions are provided in /architecture as design references to illustrate how the codebase was organized.

The project is organized into modular Python scripts, each handling a specific part of the pipeline:
- main.py: Entry point for the application, orchestrating the pipeline and launching the GUI. Supports CLI execution for debugging.
- gui.py: Implements the PyQt6-based GUI for user interaction, file selection, data preview, and visualization generation.
- data_loader.py: Handles loading, validation, and cleaning of CSV data, ensuring required columns (lat, lon, distance) and removing outliers.
- interpolation.py: Performs grid interpolation using CloughTocher2DInterpolator and saves results in CSV and NPZ formats.
- visualization.py: Generates 2D contour maps, 3D surface plots, and data tables, saving outputs as PNG files.
- report.py: Creates a three-page PDF report using ReportLab, incorporating visualizations and a data table.
All outputs (visualizations and reports) are saved in the output/visualizations directory.

<img width="180" height="220" alt="image" src="https://github.com/user-attachments/assets/71d0d008-114a-4ab3-8686-503d6f8a3a62" />

# ※ Usage (Demo Workflow)
This section illustrates how the tool works (as shown in the demo GIF/screenshots below).
- Launch the GUI:
  - Run python main.py or main.exe to open the Depth Map Generator interface.
- Select a CSV File:
  - Click the "Load" button to choose a bathymetric CSV file.
  - Preview the first 10 rows in the GUI.
  - Choose whether the data is raw (needs cleaning) or pre-cleaned.
- Generate Visualizations:
  - Click "Next" to proceed to the visualization step.
  - Click "Generate Visualizations" to process the data, create maps, and generate the report.
  - Monitor progress via the progress bar and feedback log.
- View Outputs:
Upon completion, click "Finish" to open the output folder containing:
  - bathymetry_2d_map.png: 2D contour map
  - bathymetry_3d_map.png: 3D surface plot
  - bathymetry_data_table.png: Data table
  - bathymetry_report.pdf: Three-page PDF report
- CLI Mode (Optional):
  - Uncomment the relevant lines in main.py to run the pipeline via the command line for debugging or automation.
- Note: Source code and executables are not included in this demo repository.
# ※ Screenshots / Demo
- GUI File Selection: Displays file selection, data preview, and raw/cleaned data options.
- GUI Visualization: Shows progress bar and feedback during processing.
<img width="500" height="500" alt="2" src="https://github.com/user-attachments/assets/925dbcb7-d017-4e55-8ea3-6f733e94c905" />
<img width="500" height="500" alt="4" src="https://github.com/user-attachments/assets/5c74a610-19bd-45af-a35b-558b9733976d" />

- Demo:
![Untitled video - Made with Clipchamp mp4](https://github.com/user-attachments/assets/90542c97-fafd-4ee1-bb4b-a6538d0937b8)

# ※ Internship Context
This project was developed as part of an internship under CORATIA TECHNOLOGIES Pvt. Ltd. focused on automating bathymetric data processing for marine research. The goal was to create a user-friendly tool that transforms raw ASV data into actionable visualizations and reports, reducing manual effort for researchers and surveyors. The tool addresses the need for reliable, automated processing of geospatial data while maintaining high-quality outputs suitable for professional reports.
# ※ Learnings & Contributions
- Learnings:
  - Learnt about professional software development practices
  - Mastered geospatial data processing using pandas, numpy, and scipy.
  - Gained expertise in GUI development with PyQt6, including custom window designs and event handling.
  - Learned to integrate multiple visualization libraries (matplotlib, plotly, contextily) for diverse output formats.
  - Developed skills in PDF generation using ReportLab for professional reporting.
  - Improved error handling and data validation techniques for robust data pipelines.
- Contributions:
  - Built a complete end-to-end pipeline for bathymetric data processing.
  - Designed a modular codebase for easy maintenance and extensibility.
  - Implemented adaptive algorithms (e.g., IQR-based outlier removal, dynamic grid resolution) for data-specific processing.
  - Created a user-friendly GUI to simplify complex workflows for non-technical users.
  - Delivered professional-grade visualizations and reports suitable for marine research applications.
# ※ Challenges Faced
- Data Quality Variability: Handling diverse CSV formats with missing or invalid data required robust validation and cleaning logic.
- Visualization Scalability: Balancing high-resolution visualizations with memory constraints, especially for large datasets, necessitated dynamic grid resolution adjustments.
- GUI Design: Implementing a frameless, draggable window with a modern aesthetic while ensuring cross-platform compatibility was complex.
- Dependency Management: Resolving compatibility issues between matplotlib, plotly, and contextily required careful environment configuration.
- Performance Optimization: Optimizing interpolation and visualization steps for large datasets to ensure reasonable processing times.
# ※ Future Scope / Improvements
- Advanced Interpolation Methods: Integrate additional interpolation techniques (e.g., Kriging via PyKrige) for improved accuracy.
- Real-Time Visualization: Add interactive previews of 2D/3D maps within the GUI using pyvista or plotly.
- Batch Processing: Support processing multiple CSV files in a single session.
- Customizable Reports: Allow users to customize PDF report layouts and content via the GUI.
# ※ Acknowledgements
- Coratia Technologies: For providing the opportunity to develop this project during the internship.
- Open-Source Community: For the robust libraries (pandas, numpy, scipy, matplotlib, plotly, PyQt6, ReportLab, contextily) that made this project possible.
- References: Medium articles on Python best practices, pandas documentation, and SciPy's CloughTocher2DInterpolator documentation for guiding implementation.

# ※ Disclaimer
- # This repository is for demonstration purposes only.
- # Due to NDA restrictions with Coratia Technologies Pvt. Ltd., the source code and proprietary datasets are not included.
- # The content here (architecture notes, demo screenshots, visual previews, and learnings) is solely intended to showcase my contributions and project experience to recruiters and academic evaluators.
- # All rights reserved. No part of this repository may be copied, reused, or redistributed without explicit permission.
