from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://www.suning.com/")
driver.maximize_window()
try:
    driver.find_element(By.ID,"searchKeywords").send_keys("TIFFANY&CO.")#打开苏宁，输入Tiffany
    time.sleep(3)
    driver.find_element(By.ID,"searchSubmit").click()#点击搜索
    driver.find_element(By.ID,"0000000000-12280394524").click()#点击商品进入详情页
    a=driver.window_handles#获取窗口的元素
    driver.switch_to.window(a[-1])#跳入指定窗口
    driver.find_element(By.ID,"addCart").click()#点击加入购物车
except:
    driver.save_screenshot("no.png")
    print("加购失败")
else:
    driver.save_screenshot("ok.png")
    print("加购成功")
finally:
    print("谢谢选购")
time.sleep(10)
driver.quit()