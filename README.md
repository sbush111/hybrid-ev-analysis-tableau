# Hybrid and Electric Vehicle Adoption: Analysis and Visualization

A Tableau data visualization project that assesses the current state of Hybrid and Electric Vehicle adoption in the U.S.

## Overview

Click below to see the video presentation for this project 🡓🡓🡓 

[![Watch the video](https://img.youtube.com/vi/FuW8dX3bUlw/0.jpg)](https://www.youtube.com/watch?v=FuW8dX3bUlw)

This report seeks to 
assess the current state of Hybrid and Electric Vehicle (H/EV) adoption in the United States in 
2026 by visualizing data concerning H/EV sales in Tableau, combining them into several 
dashboards comprising a single story, and publishing that story to the Tableau Public web 
platform.

The project originally took advantage of Tableau Public's ability to periodically update data from a google spreadsheet by using GitHub Actions to pull data from an API and push it to the google spreadsheet, but that feature has since been terminated. The code that supported it is still visible in the repository, however, to demonstrate knowledge of interacting with APIs and GitHub Actions.

## The Respository

As this is a fairly small project, the repo's structure is straightforward. All data used for the analysis are in the form of .csv files in the /data directory. Also in that directory is references.txt which lists the source of each dataset.

All other files exist at the root directory:
* dummy_api.py - a Python script that simulates the results of calls to the NLR API for development purposes
* envinroment.json - the environment file for the Anaconda environment used in this project. With Anaconda installed on your machine use `conda create --file environment.json` to clone the environment.
* server.bat - a Windows Batch script which launches the dummy API server within the conda environment
* update_data.py - the script run by GitHub Actions to pull data from the NLR API and push it to the Google Spreadsheet
* workbook.twbx - the Tableau workbook which contains all of the data visualizations for this project

## Viewing the Workbook

Visitors to this repository have two main options for viewing and interacting with the Tableau Workbook:
* Download [Tableau Desktop](https://www.tableau.com/products/desktop) and use it to open the file
* Visit the [browser version of the workbook](https://public.tableau.com/app/profile/sean.bush/viz/TheStateofHybridandElectricVehicleAdoptionintheU_S_/U_S_HybridEVAdoptionStory) on the Tableau Public platform
