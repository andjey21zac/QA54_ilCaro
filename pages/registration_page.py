from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class RegistrationPage:
    REGISTRATION_LINK = (By.CSS_SELECTOR, "[href='/register']")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, '[name="firstName"]')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[name='lastName']")
    EMAIL_INPUT = (By.CSS_SELECTOR, '[name = "username"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[name = "password"]')
    TERM_OF_USE_CHECK_BOX = (By.ID, "terms-of-use")
    BUTTON_REGISTRATION = (By.XPATH, "//button[text()='Y'alla!']")

    def __init__(self, driver):
        self.driver = driver

    def open_registration_page(self):
        self.driver.find_element(*self.REGISTRATION_LINK).click()

    def fill_first_name_field(self, first_name):
        self.driver.find_element(*self.FIRST_NAME_INPUT).clear()
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)

    def fill_last_name_field(self, last_name):
        self.driver.find_element(*self.LAST_NAME_INPUT).clear()
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)

    def fill_email_field(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).clear()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def fill_password_field(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_registration_button(self):
        self.driver.find_element(*self.REGISTRATION_BUTTON).click()

    def click_policy(self):
        self.driver.find_element(*self.TERM_OF_USE_CHECK_BOX).click() #13*13

    # def is_sign_out_displayed(self):
    #     return self.driver.find_element(*self.SIGN_OUT_BUTTON).is_displayed()

    def is_sign_out_displayed(self):
        try:
            WebDriverWait(self.driver, timeout = 10).until(
                expected_conditions.visibility_of_element_located(self.SIGN_OUT_BUTTON)
            )
            return True
        except TimeoutException:
            return False


    def get_alert_text(self):
        alert = WebDriverWait(self.driver, timeout = 10).until(
           expected_conditions.alert_is_present()
        )
        return alert.text

    def accept_alert(self):
        self.driver.switch_to.alert.accept()