# Los Buenos
Space Apps COVID-19 Challenge Project

## Pre Set-Up
* Set your NASA Earth Data credentials in scripts "download_data.py" and "process_data.py" by changing "username" and "password" variables
* Add Selenium Chrome Driver to your project folder (https://chromedriver.chromium.org/downloads)

## Project Usage

* Run "process_data.py" for processing Daily Country Average Temperature, Relative Humidity and NO2 Emision at NASA's Giovanni webpage.

* Run "download_data.py" for downloading Giovanni's data.

* Put downloaded files in your project folder, changing files' names according to the following pattern:

    "temp_[country]"
    
    "hum_[country]"

    "no2_[country]"

* Run "create_final_data" to create a file like the ones in folder "results/giovanni"

## Analysis

Data used:
* John Hopkins Coronavirus Resource Center Database (results/johnhopkins)
* Country Average Temperature, Relative Humidity and NO2 Emision from NASA's Giovanni Tool (results/giovanni)

Results stored in results/SpaceApps_Covid19 workbook.
