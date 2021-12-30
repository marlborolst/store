from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
url = "127.0.0.1:4723/wd/hub"

param = {
          "platformVersion": "7.1.2",
          "platformName": "Android",
          "appPackage": "com.jingdong.app.mall",
          "appActivity": "com.jingdong.app.mall.main.MainActivity",
          "deviceName": "127.0.0.1:62001"
        }
driver =  webdriver.Remote(url,param) #

time.sleep(15)
el1 =  driver.find_element_by_id("com.jingdong.app.mall:id/bq8")
el1.click()
TouchAction(driver).tap(x=414, y=139).perform()
el2 = driver.find_element_by_id("com.jd.lib.search:id/search_text")
el2.send_keys("ysl")
el2.click()
TouchAction(driver).tap(x=35, y=207).perform()
el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout[2]/android.widget.RelativeLayout")
el3.click()
el4 = driver.find_element_by_id("com.jd.lib.productdetail:id/pd_txt_shopcar")
el4.click()


