from datetime import time, datetime
from lib2to3.pgen2 import driver
import os
from selenium import webdriver
# https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python
from selenium.webdriver.chrome.service import Service
####
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import pandas as pd

from time import sleep

import random

import pytest

from app import *

@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    driver.maximize_window()
    
    yield driver
    driver.quit()

def test_browser(browser):
    browser.get("https://www.bestbuy.com")
    
    assert "Best Buy" in browser.title
    
def test_search(browser):
    try:
        search = browser.find_element(By.NAME, "st")
        search.send_keys("Iphone")
        search.send_keys(Keys.ENTER)
        sleep(15)
        
        page_source = browser.page_source
        
        assert "Apple" in page_source
    
    except Exception as e:
        print(e)
    finally:
        browser.close()
        
def test_product_details():
    product="Apple - iPhone SE (3rd Generation) 64GB - Midnight (AT&T)"

    get_product_detail(product)
    
    page_source = browser.page_source
    
    assert "Apple" in page_source