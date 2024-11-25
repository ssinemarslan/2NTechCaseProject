import pytest
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from myConstants import constants as c
from time import sleep

class Test_Searching_City():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.get(c.PORTAL_URL)
        #self.driver.get("https://2nhaber.com/")
        self.driver.maximize_window()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_searching(self):
        searching_button = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH,c.SEARCHING_BUTTON_XPATH)))
        searching_button.click()

        searching_input = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH,c.SEARCHING_INPUT_XPATH)))
        searching_input.send_keys("İstanbul")
        searching_input.send_keys(Keys.RETURN)  # Arama tuşu olmadığı için enter tuşu ile çalıştırılıyor.

        # Arama sonuçlarının yüklenmesini bekleyin
        output_list = WebDriverWait(self.driver, 5).until(
        lambda driver: driver.find_elements(By.XPATH,c.OUTPUT_LIST_XPATH))

        # Liste dolu mu kontrol edin
        assert len(output_list) > 0, "Arama sonuçlarında hiçbir haber bulunamadı!"

        # Haber numarası
        news_number = 8

        # İstenilen sıradaki habere tıklayın
        if news_number <= len(output_list):
            selected_news = output_list[news_number - 1]
            print("Seçilen haber başlığı:", selected_news.text)

            # Haber başlığını doğrulama
            expected_text = "İstanbul ile ilgili beklenen haber başlığı"  # Bu statik bir örnek
            assert expected_text in selected_news.text, f"Seçilen haber başlığı beklenenle eşleşmiyor: {selected_news.text}"

            # Habere tıklama
            selected_news.click()
        else:
            print(f"Yeterli haber bulunamadı. Toplam haber sayısı: {len(output_list)}")
