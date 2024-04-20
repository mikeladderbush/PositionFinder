from turtle import position
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import exceptions
import time


#initial google search, takes our driver and the search input, i.e. "Software Developer"
def initial_search(driver, input):
    
    #Find our google search bar, send it the input, search it, then find the job box and click it
    search_bar = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
    search_bar.send_keys(f'{input}')
    search_bar.send_keys(Keys.ENTER)
    scroll_box_jobs = driver.find_element(By.XPATH, '//*[@id="fMGJ3e"]/a')
    scroll_box_jobs.click()
    


def set_google_filters(driver, filters):
    
    #create filters dictionary that contains "Location", "Date Posted", "Requirements", "Type", etc.
    for filter in filters:
        #this is a placeholder for when I create the dictionary
        """if filter == "location: 30mi":
            30miles = driver.find_element(By.XPATH, '//*[@id="choice_box_root"]/div[2]/div[2]/div[1]/div[4]/span')
            30miles.click()"""
        pass
    


#roughly finds the first present apply box, will be used once all links are open in tabs.
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
        

#sign in to speed up applying depending on types of websites like linkedIn/workday.
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
        




        







        