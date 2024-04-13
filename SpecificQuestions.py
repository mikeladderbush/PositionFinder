from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Accept new parameter for potential XPath values. 
# 
# Base questionnaire, next step is to use regex to make these more consistently able to answer
"""
    Job Specific Questions
 
 
    Questionnaire
 
    Please answer the following questions as accurately as possible.
    1. Based on your education and/or experience, which of the following requirements do you meet?

"""          
def break_down_questions(driver):
    # Add additional question templates based on other application questions
    try:
        question_template_form = driver.find_elements(By.XPATH, '//*[@id="et-ef-content-ftf-mastercontentpanel"]/table/tbody/tr/td/span[4]/span[3]')
    except:
        print("cant find question template")
    else:
        for element in question_template_form:
            print(element.text)
            if "education" in element.text:
                try:
                    bachelors_degree = driver.find_element(By.XPATH,"//*[contains(text(),'Bachelor')]")
                except:
                    print("can't find bachelors degree option")
                else:
                    bachelors_degree.click()
                    
            if "data visualization tools" in element.text:
                try:
                    one_to_three_years = driver.find_element(By.XPATH,"//*[contains(text(),'1 year')]")
                except:
                    print("can't find experience level option")
                else:
                    one_to_three_years.click()
                    
            if "Microsoft" in element.text:
                try:
                    microsoft_experience = driver.find_element(By.XPATH,"//*[contains(text(),'Advanced')]")
                except:
                    print("can't find microsoft experience")
                else:
                    microsoft_experience.click()
                    
            if "languages" in element.text:
                try:
                    python_selection = driver.find_element(By.XPATH,"//*[contains(text(),'Python')]")
                except:
                    print("Python not found")
                else:
                    python_selection.click()
                    
                try:
                    java_selection = driver.find_element(By.XPATH,"//*[contains(text(),'Java')]")
                except:
                    print("Java not found")
                else:
                    java_selection.click()
                        
                try:
                    cpp_selection = driver.find_element(By.XPATH,"//*[contains(text(),'C')]")
                except:
                    print("c++ not found")
                else:
                    cpp_selection.click()
                    
                try:
                    SQL_selection = driver.find_element(By.XPATH,"//*[contains(text(),'SQL')]")
                except:
                    print("SQL not found")
                else:
                    SQL_selection.click()
                    