import allure
from base.base_test import BaseTest

@allure.feature("Mail functionality")
class TestMail(BaseTest):

    @allure.title("send mails test")
    @allure.severity("Critical")
    def test_send_mail(self):
        self.login_page.open()
        self.login_page.enter_btn_click()
        self.login_page.switch_to_iframe()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.submit_btn_click()
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.enter_to_account()

        address_list = ["tany_27_07@mail.ru", "test"]
        mail_subject = "test subject"
        mail_body = "test mail"

        self.mail_page.open()
        for address in address_list:
            self.mail_page.wright_letter_btn_click()
            self.mail_page.enter_email(address)
            self.mail_page.enter_mail_subject(mail_subject)
            self.mail_page.enter_mail_body(mail_body)
            self.mail_page.file_upload()
            self.mail_page.send_mail_btn_click(address)
            self.mail_page.open()



