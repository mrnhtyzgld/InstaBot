from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import InstaBotExceptions


# INFO add "wait key generate" & "wait key activate" threaded functions
# INFO will be useful when opening instagram: activate the func, open insta, then wait the func to finish

class Waiting:
    def __init__(self, driver):
        self.driver = driver


    def wait_sec(self, seconds):
        self.driver.implicitly_wait(seconds)

    def wait_main_page(self):
        pass

    # waits for the whole page to reload
    #recommended to use wait_main_page etc when can because by the time this finishes this might not load some js stuff.
    def wait_refresh(self, timeout):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(lambda driver: driver.execute_script("return document.readyState;") != "complete")
            wait.until(lambda driver: driver.execute_script("return document.readyState;") == "complete")
        except TimeoutException:
            raise InstaBotExceptions.TimeOut("wait_refresh: function got timed out!")

    #this function also returns the element
    def wait_xpath_appearance(self, xpath, needs_to_be_visible=True, needs_to_be_clickable=True, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
            if needs_to_be_visible:
                element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
            if needs_to_be_clickable:
                element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

        except TimeoutException:
            raise InstaBotExceptions.TimeOut("wait_xpath_appearance: function got timed out!")

        return element

    # NOTE: returns ( invisible || does not exists in DOM )
    def wait_xpath_disappearance(self, xpath, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)  # 10 saniye kadar bekleyebilir
            result = wait.until(EC.invisibility_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            raise InstaBotExceptions.TimeOut("wait_xpath_disappearance: function got timed out!")



