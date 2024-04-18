
from turtle import position
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import exceptions
import time



def set_filters_mass_t(driver):
    
    try:
        
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
    


def get_jobs_mass_t(driver):
    
    try:
        
        position_elements = driver.find_elements(By.XPATH, '//li/div[2]/div[1]/span[1]/a')
        status_elements = driver.find_elements(By.XPATH, '//li/div[3]/a')
        complete_elements = zip(position_elements, status_elements)

    except Exception:
        
        raise exceptions.GetJobsException
        
    else:
        
        for title, status in complete_elements:
            
            if("Software" in title.text or "Developer" in title.text or "Data" in title.text or "Analyst" in title.text):
                
                if("Finish Draft Submission" in status.text or "Apply" in status.text):
                    
                    title.send_keys(Keys.CONTROL + Keys.RETURN)
                    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.TAB)

        
    next = driver.find_element(By.XPATH, '//*[@id="next"]')

    next_available = next.get_attribute("aria-disabled")
    
    if next_available ==  "false":

        next.click()
        
        time.sleep(2)
        
        get_jobs_mass_t(driver)
        


def mass_T_switch_and_apply(driver, window, *args):
    
    driver._switch_to.window(window)
    time.sleep(2)
    
    if args:
        for ar in args:
            application_step_text = ar.text
        
    else:
        try:
            
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
                mass_T_switch_and_apply(driver, window, ar)
                    
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
                mass_T_switch_and_apply(driver, window, ar)

            except Exception:
                    
                raise exceptions.ApplicationStepException('Step 2', 'Unable to complete general questions')
    
        case 'Step 3 out of 10':
                
            try:
                    
                break_down_questions(driver)
                save_and_continue = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/div/div/form/span/span[2]/span[5]/span[1]/span/span[1]/input[1]')
                save_and_continue.click()
                
                ar = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/div/div/form/span/span[2]/span[3]/span[2]/span[1]')
                    
                time.sleep(3)
                window = driver.current_window_handle
                mass_T_switch_and_apply(driver, window, ar)
                
                    
            except Exception:
                    
                raise exceptions.ApplicationStepException('Step 3', 'Unable to complete specific questions')


        case 'Step 4 out of 10' | 'Step 3 out of 9':
                
            try:
                    
                save_and_continue = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/div/div/form/span/span[2]/span[5]/span[1]/span/span[1]/input[1]')
                save_and_continue.click()
                    
                ar = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/div/div/form/span/span[2]/span[3]/span[2]/span[1]')

                time.sleep(3)
                window = driver.current_window_handle
                mass_T_switch_and_apply(driver, window, ar)

            except Exception:
                    
                raise exceptions.ApplicationStepException('Step 4', 'Unable to complete education')

        case 'Step 5 out of 10' | 'Step 4 out of 9':
                
            try:
                    
                save_and_continue = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/div/div/form/span/span[2]/span[5]/span[1]/span/span[1]/input[1]')
                save_and_continue.click()
                    
                ar = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/div/div/form/span/span[2]/span[3]/span[2]/span[1]')

                time.sleep(3)
                window = driver.current_window_handle
                mass_T_switch_and_apply(driver, window, ar)
                                        
            except Exception:
                    
                raise exceptions.ApplicationStepException('Step 5', 'Unable to complete')

        case 'Step 6 out of 10' | 'Step 5 out of 9':
                
            try:
                    
                save_and_continue = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/div/div/form/span/span[2]/span[5]/span[1]/span/span[1]/input[1]')
                save_and_continue.click()
                    
                ar = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/div/div/form/span/span[2]/span[3]/span[2]/span[1]')

                time.sleep(3)
                window = driver.current_window_handle
                mass_T_switch_and_apply(driver, window, ar)
                    
            except Exception:
                    
                raise exceptions.ApplicationStepException('Step 6', 'Unable to complete')

        case 'Step 7 out of 10' | 'Step 6 out of 9':
                
            try:
                    
                save_and_continue = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/div/div/form/span/span[2]/span[5]/span[1]/span/span[1]/input[1]')
                save_and_continue.click()
                    
                ar = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/div/div/form/span/span[2]/span[3]/span[2]/span[1]')

                time.sleep(3)
                window = driver.current_window_handle
                mass_T_switch_and_apply(driver, window, ar)
                    
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
                mass_T_switch_and_apply(driver, window, ar)
                
            except Exception:
                    
                raise exceptions.ApplicationStepException('Step 8', 'Unable to complete')

    
        case 'Step 9 out of 10' | 'Step 8 out of 9':
                
            try:
                    
                save_and_continue = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/div/div/form/span/span[2]/span[5]/span[1]/span/span[1]/input[1]')
                save_and_continue.click()
                    
                ar = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/div/div/form/span/span[2]/span[3]/span[2]/span[1]')

                time.sleep(3)
                window = driver.current_window_handle
                mass_T_switch_and_apply(driver, window, ar)
                    
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
    
    
        
def break_down_questions(driver):
    
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
                    