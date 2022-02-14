#! venv/bin/python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from functools import wraps
from decouple import config
from time import sleep

service = Service(config("CHROMEDRIVER"))
options = webdriver.ChromeOptions()
# options.add_argument("")
driver = webdriver.Chrome(service=service, options=options)
driver.get(config("URL"))
image = driver.find_element(By.TAG_NAME, 'picture').find_element(By.TAG_NAME, 'img')
print(image.get_attribute('src'))