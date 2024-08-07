from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


try:
    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/')
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'user-name')))
    
    username_input = driver.find_element(By.ID, 'user-name')
    username_input.send_keys('standard_user')
    
    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys('wrong_password')
    
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()
    
    
    
finally:
    print("\nlogin failed, incorrect username or password")
    driver.quit()
