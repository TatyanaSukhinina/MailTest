from selenium.webdriver.common.by import By
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import allure


class LoginPage(BasePage):

    PAGE_URL = Links.HOST
    ENTER_BTN = ("xpath", "//button[text() = 'Войти']")
    USERNAME_FLD = ("xpath", "//input[@name='username']")
    PASSWORD_FLD = ("xpath", "//input[@name='password']")
    SUBMIT_BTN = ("xpath", "//span[text() = 'Войти']")

    def enter_btn_click(self):
        self.wait.until(EC.element_to_be_clickable(self.ENTER_BTN)).click()

    @allure.step("Успешно введен логин")
    def enter_login(self, login):
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_FLD)).send_keys(login)

    @allure.step("Успешно введен пароль")
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FLD)).send_keys(password)

    def submit_btn_click(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BTN)).click()

    @allure.step("Успешно произведен вход в учетную запись")
    def enter_to_account(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BTN)).click()

    def switch_to_iframe(self):
        iframe = self.driver.find_element(By.XPATH, '//iframe[@class="ag-popup__frame__layout__iframe"]')
        self.driver.switch_to.frame(iframe)




