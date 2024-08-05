import pytest
from config.data import Data
from pages.login_page import LoginPage
from pages.mail_page import MailPage

class BaseTest:
    data: Data
    login_page: LoginPage
    mail_page: MailPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()
        request.cls.login_page = LoginPage(driver)
        request.cls.mail_page = MailPage(driver)
