import random
import uuid

from models.user import User

from pages.registration_page import  RegistrationPage


def test_valid_registration_success(driver):
    registration_page = RegistrationPage(driver)
    #random_suffix = random.randint(1,1000_000)
    random_suffix = uuid.uuid4()
    user = User("Andrey",
            "Kotik",
                f"Qwer{random_suffix}10@gm.com",
                "Aa_12345$")

    registration_page.open_registration_page()
    registration_page.fill_registration_form(user)
    assert registration_page.confirmation1() == "Registered"
    assert registration_page.confirmation2() == "You are logged in success"
    registration_page.close_window()


def test_invalid_registration_with_empty_name(driver):
    registration_page = RegistrationPage(driver)
    user = User("",
            "Kotik",
                "Qwer10@gm.com",
                "Aa_12345$")


    registration_page.open_registration_page()
    registration_page.fill_registration_form(user)
    assert registration_page.error_message_text() == "Name is required"
    assert registration_page.submit_button_disabled()










