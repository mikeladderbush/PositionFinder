
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import utils


options = Options()
# options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options)
driver.get('https://massanf.taleo.net/careersection/ex/jobsearch.ftl')

head_page = driver.current_window_handle

jobs = []

time.sleep(5)

utils.sign_in(driver)

time.sleep(5)

utils.set_filters(driver)

time.sleep(5)
    
utils.get_jobs(driver)
    
child_windows = driver.window_handles

time.sleep(2)

for window in child_windows:
    if(window!=head_page):
        utils.switch_to_and_apply(driver, window)
        
time.sleep(2)