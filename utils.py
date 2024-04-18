from turtle import position
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import exceptions
import time



def initial_search(driver, input):
    
    search_bar = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
    search_bar.send_keys(f'{input}')
    time.sleep(2)
    scroll_box_jobs = driver.find_elements(By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div/div/div[3]/div[1]/div[1]/div[3]/ul/li')
    return scroll_box_jobs



def find_application (driver):

    try:
        
        apply_link = driver.find_element(By.XPATH,"//*[contains(text(),'Apply')]")
        apply_link.click()
        time.sleep(1)
        
        try:
            accept_cookies = driver.find_element(By.XPATH, "//*[contains(text(),'Accept Cookies') or contains(text(),'Cookies')]")
        except:
            pass
        else:
            accept_cookies.click()
            time.sleep(1)
            
        try:
            accept_terms = driver.find_element(By.XPATH, '//*[@id="dialogTemplate-dialogForm-StatementBeforeAuthentificationContent-ContinueButton"]')
        except:
            pass
        else:
            accept_terms.click()
            time.sleep(1)
        
        if driver.find_element(By.XPATH, "//*[contains(text(),'Workday')]"):
            
            websiteType = "Workday"
            sign_in(driver, websiteType)
        
        
    except Exception:
        
        raise exceptions.LoginException
        
    else:
        
        pass
        


def sign_in(driver, websiteType):
    
    #Need to change for different websites and emails depending on if they work
    if websiteType == "Workday":
        
        email = driver.find_element(By.XPATH, '//*[@id="input-4"]')
        password = driver.find_element(By.XPATH,  '//*[@id="input-5"]')
        email.send_keys('mikeladderbush@gmail.com')
        password.send_keys('Applesauce1%')
        sign_in_button = driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div[1]/section/div/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/form/div[3]/div/div/div/div/div')
        
        try:
            sign_in_button.click()
        except:
            print("Cant sign into workday")
        else:
            pass
        




        







        