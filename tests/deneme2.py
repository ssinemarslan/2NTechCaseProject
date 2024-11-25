import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from myConstants import constants as c

class Test_Searching_City():

    def setup_method(self,method):
        self.driver=webdriver.Chrome()
        self.driver.get(c.PORTAL_URL)
        self.driver.maximize_window()
        self.vars = {}

    def teardown_method(self, method):
      self.driver.quit()

def test_searching(self):
    # Arama butonunun görünür olmasını bekleyin ve tıklayın
    searching_button = WebDriverWait(self.driver, 5).until(
        ec.visibility_of_element_located((By.XPATH, c.SEARCHING_BUTTON_XPATH))
    )
    searching_button.click()
    
    # Arama giriş alanının görünür olmasını bekleyin ve arama terimini yazın
    searching_input = WebDriverWait(self.driver, 5).until(
        ec.visibility_of_element_located((By.XPATH, c.SEARCHING_INPUT_XPATH))
    )
    searching_input.send_keys("İstanbul")
    searching_input.send_keys(Keys.RETURN)  # Arama tuşu yok, Enter tuşunu simüle ediyoruz
    
    # Haber listelerinin görünür olmasını bekleyin
    news_list = WebDriverWait(self.driver, 5).until(
        ec.presence_of_all_elements_located((By.XPATH, c.NEWS_LIST_XPATH))
    )
    
    # Belirli bir haber öğesini indeksle seçin (dikkat: 0 tabanlı indeksleme)
    news_number = 8
    news_list[news_number - 1].click()  # 8. haber (7. indeks) öğesine tıklayın
