from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import Websites.LinkedIn.LinkedIn
import Websites.Generic.Generic_Careers
import Websites.Zip_Recruiter.Zip_Recruiter
import Websites.Glassdoor.Glassdoor
import time

def site_determination(driver):
    
    print(driver.current_url)

    if 'linkedin' in driver.current_url:
        Websites.LinkedIn.LinkedIn.sign_in(driver)
        time.sleep(2)
    
    if 'careers' in driver.current_url:
        Websites.Generic.Generic_Careers.sign_in(driver)
        time.sleep(2)
        Websites.Generic.Generic_Careers.one_page_application(driver)
        
    if 'ziprecruiter' in driver.current_url:
        Websites.Zip_Recruiter.Zip_Recruiter.sign_in(driver)
       
    if 'glassdoor' in driver.current_url:
        Websites.Glassdoor.Glassdoor.sign_in(driver)