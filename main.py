import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

import InstaBotExceptions
import Waiting

# ayraçlar: INFO NOTE TODO

##
## waiting yazıldı ve main başlandı exception sınıfı yazıldı, sırada mainin algoritma tasarımı ve threadable Waiting var.
##gptnin son promptu threadable hakkında fikir veriyor
##

# INFO github kodun server izni almadan çalışamamasını sağla sada server açık değilken
# INFO try except ile robust yap kodunu
# INFO bilgileri kaydetme gibi popupların çıkmasına yönelik cookie çözümü bulabiliriz. ama her türlü ilk proje ilk yürütüldüğünde handle etmesi gerekecek
class InstaBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        #self.debug_mode = True

        service = Service(executable_path="geckodriver.exe")
        self.driver = webdriver.Firefox(service=service)
        #self.driver.maximize_window()

        self.driver.get("https://www.instagram.com")
        self.driver.implicitly_wait(3)  # TODO change this

        self.waitHandler = Waiting.Waiting(self.driver)

        user = self.driver.find_element(By.XPATH, '//input[@aria-label="Telefon numarası, kullanıcı adı veya e-posta"]')
        pasw = self.driver.find_element(By.XPATH, '//input[@aria-label="Şifre"]')

        user.send_keys(self.username)
        pasw.send_keys(self.password)

        login_button = self.driver.find_element(By.XPATH, "//button[contains(., 'Giriş yap')]")
        login_button.click()

        self.waitHandler.wait_refresh(30)
        self.password_save()
        self.notifications(12)

        #
        #
        #





    def password_save(self):
        #Giriş bilgilerin kaydedilsin mi?
        #Not now
        #Şimdi değil, Bilgileri kaydet
        try:
            button = self.driver.find_element(By.XPATH, "//button[contains(., 'Bilgileri kaydet')]")
            button.click()
        except:
            print("unsuccesful login info popup")


    def notifications(self, timeout):
        try:
            self.waitHandler.wait_xpath_appearance("//*[contains(., 'Bildirimleri Aç')]", needs_to_be_visible=True, needs_to_be_clickable=True)
            button = self.driver.find_element(By.XPATH, "//button[contains(., 'Şimdi Değil')]")
            # button is in DOM and visible and clickable

            button.click()
        except:
            print("unsuccesful notifications info popup")


    def __quit(self):
        self.driver.quit()



    # driver.find_elements()
    # NoSuchElementException atar

    # driver.find_element()

if __name__ == "__main__":
    import os

    username = os.getenv("InstaBot_Username")
    password = os.getenv("InstaBot_Password")
    newBot = InstaBot(username, password)