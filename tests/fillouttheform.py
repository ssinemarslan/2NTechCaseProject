#Ziyaretçi 2NTECH (https://www.2ntech.com.tr/hr) sitesinde bulunan formun 
#1.adımını eksiksiz doldurup 2.adımında “Test Engineer” pozisyonunu seçmeli ve formu başarılı bir şekilde göndermelidir. 
#Senaryo sonunda formun başarılı gönderildiği kontrol edilmeli ve kanıtlanmalıdır.
import pytest
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
from myConstants import constants_fillform as f

class Test_FillOutTheForm():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.get(f.HR_URL)
        #self.driver.get("https://2nhaber.com/")
        self.driver.maximize_window()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_theform(self):
        namesurname_box=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,f.NAMESURNAME_BOX_XPATH)))
        namesurname_box.click()
        namesurname_box.send_keys("Test Account")
        birthday_date=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,f.BIRTHDAY_DATE)))
        birthday_date.click()
        birthday_date.send_keys("20.06.1999")
        tcnobox=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,f.TCNOBOX_XPATH)))
        tcnobox.click()
        tcnobox.send_keys("12345678910")
        phonenumber_box=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,f.PHONEBOX_XPATH)))
        phonenumber_box.send_keys("05452223344")
        mailbox=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,f.MAILBOX_XPATH)))
        mailbox.send_keys("111@gmail.com")
        cv_input=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,f.CV_INPUT_XPATH)))
        cv_input.click()
        degreebuton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,f.DEGREEBOX_XPATH)))
        degreebuton.click()
        kvkkbuton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,f.KVKKTEXT_XPATH)))
        kvkkbuton.click()
        next_button=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,f.NEXT_BUTTON_XPATH)))
        next_button.click()
        testengineer=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,f.TESTENGINEER_XPATH)))
        testengineer.click()
        sendbutton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,f.SENDBUTTON_XPATH)))
        sendbutton.click()
        informationtext=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,f.INFORMATION_XPATH)))
        assert informationtext.text=="Form Başarı ile gönderildi. Katıldığınız için teşekkür ederiz."
        




