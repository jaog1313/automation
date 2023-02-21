from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome('./chromedriver')
driver.get("https://mcstaging.plazalama.com.do")
#my_div = driver.find_element(By.ID, "dive-into-python")
#print(type(my_div))
#Esto deberia lanzar una exccepcion porque ese ID no existe
#my_div = driver.find_element(By.ID, "dive-into-javascript")
try:
    element = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, ".//*[contains(@class , 'authorization-link')]"))
        )
    print(type(element))
    WebDriverWait(driver, 3)
    element.click()
    

except TimeoutException as ex:
    print("Han pasado 84 años y no encontramos ese elemento " + str(ex))

driver.close()