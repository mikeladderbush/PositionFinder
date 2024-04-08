
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import exceptions
import time
import SpecificQuestions


# Accept new parameter for potential XPath values.
# bachelors_degree = driver.find_element(By.XPATH,"//*[text()[contain(., 'A Bachelor')]")
# search for text and then use that to determine paths, look below at software/developer search line. Optimize later
def sign_in (driver):

    try:
        sign_in = driver.find_element(By.XPATH, '//*[text()="Sign In"]')
        sign_in.click()
        time.sleep(1)

        accept_terms = driver.find_element(By.XPATH, '//*[@id="dialogTemplate-dialogForm-StatementBeforeAuthentificationContent-ContinueButton"]')
        accept_terms.click()
        time.sleep(1)

        user_name = driver.find_element(By.XPATH, '//*[@id="dialogTemplate-dialogForm-login-name1"]')
        password = driver.find_element(By.XPATH, '//*[@id="dialogTemplate-dialogForm-login-password"]')
        user_name.send_keys('Michael123')
        password.send_keys('Applesauce1%')
        
        login_button = driver.find_element(By.XPATH, '//*[@id="dialogTemplate-dialogForm-login-defaultCmd"]')
        login_button.click()
        
    except Exception:
        
        raise exceptions.LoginException
        
    else:
        
        pass
        
     
        
def set_filters(driver):
    
    try:
        # Replace Magic variables
        location_check_box = driver.find_element(By.XPATH, '//*[@id="LOCATION-content"]/div[2]/div[3]/a/label/div')
        location_check_box.click()
        time.sleep(2)

        job_field_check_box_1 = driver.find_element(By.XPATH, '//*[@id="JOB_FIELD-content"]/div[1]/div[7]/a/label/div')
        job_field_check_box_1.click()
        time.sleep(2)
    
        show_more_box = driver.find_element(By.XPATH, '//*[@id="JOB_FIELD-moreless"]')
        show_more_box.click()
        time.sleep(2)
    
        job_field_check_box_2 = driver.find_element(By.XPATH, '//*[@id="JOB_FIELD-content"]/div[1]/div[11]/a/label/div')
        job_field_check_box_2.click()
        time.sleep(2)
        
    except Exception:
        
        raise exceptions.FilterException
        
    else:
        
        pass



def get_jobs(driver):
            
    try:
        
        position_elements = driver.find_elements(By.XPATH, '//li/div[2]/div[1]/span[1]/a')
        status_elements = driver.find_elements(By.XPATH, '//li/div[3]/a')
        complete_elements = zip(position_elements, status_elements)

    except Exception:
        
        raise exceptions.GetJobsException
        
    else:
        
        for title, status in complete_elements:
            
            if("Software" in title.text or "Developer" in title.text or "Data" in title.text):
                
                if("Finish Draft Submission" in status.text or "Apply" in status.text):
                    
                    title.send_keys(Keys.CONTROL + Keys.RETURN)
                    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.TAB)
            


def switch_to_and_apply(driver, window, *args):
    
    driver._switch_to.window(window)
    time.sleep(2)
    
    if args:
        for ar in args:
            application_step_text = ar.text
        
    else:
        try:
            # Replace Magic variables
            apply = driver.find_element(By.XPATH, '//*[@id="requisitionDescriptionInterface.UP_APPLY_ON_REQ.row1"]')
            apply.click()
    
            application_step = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/div/div/form/span/span[2]/span[3]/span[2]/span[1]')
            application_step_text = application_step.text
        
        except Exception:
        
            raise exceptions.ApplicationStepException('application_text step', 'Application step unable to be located')

    match application_step_text:
            
        case 'Step 1 out of 10' | 'Step 1 out of 9':
                
            try:
                    
                source = driver.find_element(By.XPATH, '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_2-sourceTrackingBlock-recruitmentSourceType"]')
                source.click()

                job_board = driver.find_element(By.XPATH, '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_2-sourceTrackingBlock-recruitmentSourceType"]/option[6]')
                job_board.click()
            
                time.sleep(2)
                
                board_selection = driver.find_element(By.XPATH, '//*[@id="recruitmentSourceDP"]')
                board_selection.click()

                indeed = driver.find_element(By.XPATH, '//*[@id="recruitmentSourceDP"]/option[9]')
                indeed.click()

                time.sleep(2)
                
                save_and_continue = driver.find_element(By.XPATH, '//*[@id="et-ef-content-ftf-saveContinueCmdBottom"]')
                save_and_continue.click()
                
                ar = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/div/div/form/span/span[2]/span[3]/span[2]/span[1]')
                
                time.sleep(3)
                window = driver.current_window_handle
                switch_to_and_apply(driver, window, ar)
                    
            except Exception:
                    
                raise exceptions.ApplicationStepException('Step 1', 'Unable to complete basic information')

        
        case 'Step 2 out of 10' | 'Step 2 out of 9':
                
            try:
                    
                general_questions = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/div/div/form/span/span[2]/span[4]/table/tbody/tr/td/h1/span[1]')
                save_question = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/div/div/form/span/span[2]/span[5]/span[1]/span/span[1]/input[1]')
                save_question.click()
                    
                ar = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/div/div/form/span/span[2]/span[3]/span[2]/span[1]')

                time.sleep(3)
                window = driver.current_window_handle
                switch_to_and_apply(driver, window, ar)

            except Exception:
                    
                raise exceptions.ApplicationStepException('Step 2', 'Unable to complete general questions')
    
        case 'Step 3 out of 10':
                
            try:
                    
                SpecificQuestions.break_down_questions(driver)
                save_and_continue = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/div/div/form/span/span[2]/span[5]/span[1]/span/span[1]/input[1]')
                save_and_continue.click()
                
                ar = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/div/div/form/span/span[2]/span[3]/span[2]/span[1]')
                    
                time.sleep(3)
                window = driver.current_window_handle
                switch_to_and_apply(driver, window, ar)
                
                    
            except Exception:
                    
                raise exceptions.ApplicationStepException('Step 3', 'Unable to complete specific questions')


        case 'Step 4 out of 10' | 'Step 3 out of 9':
                
            try:
                    
                save_and_continue = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/div/div/form/span/span[2]/span[5]/span[1]/span/span[1]/input[1]')
                save_and_continue.click()
                    
                ar = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/div/div/form/span/span[2]/span[3]/span[2]/span[1]')

                time.sleep(3)
                window = driver.current_window_handle
                switch_to_and_apply(driver, window, ar)

            except Exception:
                    
                raise exceptions.ApplicationStepException('Step 4', 'Unable to complete education')

        case 'Step 5 out of 10' | 'Step 4 out of 9':
                
            try:
                    
                save_and_continue = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/div/div/form/span/span[2]/span[5]/span[1]/span/span[1]/input[1]')
                save_and_continue.click()
                    
                ar = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/div/div/form/span/span[2]/span[3]/span[2]/span[1]')

                time.sleep(3)
                window = driver.current_window_handle
                switch_to_and_apply(driver, window, ar)
                                        
            except Exception:
                    
                raise exceptions.ApplicationStepException('Step 5', 'Unable to complete')

        case 'Step 6 out of 10' | 'Step 5 out of 9':
                
            try:
                    
                save_and_continue = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/div/div/form/span/span[2]/span[5]/span[1]/span/span[1]/input[1]')
                save_and_continue.click()
                    
                ar = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/div/div/form/span/span[2]/span[3]/span[2]/span[1]')

                time.sleep(3)
                window = driver.current_window_handle
                switch_to_and_apply(driver, window, ar)
                    
            except Exception:
                    
                raise exceptions.ApplicationStepException('Step 6', 'Unable to complete')

        case 'Step 7 out of 10' | 'Step 6 out of 9':
                
            try:
                    
                save_and_continue = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/div/div/form/span/span[2]/span[5]/span[1]/span/span[1]/input[1]')
                save_and_continue.click()
                    
                ar = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/div/div/form/span/span[2]/span[3]/span[2]/span[1]')

                time.sleep(3)
                window = driver.current_window_handle
                switch_to_and_apply(driver, window, ar)
                    
            except Exception:
                    
                raise exceptions.ApplicationStepException('Step 7', 'Unable to complete')

        case 'Step 8 out of 10' | 'Step 7 out of 9':
                
            try:
                    
                sign_signature = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/div/div/form/span/span[2]/span[4]/table/tbody/tr/td/span[4]/div[2]/span/table/tbody/tr/td/span/input')
                sign_signature.send_keys('Michael Ladderbush')
                save_and_continue = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/div/div/form/span/span[2]/span[5]/span[1]/span/span[1]/input[1]')
                save_and_continue.click()
                    
                ar = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/div/div/form/span/span[2]/span[3]/span[2]/span[1]')

                time.sleep(3)
                window = driver.current_window_handle
                switch_to_and_apply(driver, window, ar)
                
            except Exception:
                    
                raise exceptions.ApplicationStepException('Step 8', 'Unable to complete')

    
        case 'Step 9 out of 10' | 'Step 8 out of 9':
                
            try:
                    
                save_and_continue = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/div/div/form/span/span[2]/span[5]/span[1]/span/span[1]/input[1]')
                save_and_continue.click()
                    
                ar = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/div/div/form/span/span[2]/span[3]/span[2]/span[1]')

                time.sleep(3)
                window = driver.current_window_handle
                switch_to_and_apply(driver, window, ar)
                    
            except Exception:
                    
                raise exceptions.ApplicationStepException('Step 9', 'Unable to complete')
            
        case 'Step 10 out of 10' | 'Step 9 out of 9':
            try:
                    
                submit= driver.find_element(By.XPATH, '//*[@id="et-ef-content-ftf-submitCmdBottom"]')
                submit.click()
                time.sleep(3)
                driver.close()
                    
            except Exception:
                    
                raise exceptions.ApplicationStepException('Step 10', 'Unable to complete')




        