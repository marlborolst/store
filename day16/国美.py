from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains#事件链
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://www.gome.com.cn/")
driver.maximize_window()
try:
    ac = ActionChains(driver)  # 把driver交给事件链执行
    ab=driver.find_element(By.XPATH,"//*[@id='lisnav']/li[9]/h3/a[1]")
    ac.move_to_element(ab).perform()  # 悬浮在左侧列表食品酒水栏。move_to_element移到设置的元素,ab上面定位到的设置.然后执行操作
    time.sleep(3)
    driver.find_element(By.XPATH,"/html/body/div[4]/div/div[1]/div/div[2]/div/div[9]/div[1]/div[2]/div[4]/ul/div[2]/a[2]").click()#点击洋酒
    a=driver.window_handles#获取窗口的元素
    driver.switch_to.window(a[-1])#跳入指定窗口
    ad=driver.find_element(By.XPATH,"//*[@id='gm-9140335721-1131086616']")#悬浮在商品上
    time.sleep(3)
    ac.move_to_element(ad).perform()
    driver.find_element(By.XPATH,"//*[@id='gm-9140335721-1131086616']/div/div/p[6]/a").click()#点击加入购物车
except:
    driver.save_screenshot("no.png")
    print("加购失败")
else:
    a = driver.window_handles  # 获取窗口的元素
    driver.switch_to.window(a[-1])  # 跳入指定窗口
    time.sleep(3)
    driver.save_screenshot("ok.png")
    print("加购成功")
finally:
    print("谢谢选购")
time.sleep(10)
driver.quit()