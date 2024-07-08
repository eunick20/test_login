# script.py
#importando os módulos necessário do Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from config import Config

#iniciando o teste abrindo o navegador e maximizando a tela
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.maximize_window()

# usamos .get para fazer uma busca na url
driver.get('https://www.saucedemo.com/v1/')

# usamos find_element para encontrar um elemento no HTML e send_keys para preencher os campos
driver.find_element(By.ID, "user-name").send_keys(Config.USERNAME)
driver.find_element(By.ID, "password").send_keys(Config.PASSWORD)
driver.find_element(By.ID, "login-button").click()

# Verificar se o login foi bem-sucedido usando assert is displayed
assert driver.find_element(By.XPATH, "//div[@class='inventory_item_name'][contains(.,'Sauce Labs Backpack')]").is_displayed()

# Clicar em adicionar ao carrinho
driver.find_element(By.XPATH, "(//button[contains(.,'ADD TO CART')])[1]").click()

# Ir para o carrinho
driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container > a > svg").click()

# Clicar em CHECKOUT
driver.find_element(By.XPATH, "//a[@class='btn_action checkout_button'][contains(.,'CHECKOUT')]").click()

# Preencher com dados do cliente
driver.find_element(By.ID, "first-name").send_keys(Config.FIRST_NAME)
driver.find_element(By.ID, "last-name").send_keys(Config.LAST_NAME)
driver.find_element(By.ID, "postal-code").send_keys(Config.POSTAL_CODE)
driver.find_element(By.XPATH, "//input[contains(@class,'btn_primary cart_button')]").click()

# Verificar dados e finalizar a compra
driver.find_element(By.XPATH, "//a[@class='btn_action cart_button'][contains(.,'FINISH')]").click()

# Verificando se a compra foi realizada buscando um elemento no final da compra
assert driver.find_element(By.XPATH, "//h2[@class='complete-header'][contains(.,'THANK YOU FOR YOUR ORDER')]").is_displayed()

# Aguardar um tempo antes de fechar o navegador
time.sleep(3)

#chromedriver fecha o navegador automaticamente