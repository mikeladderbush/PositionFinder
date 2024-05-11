from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
import Websites.Workday.Workday

def sign_in(driver):
    
    try:
        sign_in = driver.find_element(By.XPATH, '//*[contains(text(),"Sign in") or contains(text(),"sign in")]')
    except:
        print('Unable to find sign in to Generic Career Site')
    else:
        #Add functionality if sign in is not interactable
        sign_in.click()
        time.sleep(2)
        print('Made it to sign in!')
        if 'workday' in driver.current_url:
            Websites.Workday.Workday.sign_in(driver)
        
def one_page_application(driver):
    
    try:
        first_name = driver.find_element(By.XPATH, '//*[contains(text(),"First")')
        last_name = driver.find_element(By.XPATH, '//*[contains(text(),"Last")')
    except:
        print('Unable to find name entry points')
    else:
        pass