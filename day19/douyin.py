from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
url = "127.0.0.1:4723/wd/hub"

param = {
  "deviceName": "127.0.0.1:62001",
  "platformName": "Android",
  "platformVersion": "7.1.2",
  "appPackage": "com.ss.android.ugc.aweme",
  "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity"
}

driver =  webdriver.Remote(url,param) #

time.sleep(10)
el1 = driver.find_element_by_id("com.ss.android.ugc.aweme:id/bdb")
el1.click()
while True:
  TouchAction(driver).press(x=648, y=1184).move_to(x=648,y= 252).release().perform()
  time.sleep(10)