import time

from selenium import webdriver
from selenium.webdriver.common.by import By

username = "202010101"
password = "Software2025!"
driver = webdriver.Chrome(r"C:\Users\18298\Desktop\LoginPy\chromedriver.exe")
driver.get("https://plataformavirtual.itla.edu.do/login/index.php")
driver.maximize_window()
driver.get_screenshot_as_file("screenshot1.png")

driver.find_element(By.ID, "username").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)
driver.get_screenshot_as_file("screenshot2.png")

driver.find_element(By.CSS_SELECTOR,".btn-primary").click()
driver.get_screenshot_as_file("screenshot3.png")

time.sleep(5)

driver.quit()

