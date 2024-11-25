#Ziyaretçi 2NHABER (https://2nhaber.com/) web sitesinin anasayfasında bulunan search butonuna tıklamalı. 
#Açılan inputa “İstanbul” yazarak arama yapmalı ve çıkan sonuçların ilk sayfasındaki 8.haberin detayına gitmelidir.  
#Arama sayfasında bulunan 8.haberin bilgisi statik olarak verilmemelidir. Sadece sayıyı güncelleyerek 8 
#yerine 3.habere de gidilebilmelidir. Kanıtlama işleminde kıyaslama için haberin bilgisi statik olarak 
#tutulabilir. 

import pytest
from time import sleep
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
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.driver.get(c.PORTAL_URL)
    #self.driver.get("https://2nhaber.com/")
    self.driver.maximize_window()
    self.vars = {}

  def teardown_method(self, method):
    self.driver.quit()

  def test_searching(self):
    searching_button=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,c.SEARCHING_BUTTON_XPATH)))
    searching_button.click()
    searching_input=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,c.SEARCHING_INPUT_XPATH)))
    searching_input.send_keys("İstanbul")
    searching_input.send_keys(Keys.RETURN) #arama tuşu olmadığı için enter tuşunu bu key ile gerçekleştirildi.
    sleep(7)
    output_list=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,c.OUTPUT_LIST_XPATH)))

    news_number=8 
    # news_list=WebDriverWait(self.driver,10).until(ec.element_to_be_clickable((By.XPATH,nc.NEWS_LIST_XPATH)))
    # news_list[news_number - 1].click()

    # news_details=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,nc.NEWS_DETAILS_XPATH))) # 'news-detail-id' doğru xpath ile değiştirilmeli
    # assert news_details.text=="Aydınlatma Metni"
    assert len(output_list) > 0
    # İstenilen sıradaki habere tıklama
    if news_number <= len(output_list):
     selected_news = output_list[news_number - 1]
     print("Seçilen haber başlığı:", selected_news.text)  # Haber bilgisi kıyaslama için saklanabilir

     # Başlık doğrulama (örnek)
    expected_text = "İstanbul ile ilgili beklenen haber başlığı"  # Bu statik bir örnek
    assert expected_text in selected_news.text, f"Seçilen haber başlığı beklenenle eşleşmiyor: {selected_news.text}"