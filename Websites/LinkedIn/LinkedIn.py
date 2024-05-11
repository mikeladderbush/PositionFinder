from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def sign_in(driver):
    
    try:
        sign_in = driver.find_element(By.XPATH, '//*[contains(text(),"Sign in") or contains(text(),"sign in")]')
    except:
        print('Unable to find sign in to LinkedIn')
    else:
        sign_in.click()
        time.sleep(2)
        print('Made it to sign in!')
        email = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[1]/input')
        password = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[2]/input')
        dumby_sign_in = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[3]/button')
        dumby_sign_in.click()