
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

searches = []

for search in searches:

    jobs = utils.initial_search(driver, search)
    
    for job in jobs:
        
        job.send_keys(Keys.CONTROL + Keys.RETURN)
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.TAB)

    time.sleep(2)
    
    child_windows = driver.window_handles

    time.sleep(2)
    
    for window in child_windows:
        if(window!=head_page):
            #todo: switch and start application process
            pass
        
    time.sleep(2)