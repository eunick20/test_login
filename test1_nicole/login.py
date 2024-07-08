# script.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from config import Config

# No primeiro passo abrimos o navegador e maximizamos a tela
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.maximize_window()

# Busca URL
driver.get(Config.BASE_URL)

# Inserir dados válidos para fazer o login
driver.find_element(By.ID, "user-name").send_keys(Config.USERNAME)
driver.find_element(By.ID, "password").send_keys(Config.PASSWORD)
driver.find_element(By.ID, "login-button").click()

# Usamos assert para validar se o login foi bem-sucedido buscando um elemento no menu
assert driver.find_element(By.XPATH, "//div[@class='inventory_item_name'][contains(text(),'Sauce Labs Backpack')]").is_displayed()

# Aguardar antes de finalizar o script
time.sleep(3)

#chromedriver fecha o navegador automaticamente