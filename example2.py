from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome('./chromedriver')
driver.get("https://mcstaging.purdyenlinea.com")
driver.maximize_window()
#driver.manage.window.maximize()
#my_div = driver.find_element(By.ID, "dive-into-python")
#print(type(my_div))
#Esto deberia lanzar una exccepcion porque ese ID no existe
#my_div = driver.find_element(By.ID, "dive-into-javascript")
try:
    """"
    mi_lista = driver.find_elements(By.XPATH, ".//*[contains(@class , 'authorization-link')]")
    for e in mi_lista:
        print(e)
    """
    #driver.find_element(By.XPATH, ".//*[contains(@class , 'authorization-link')]//a[not(@class)]").click()
    """"
    element = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, ".//*[contains(@class , 'authorization-link')]"))
        )
    """
    """"
    element = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, ".//*[contains(@class , 'logo')]"))
        )
    """

    element = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, ".//*[text()contains(. ,'Iniciar')]"))
        )
    #element = driver.find_element(By.XPATH, ".//*[text()contains(text(),'Iniciar')]")
    #element.click()
    print(type(element))
    
    WebDriverWait(driver, 3)
    element.click()
    #element.click()

finally:
    driver.quit()
    
""""
except TimeoutException as ex:
    print("Han pasado 84 años y no encontramos ese elemento " + str(ex))

"""

#driver.close()