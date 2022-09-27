from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class Form:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def fill_form(self, form_link, property_address, property_price, property_link):
        self.driver.get(form_link)
        address = self.driver.find_element(
            By.XPATH,
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
        )
        address.send_keys(property_address)
        price = self.driver.find_element(
            By.XPATH,
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
        )
        price.send_keys(property_price)
        link = self.driver.find_element(
            By.XPATH,
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
        )
        link.send_keys(property_link)
        submit_btn = self.driver.find_element(
            By.XPATH,
            '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'
        )
        submit_btn.click()

    def quit_browser(self):
        self.driver.quit()

