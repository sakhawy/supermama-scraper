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
title = driver.title
duration = driver.find_element(By.CLASS_NAME, 'recipe__duration').find_element(By.TAG_NAME, 'span').text
quantity = driver.find_element(By.CLASS_NAME, 'recipe__quantity').find_element(By.TAG_NAME, 'span').text
nutrition = driver.find_element(By.CLASS_NAME, 'recipe__nutrition').find_element(By.TAG_NAME, 'span').text
recipe = [x for x in driver.find_element(By.CLASS_NAME, 'container').find_element(By.TAG_NAME, 'ul').find_elements(By.TAG_NAME, 'li')]