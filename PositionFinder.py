
from msilib import Control
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import utils
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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
        apply_on_default_site = driver.find_element(By.XPATH, 'div[1]/div/span/div/span/a')
        apply_on_default_site.send_keys(Keys.CONTROL + "t")
        pass

    time.sleep(2)
    
    child_windows = driver.window_handles

    time.sleep(2)
    
    for window in child_windows:
        if(window!=head_page):
            #todo: switch and start application process
            pass
        
    time.sleep(2)