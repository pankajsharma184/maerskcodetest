from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from main.Elements import Elements as EL
from webdrivermanager import ChromeDriverManager

class SeleniumFunctions:

    def __init__(self,time):
        self.time = time

    def launch_browser(self):
        chrome = ChromeDriverManager()
        chrome.download_and_install()
        self.driver = webdriver.Chrome()
        self.driver.get(EL.Url)
        self.driver.implicitly_wait(2)

    def browser_actions(self):
        self.driver.find_element(By.ID, EL.Text_Box).send_keys(self.time)
        self.driver.find_element(By.XPATH,EL.start_button).click()

    def browser_first_wait(self):
        try:
            WebDriverWait(self.driver, self.time).until(EC.presence_of_element_located((By.XPATH, EL.first_wait_element)))
        except TimeoutException:
            print("The Element you are tracking is not present on the Page Source, Please debug the code and look into selenium wait time")

    def browser_second_wait(self):
        try:
            WebDriverWait(self.driver, self.time).until(
                EC.presence_of_element_located((By.XPATH, EL.second_wait_element)))
        except TimeoutException:
            print(
                "The Element you are tracking is not present on the Page Source, Please debug the code and look into selenium wait time")

    def close_browser(self):
        self.driver.quit()

