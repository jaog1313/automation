from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("https://mcstaging.plazalama.com.do")
print(driver.title)
driver.maximize_window()
try:

    element = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.NAME, "q"))
        )
    #element.click()
    element.send_keys("test")
    element.send_keys(Keys.RETURN)
    time.sleep(5)
    print(driver.page_source)
finally:

    driver.quit()