import pytest
from selenium.webdriver.common.by import By
from unittest.mock import Mock, patch
from utils import sign_in

exceptions = Mock()

@pytest.fixture(scope="module")
def driver():
    driver = Mock()
    yield driver

def test_sign_in(driver):
    mock_find_element = driver.find_element = Mock()
    mock_click = Mock()
    mock_send_keys = Mock()

    # Mocking find_element to return a mock object for each call
    mock_find_element.side_effect = [
        mock_click,  # Mock for sign_in
        mock_click,  # Mock for accept_terms
        mock_send_keys,  # Mock for user_name
        mock_send_keys,  # Mock for password
        mock_click   # Mock for login_button
    ]

    sign_in(driver)

    # Assertions to check if find_element was called with correct XPATHs
    mock_find_element.assert_any_call(By.XPATH, '//*[text()="Sign In"]')
    mock_find_element.assert_any_call(By.XPATH, '//*[@id="dialogTemplate-dialogForm-StatementBeforeAuthentificationContent-ContinueButton"]')
    mock_find_element.assert_any_call(By.XPATH, '//*[@id="dialogTemplate-dialogForm-login-name1"]')
    mock_find_element.assert_any_call(By.XPATH, '//*[@id="dialogTemplate-dialogForm-login-password"]')
    mock_find_element.assert_any_call(By.XPATH, '//*[@id="dialogTemplate-dialogForm-login-defaultCmd"]')

    # Assertions to check if click and send_keys were called
    mock_click.assert_called()
    mock_click.assert_called_with()
    mock_send_keys.assert_called_with('Michael123')
    mock_send_keys.assert_called_with('Applesauce1%')
