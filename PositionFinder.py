
from msilib import Control
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import utils
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import Websites.Site_Parser

options = Options()
# options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options)
driver.get('https://www.google.com/')

head_page = driver.current_window_handle

searches = ["Software Engineer Jobs"]

for search in searches:

    utils.initial_search(driver, search)
            
    #find all job boxes, loop through them opening each default application site in a new tab.
    jobs = driver.find_elements(By.TAG_NAME, 'li')
    
    for job in jobs:
        job.click()
        time.sleep(2)
        apply_on_default_site = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[1]/div/div/div[3]/div[2]/div/div[1]/div/div/g-scrolling-carousel/div[1]/div/span/div/span[1]/a")
        apply_on_default_site.click()
        pass

    time.sleep(2)
    
    original_window = driver.current_window_handle

    time.sleep(2)
    
    for window in driver.window_handles:
        if window != original_window:
            #todo: switch and start application process
            driver.switch_to.window(window)
            site_type = Websites.Site_Parser.site_determination(driver)
            pass
        
        
    time.sleep(2)