import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    def open(self):
        with allure.step(f"Успешно открыта страница {self.PAGE_URL} "):
            self.driver.get(self.PAGE_URL)

    def is_opened(self):
        with allure.step(f"Open {self.PAGE_URL} page"):
            self.wait.until(EC.url_to_be(self.PAGE_URL))

