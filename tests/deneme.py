from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# WebDriver'ı başlatıyoruz (Chrome kullanılıyor)
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

try:
    # 2NHABER anasayfasına gidiyoruz
    driver.get("https://2nhaber.com/")

    # Arama butonuna tıklıyoruz
    search_button = driver.find_element(By.XPATH, '//*[@id="search-button-id"]')  # 'search-button-id' doğru xpath ile değiştirilmeli
    search_button.click()

    # Arama kutusuna "İstanbul" yazıyoruz
    search_input = driver.find_element(By.XPATH, '//*[@id="search-input-id"]')  # 'search-input-id' doğru xpath ile değiştirilmeli
    search_input.send_keys("İstanbul")
    search_input.send_keys(Keys.RETURN)

    # Sayfanın yüklenmesi için biraz bekliyoruz
    time.sleep(3)  # Yüklenmesi için süre tanıyoruz

    # 8. haberin detayına gitmek için dinamik bir yapı kuruyoruz
    news_number = 8  # Bu sayı dinamik olarak değiştirilebilir

    # Arama sonuçları sayfasındaki haberlerin linkine tıklıyoruz
    news_list = driver.find_elements(By.XPATH, '//*[@class="news-item-class"]')  # 'news-item-class' doğru xpath ile değiştirilmeli
    news_list[news_number - 1].click()  # 8. haberin detayına gitmek

    # Sayfanın yüklenmesi için bekliyoruz
    time.sleep(3)

    # Burada detaylı haber bilgilerini alabilirsiniz (isteğe bağlı)
    news_details = driver.find_element(By.XPATH, '//*[@id="news-detail-id"]')  # 'news-detail-id' doğru xpath ile değiştirilmeli
    print(news_details.text)
