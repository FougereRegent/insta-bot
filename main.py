import names
from typing import NoReturn
from selenium import webdriver
from selenium.webdriver.common.by import By
from google_models import HomePage, LoginPage

CONST_INSTAGRAM_URL: str = ""

def main() -> NoReturn:
    driver = webdriver.Firefox()
    homePage = HomePage(driver)
    loginPage = LoginPage(driver)
    homePage.AcceptCookie()
    homePage.ConnectButton()
    loginPage.CreateAccount()
    pass

if __name__ == "__main__":
    main()
