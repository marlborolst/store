import time
class lj:

    def __init__(self,driver):# 全局用的都是一个driver
        self.driver = driver

    def login(self,username,pwd):
        self.driver.find_element_by_xpath("//*[@id='loginname']").send_keys(username)
        self.driver.find_element_by_xpath("//*[@id='password']").send_keys(pwd)
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='submit']").click()
        self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/li[2]/ul/li/div/span[4]/a").click()
        time.sleep(3)

    def getSuccessResult(self):#获取登陆成功的测试依据
        return self.driver.title#浏览器标题信息


