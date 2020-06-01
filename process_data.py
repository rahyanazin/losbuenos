###################
username = USERNAME
password = PASSWORD
countries = ['Brazil', 'United States', 'China']
###################

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

giovanni_url = "https://giovanni.gsfc.nasa.gov/giovanni/"
area_average_humidty_temperature_no2_giovanni_url = "https://giovanni.gsfc.nasa.gov/giovanni/#service=ArAvTs&starttime=2019-01-01T00:00:00Z&endtime=2020-05-27T23:59:59Z&data=OMNO2d_003_ColumnAmountNO2CloudScreened%2CAIRS3STD_006_SurfSkinTemp_A(units%3DC)%2CAIRS3STD_006_RelHumSurf_D"

driver = webdriver.Chrome('chromedriver.exe')
driver.implicitly_wait(60)

### login to earth date
driver.get(area_average_humidty_temperature_no2_giovanni_url)
driver.find_element(By.ID,"loginLink").click()
driver.find_element(By.ID, "username").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.NAME, "commit").click()

### process countries' data
driver.get(area_average_humidty_temperature_no2_giovanni_url);
for country in countries:
    driver.find_element(By.ID, "sessionDataSelBbPkbbox").send_keys(f"Countries : {country};")
    driver.find_element(By.ID, "sessionDataSelToolbarplotBTN-button").click()
    driver.find_element(By.ID, "sessionWorkspaceToolbarselectDataBTN-button").click()