import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


class Examples_automation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        #self.driver = webdriver.Chrome('./chromedriver')
    def test_plazalama(self):
        driver = self.driver
        driver.get("https://mcstaging.plazalama.com.do")
        print(driver.title)
        driver.maximize_window()
        try:

            element = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.NAME, "q"))
                )
            """
            element = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, ".//*[contains(@class , 'subcategory-title')]"))
                )
            """
            #element.click()
            element.send_keys("test")
            element.send_keys(Keys.RETURN)
            time.sleep(5)
            print(driver.page_source)
        except:
            print("Sucedió un problema")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

            