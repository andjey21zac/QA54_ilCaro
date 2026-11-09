from pages.registration_page import RegistrationPage

VALID_EMAIL = "test123@gg.com"
INVALID_EMAIL = "test1gg.com"
REGISTERED_EMAIL = "test1@gg.com"
VALID_PASSWORD = "Aa_1234!"
INVALID_PASSWORD = "Aa1234"

def test_valid_registration_success(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_registration_page()
    registration_page.fill_email_field(VALID_EMAIL)
    registration_page.fill_password_field(VALID_PASSWORD)
    registration_page.click_registration_button()
    assert registration_page.is_sign_out_displayed()

def test_with_invalid_email(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_registration_page()
    registration_page.fill_email_field(INVALID_EMAIL)
    registration_page.fill_password_field(VALID_PASSWORD)
    registration_page.click_registration_button()
    assert "Wrong email or password" in registration_page.get_alert_text()  #contains
    registration_page.accept_alert()

def test_with_valid_email_and_invalid_password(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_registration_page()
    registration_page.fill_email_field(VALID_EMAIL)
    registration_page.fill_password_field(INVALID_PASSWORD)
    registration_page.click_registration_button()
    assert "Wrong email or password" in registration_page.get_alert_text()
    registration_page.accept_alert()

def test_login_registered_user(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_registration_page()
    registration_page.fill_email_field(REGISTERED_EMAIL)
    registration_page.fill_password_field(VALID_PASSWORD)
    registration_page.click_registration_button()
    assert registration_page.get_alert_text() == "User already exist"
    registration_page.accept_alert()