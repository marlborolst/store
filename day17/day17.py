from selenium import webdriver
from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from rwsj import rwsj
from lj import lj
from 教师 import js
import time
p=rwsj()

@ddt
class Testlogin(TestCase):

    @data(*p.dq())
    @unpack
    def testLogin(self,a,b,c,d):
        username = b
        pwd  = c
        expect = d

        driver = webdriver.Chrome()
        driver.get("http://localhost:8081/HKR")
        driver.maximize_window()

        loginOpera = lj(driver)
        loginOpera.login(username,pwd)

        result = loginOpera.getSuccessResult()

        if expect == result:
            p.writeData(a, 4, result)
            p.writeData(a, 5, "是")
            driver.save_screenshot("s成功.png")
        else:
            p.writeData(a, 4, result)
            p.writeData(a, 5, "否")
            driver.save_screenshot("s失败.png")
        time.sleep(3)
        driver.quit()
        self.assertEqual(result, expect)
