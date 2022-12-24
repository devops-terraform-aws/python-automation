from datetime import time, datetime
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



def remove_csv_files():
    CURRENT_WORKING_DIR = os.getcwd()
    
    for files in os.listdir(CURRENT_WORKING_DIR):
        if files.endswith('csv'):
            try:
                os.remove(files)
                print("The file has been deleted successfully!")
            except:
                print("no such files")

def browser():
    #driver = webdriver.Chrome(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    driver.maximize_window()
    driver.get("https://www.bestbuy.com")
    #driver.find_elements(By.)
    
    return driver

def search_product(product):
    driver = browser()
    search = driver.find_element(By.NAME, "st")
    search.send_keys(product)
    search.send_keys(Keys.ENTER)
    sleep(15)
    return driver

# Finds the price of a specific product using its SKU number
def get_sku_price(driver): 
    price = driver.find_element(By.XPATH, '/html/body/div[3]/main/div[2]/div[3]/div[2]/div/div/div[1]/div/div/div/div/div[1]/div[1]/div[1]/div/span[1]').text

    # print(f"The item with sku number {product} has a price of {price}.")
    return(price)

# Return the number of product pages produced by the product search
# By extracting the last page number from the list of page numbers at the bottom of the page
def last_page_number(driver):
    content = driver.page_source
    soup = BeautifulSoup(content,"html.parser")

    pages = soup.find_all('li', attrs={'class':'page-item'})

    last_page = len(pages)
    if last_page <= 1:
        return(1)
    else:
        last_page = pages[-1].find("a", attrs={'class':'trans-button page-number'}).text
    return(last_page)


# Returns the prices on one page
def get_one_page_prices(driver, products, prices): 
    content = driver.page_source
    soup = BeautifulSoup(content,"html.parser")

    for a in soup.findAll('li', attrs={'class':'sku-item', 'data-itm':'false'}):
        sku = a.find('h4', attrs={'class':'sku-title'})
        name = sku.find('a')
        products.append(name.text)

        price_block = a.find('div', attrs={'class':'priceView-hero-price priceView-customer-price'})
        if price_block != None:
            price = price_block.find('span').text
        else:
            price = "Open Box"     
        prices.append(price)
        
        print(f"Product: {name.text} \nPrice: {price}\n")

# Moves to the next products page
def move_to_next_page(driver):
    next_page_button = driver.find_element(By.CLASS_NAME, "sku-list-page-next")
    next_page_button.click()

# Get products and prices on all pages
def get_all_pages_prices(driver, product): 
    products=[] #List to store product names
    prices=[] #List to store product prices

    # Get the last page number
    last_page = int(last_page_number(driver))
    #print(f"Last page is {last_page}")
    try:
        # Cycle through all the pages
        if last_page == 1:
            get_one_page_prices(driver, products, prices)
        else:
            for page in range(last_page):
                # Get prices of the current page
                print(f"Processing Page: {page + 1}")
                get_one_page_prices(driver, products, prices)
                
                # Move to the next page
                move_to_next_page(driver)

        # Save products and prices
        filename = unique_filename(product)
        save_products(products, prices, filename)
        return(filename), products
    except:
        print("Element click intercepted!")
        pass

# Stores product names and prices in a csv file
def save_products(products, prices, filename):
    df = pd.DataFrame({'Product Name':products,'Price':prices}) 
    df.to_csv(filename, index=False, encoding='utf-8')


# Generates a unique file name
def unique_filename(product):
    now = datetime.now()
    date_time = now.strftime("%m-%d-%Y-%H-%M-%S")
    filename = "prices_" + product + "_" + date_time + ".csv"
    return(filename)

# Get prices
def get_prices(product):
    # Search the product
    driver = search_product(product)

    # Get prices
    filename = get_all_pages_prices(driver, product)

    # Shuts down the browser
    driver.quit()

    # Returns the filename containing the product prices
    return(filename)

# Product detailed page
def get_product_detail(product):
    product_sku = []
    # search product
    driver = search_product(product)
    try:
        # get random product
        product_list = get_all_pages_prices(driver, product)[1]
        rand_product = random.choice(product_list)
        print(rand_product)
        print(type(rand_product))
        # products(rand_product)
        # search the random product
        searched_product = search_product(rand_product)
        sleep(10)
        items = searched_product.find_elements(By.CLASS_NAME, 'sku-title')
        for item in items:
            # print(item.text)
            product_sku.append(item.text)
            sleep(10)
        for sku in product_sku:
            if sku == product_sku[5]:
                selected_sku = driver.find_element(By.CLASS_NAME, 'sku-title')
                selected_sku.click()
                sleep(10)
        
        return product_sku
    except:
        print("No product is selected")
        pass

def main():
    remove_csv_files()
    product="Apple - iPhone SE (3rd Generation) 64GB - Midnight (AT&T)"
    filename = get_prices(product)
    print(filename)
    get_product_detail(product)

if __name__ == "__main__":
    main()
