from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def sign_in(driver):
    
    try:
        sign_in = driver.find_element(By.XPATH, '//*[contains(text(),"Sign in") or contains(text(),"sign in")]')
    except:
        print('Unable to find sign in to Glassdoor')
    else:
        sign_in.click()
        time.sleep(2)
        print('Made it to sign in!')