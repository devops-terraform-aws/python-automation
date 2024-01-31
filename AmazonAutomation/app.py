# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from time import sleep

# product_price = []

# def get_webpage():
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#     driver.get("https://www.amazon.com/")
#     keyword = input("Enter item name: ")
#     search_box = driver.find_element(By.ID, 'twotabsearchtextbox')
#     search_box.send_keys(keyword)

#     search_button = driver.find_element(By.ID, 'nav-search-submit-button')
#     search_button.click()
#     driver.implicitly_wait(15)
#     sleep(5)

#     item_price = driver.find_elements(By.XPATH, './/span[@class="a-price-whole"]')
#     item_fraction = driver.find_elements(By.XPATH, './/span[@class="a-price-fraction"]')

#     if item_price !=[] and item_fraction !=[]:
#         final_price = '.'.join([item_price[0].text, item_fraction[0].text])
#     else:
#         final_price = 0
#     product_price.append(final_price)
#     print( "The", keyword, "is sold at", '${}'.format(product_price[0]))

# def main():
#     global options
#     options = webdriver.ChromeOptions()
#     options.add_experimental_option('excludeSwitches', ['enable-logging'])
#     options.add_argument("start-maximized")
#     get_webpage()

# if __name__ == "__main__":
#     main()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

options = None  # Define options as a global variable

product_price = []

def get_webpage():
    global options
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://www.amazon.com/")
    keyword = input("Enter item name: ")
    
    search_box = driver.find_element(By.ID, 'twotabsearchtextbox')
    search_box.send_keys(keyword)

    search_button = driver.find_element(By.ID, 'nav-search-submit-button')
    search_button.click()
    driver.implicitly_wait(10)  # Increased implicit wait time
    sleep(5)

    item_price = driver.find_elements(By.XPATH, './/span[@class="a-price-whole"]')
    item_fraction = driver.find_elements(By.XPATH, './/span[@class="a-price-fraction"]')

    if item_price and item_fraction:
        final_price = '.'.join([item_price[0].text, item_fraction[0].text])
    else:
        final_price = 0
    product_price.append(final_price)
    print("The", keyword, "is sold at", '${}'.format(product_price[0]))

def main():
    global options
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("start-maximized")
    get_webpage()

if __name__ == "__main__":
    main()
