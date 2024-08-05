import time
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import allure
import pytest_check as check


class MailPage(BasePage):
    PAGE_URL = Links.MAIL_PAGE_LINK
    WRIGHT_LETTER_BTN = ("xpath", "//span[text()='Написать письмо']")
    PERSON_FLD = ("xpath", "//div[@data-type='to']//div[contains(@class, 'inputContainer')]/input")
    MAIL_SUBJECT_FLD = ("xpath", "//div[contains(@class, 'inputContainer')]//input[@name='Subject']")
    SEND_MAIL_BTN = ("xpath", "//span[contains(@class, 'vkuiButton__in')]//span[text() = 'Отправить']")
    ERROR_MASSAGE = ("xpath", "//h3[text() = 'Присутствуют некорректные адреса']")
    UPLOAD_ELEMENT = ("xpath", "//button[@tabindex='500']//input[@type='file']")
    MAIL_BODY_FLD = ("xpath", "//div[@role='textbox']/div[1]")

    def wright_letter_btn_click(self):
        self.wait.until(EC.element_to_be_clickable(self.WRIGHT_LETTER_BTN)).click()

    def enter_email(self, email: str):
        self.wait.until(EC.element_to_be_clickable(self.PERSON_FLD)).send_keys(email)

    def enter_mail_subject(self, subject: str):
        self.wait.until(EC.element_to_be_clickable(self.MAIL_SUBJECT_FLD)).send_keys(subject)

    def file_upload(self):
        file_path = r'C:/Users/User/Desktop'
        upload_element = self.driver.find_element(By.XPATH, "//button[@tabindex='500']//input[@type='file']")
        upload_element.send_keys(file_path)

    def enter_mail_body(self, body):
        self.wait.until(EC.element_to_be_clickable(self.MAIL_BODY_FLD)).send_keys(body)


    @allure.step("Отправка письма")
    def send_mail_btn_click(self, email: str):
        self.wait.until(EC.element_to_be_clickable(self.SEND_MAIL_BTN)).click()
        check.equal((len(self.driver.find_elements(By.XPATH, "//h3[text() = 'Присутствуют некорректные адреса']"))), 0, f"Aдресс {email} некорректен")
        time.sleep(3)

    def page_refresh(self):
        self.driver.refresh()

