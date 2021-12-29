import time
class js:

    def __init__(self,driver):# 全局用的都是一个driver
        self.driver = driver

    def login1(self,username,pwd):
        self.driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/a[2]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='loginname']").send_keys(username)
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='password']").send_keys(pwd)
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='submit']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/li[1]/ul/li[1]/div/span[4]/a").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='sear_teaname']").send_keys("贾")
        time.sleep(3)
        self.driver.find_element_by_xpath(
            "/html/body/div[4]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div/div[1]/table/tbody/tr/td[2]/a/span/span[1]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath(
            "/html/body/div[4]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div/div[2]/div[2]/div[2]/table/tbody/tr/td[9]/div/a").click()

        self.driver.switch_to.alert.accept()#点击确定
        time.sleep(3)#强制等待

    def getSuccessResult(self):#获取登陆成功的测试依据
        return self.driver.title#浏览器标题信息
