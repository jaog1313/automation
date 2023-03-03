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
        #self.driver = webdriver.Chrome()
        #self.driver = webdriver.Chrome('./chromedriver')
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)
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
            element2 = WebDriverWait(driver, 3).until(
                EC.presence_of_all_elements_located((By.XPATH, ".//*[contains(@class , 'subcategory-title')]"))
                )
            """
            
            
            #element.click()
            element.send_keys("test")
            element.send_keys(Keys.RETURN)
            #print(element2.text)
            time.sleep(5)
            self.assertNotIn("no ha dado resultados", driver.page_source)

            #print(driver.page_source)
        except:
            print("Sucedió un problema")
            
        
        
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

            