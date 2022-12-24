from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager 
import time


def browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.instagram.com")
    time.sleep(10)
    return driver

def login(username, password):
   
        driver = webdriver.Chrome(ChromeDriverManager().install())
        #Find the username box address via XPath
        user_box = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        #Find the password box address via XPath
        password_box = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        #Find the login button via Xpath
        button = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]')
        #Click on the username box
        user_box.click()
        #And enter the username in the username box
        user_box.send_keys(username)
        #time.sleep(1)
        #Click on the password box
        password_box.click()
        #And enter the password in the password box
        password_box.send_keys(password)
        #time.sleep(1)
        #Finally, click the Login button
        button.click()
        time.sleep(5)


def comment(url_post, message=None):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(url_post)
        time.sleep(5)
        
        comment_box = driver.find_element(By.XPATH, '//*[@id="mount_0_0_qk"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea')
        comment_box.click()

        comment_box_2 = driver.find_element(By.XPATH, '//*[@id="mount_0_0_qk"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea')
        comment_box_2.send_keys(message)

        post_button = driver.find_element(By.XPATH, '//*[@id="mount_0_0_qk"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/button/div')
        post_button.click()
        time.sleep(10)

    





# write your code above this function 
browser()  
login('username_value', 'password_value')
comment('https://www.instagram.com/p/Chf-duXhmKK/', 'Francis. - Very Good')
