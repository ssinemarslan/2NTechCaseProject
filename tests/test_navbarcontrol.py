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

#Ziyaretçi 2NHABER (https://2nhaber.com/) web sitesindeki bütün navbar elementlerine tıklayabilmeli 
#ve sayfalar sorunsuz açılmalı. 
#Navbar senaryosu dinamik yapıda olmalı, navbara yeni bir element eklendiğinde otomasyonu güncellemek zorunda kalmamalıyız.
# Kontrol döngü halinde, tek metot içinde tıklama ve kanıtlama işlemleri yapılmalıdır.

class Test_Navbar():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.get(c.PORTAL_URL)
        #self.driver.get("https://2nhaber.com/")
        self.driver.maximize_window()
        self.vars = {}

    def teardown_method(self, method):
      self.driver.quit()

    def test_navbar_link(self):
        #navbar_items = driver.find_elements(By.CSS_SELECTOR, "nav a")
        #nav a olan elementi bul.
        navbar_items = WebDriverWait(self.driver,5).until(ec.presence_of_all_elements_located((By.CSS_SELECTOR,c.NAVBAR_LINKS_CSS_SELECTOR)))
        #navbar_items = WebDriverWait(self.driver,10).until(ec.presence_of_all_elements_located((By.XPATH,nc.NAVBAR_LINKS_XPATH)))
        
        #her bir a elementindeki href değerini al.
        # ve hrefte href="https://2nhaber.com/hakkimizda" değerini alıyoruz.ve bunları bu listeye kaydet.
        navbar_links = [item.get_attribute('href') 
                        for item in navbar_items 
                            if item.get_attribute('href')]
        #for item in navbar_items: navbar_items listesindeki her bir öğeyi sırayla işler.
        #item.get_attribute('href'): Her öğenin href (bağlantı URL'si) özelliğini alır.
        #if item.get_attribute('href'): Sadece href değeri boş olmayan öğeleri işler.
        #Sonuç: href değerlerini bir listeye toplar.


    # Tüm öğeleri döngüyle tıklama ve doğrulama
        for link in navbar_links:#yukarıda yapılmış listedeki linklere git.
            if link:  # Eğer bağlantı boş değilse
                self.driver.get(link) #burada tıklama sağlandı click kullanılmasada.
                sleep(5)
                if self.driver.current_url == link:  # Açılan sayfanın URL'sini kontrol et
                    print(f"Başarılı: {link}") #Eğer driver.current_url (tarayıcının mevcut URL’si) ile link(tıklanan bağlantı)aynıysa,sayfa doğru açılmıştır.
                else:
                    print(f"URL yanlış yüklendi: {link}")
            else:
                print("Boş bir bağlantı algılandı, atlanıyor.")

# if self.driver.current_url == link:
# self.driver.current_url: Tarayıcının o anda açtığı sayfanın URL’sini döndürür.
# link: Tıklanan bağlantıdır.
# Karşılaştırma yapılarak, açılan sayfanın URL’sinin beklenen bağlantıyla aynı olup olmadığı kontrol edilir.

# burada "tıklama" işlemi gerçekleştirilmedi. Kodda bağlantılara doğrudan tarayıcıyı yönlendirme işlemi yapılıyor, 
# yani self.driver.get(link) komutuyla tarayıcı verilen link URL'sine gidiyor. 
# Bu işlem, bağlantıyı tıklamak yerine tarayıcıyı manuel olarak o adrese götürmek gibidir.

#Sayfa Yönlendirmelerini Kontrol Etme: Eğer bir işlem sonucunda sayfanın doğru yere yönlendirilip 
# yönlendirilmediğini kontrol etmek isterseniz, current_url kullanabilirsiniz.
#Testlerde Doğrulama: Testlerinizde, sayfa üzerinde belirli bir eylem gerçekleştirildikten sonra, 
# kullanıcıyı doğru URL'ye yönlendirip yönlendirmediğinizi doğrulamak için kullanabilirsiniz.
#Özetle, current_url, mevcut sayfanın URL'sini dinamik olarak almak için kullanışlı bir özelliktir.

# Kod şu anda dinamik. Yani, navbar'a yeni bir bağlantı eklendiğinde kodu değiştirmenize gerek kalmaz. Çünkü:
# find_elements() ile tüm <a> etiketlerini otomatik buluyoruz.
# Bu sayede yeni eklenen bağlantılar da listeye dahil ediliyor ve kontrol ediliyor.

#presence_of_all_elements_located kullanarak navbar elementlerinin alt seçeneklerine de tıklayarak doğrulama sağladı.
#visibilite_any_element_located 

#Bir butonun alt menülerine tıklamak için element_to_be_clickable 
# veya visibility_of_element_located kullanılabilir.Ama alt menülerdeki öğelere tıklamak için, 
# öğenin görünebilir olması ve tıklanabilir olması gerekmektedir.
#visibility_of_any_elements_located kullandığımda da sadece navbar elementlerine tıkladı.Alt elementlere tıklamadı.


                






