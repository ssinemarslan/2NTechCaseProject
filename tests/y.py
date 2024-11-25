from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def test_navbar_links():
    # Tarayıcıyı başlat
    driver = webdriver.Chrome()  # ChromeDriver yolunu belirtin
    driver.get("https://2nhaber.com/")
    driver.maximize_window()

    # Navbar öğelerini bulun
    navbar_items = driver.find_elements(By.CSS_SELECTOR, "nav a")  #nav a olan elementleri bul
    navbar_links = [item.get_attribute('href') for item in navbar_items if item.get_attribute('href')] #her bir a elementindeki href değerini al.
    #hrefte href="https://2nhaber.com/hakkimizda" değerini alıyoruz.ve bunları bu listeye kaydet.

    # Tüm öğeleri döngüyle tıklama ve doğrulama
    for link in navbar_links: #yukarıda yapılmış listedeki linklere git.
        try:
            driver.get(link) #linke git.
            time.sleep(2) 
            assert driver.current_url == link# ,f"URL doğru yüklenmedi: {link}" 
            print(f"Başarılı: {link}")  #Eğer driver.current_url (tarayıcının mevcut URL’si) ile link(tıklanan bağlantı)aynıysa,sayfa doğru açılmıştır.
        except Exception as e:
            print(f"Hata: {link}, {e}")
    
    # Tarayıcıyı kapat
    driver.quit()

# Test fonksiyonunu çalıştır
test_navbar_links()

#Sayfa Yönlendirmelerini Kontrol Etme: Eğer bir işlem sonucunda sayfanın doğru yere yönlendirilip 
# yönlendirilmediğini kontrol etmek isterseniz, current_url kullanabilirsiniz.
#Testlerde Doğrulama: Testlerinizde, sayfa üzerinde belirli bir eylem gerçekleştirildikten sonra, 
# kullanıcıyı doğru URL'ye yönlendirip yönlendirmediğinizi doğrulamak için kullanabilirsiniz.
#Özetle, current_url, mevcut sayfanın URL'sini dinamik olarak almak için kullanışlı bir özelliktir.

# Kod şu anda dinamik. Yani, navbar'a yeni bir bağlantı eklendiğinde kodu değiştirmenize gerek kalmaz. Çünkü:
# find_elements() ile tüm <a> etiketlerini otomatik buluyoruz.
# Bu sayede yeni eklenen bağlantılar da listeye dahil ediliyor ve kontrol ediliyor.