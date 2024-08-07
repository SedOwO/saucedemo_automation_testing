from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


try:
    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/')
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'user-name')))
    
    username_input = driver.find_element(By.ID, 'user-name')
    username_input.send_keys('standard_user')
    
    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys('secret_sauce')
    
    time.sleep(5)
    
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()
    
    time.sleep(5)
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'inventory_item')))
    
    add_to_cart_button = driver.find_element(By.CLASS_NAME, 'btn_inventory')
    add_to_cart_button.click()
    
    time.sleep(5)
    
    cart_icon = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
    cart_icon.click()
    
    time.sleep(5)
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'cart_item')))
    cart_items = driver.find_elements(By.CLASS_NAME, 'cart_item')
    
    if len(cart_items) > 0:
        print("Item successfully added to the cart!")
    else:
        print("Cart is empty!")
    
finally:
    driver.quit()
