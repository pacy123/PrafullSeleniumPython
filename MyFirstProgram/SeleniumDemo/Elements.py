import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.maximize_window()
print("Title: ", driver.title)
print("Url: ",driver.current_url)

#selenium Attributes - Id, Name, css Selector, Xpath, type
driver.find_element(By.NAME,"name").send_keys("Prafull")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("1234")
driver.find_element(By.ID, "exampleCheck1").click()

#driver.find_element(By.CSS_SELECTOR, "input[class='btn btn-success']").click()
#xpath, and csselector
#xpath  = //tagname[@attribute='value']
#CSS = tagname[attribute='value']
#driver.find_element(By.CSS_SELECTOR, "input[value='option1']")

driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()
driver.find_element(By.XPATH, "//input[@class='btn btn-success']").click()
message = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
print("AlertMessage is: ",message)

assert "Success" in message

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Name")

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
# id is also css  and . for classname













time.sleep(4)