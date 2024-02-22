from selenium import webdriver
from selenium.webdriver.common.by import By

CONST_GOOGLE_URL: str = "https://www.google.fr/"
class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(CONST_GOOGLE_URL)
        pass

    def AcceptCookie(self):
        self.driver.implicitly_wait(0.5)
        cookie_button = self.driver.find_element(by=By.ID, value="L2AGLb")
        cookie_button.click()
        pass

    def ConnectButton(self):
        connect_button = self.driver.find_element(by=By.CSS_SELECTOR, value=".gb_Ba")
        connect_button.click()
        personal_usage_button = self.driver.find_element(by=By.CSS_SELECTOR, value=".G3hhxb")
        print(personal_usage_button)


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        pass

    def CreateAccount(self):
        create_account_button = self.driver.find_element(by=By.CSS_SELECTOR, value=".VfPpkd-LgbsSe")
        create_account_button.click()
        pass
    pass
