#查询所有好友
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://localhost:8081/HKR")
driver.maximize_window()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='loginname']").send_keys("troyesivan")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='password']").send_keys("1234567")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='submit']").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/li[2]/ul/li/div/span[4]/a").click()
time.sleep(3)
driver.quit()
