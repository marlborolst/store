from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
url = "127.0.0.1:4723/wd/hub"

param = {
  "deviceName": "127.0.0.1:62001",
  "platformName": "Android",
  "platformVersion": "7.1.2",
  "appPackage": "com.sina.weibo",
  "appActivity": "com.sina.weibo.SplashActivity"
}

driver =  webdriver.Remote(url,param) #

el0 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView[3]")
el0.click()
time.sleep(15)
while True:
    time.sleep(8)
    start_x = 400
    start_y = 1300  # 滑动起点坐标
    distance = 1000  # 滑动距离
    driver.swipe(start_x, start_y, start_x, start_y - distance)