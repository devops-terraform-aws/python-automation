from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

google_chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
google_chrome.get("https://www.ziprecruiter.com/")

sleep(20)