from selenium import webdriver
from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from biao1 import rwsj
from 教师 import js
import time

p = rwsj()

@ddt
class Testlogin(TestCase):

    @data(*p.dq())
    @unpack

    def testLogin1(self, a, b, c, d):
        username = b
        pwd = c
        expect = d

        driver = webdriver.Chrome()
        driver.get("http://localhost:8081/HKR")
        driver.maximize_window()

        loginOpera = js(driver)
        loginOpera.login1(username, pwd)

        result = loginOpera.getSuccessResult()

        if expect == result:
            p.writeData(a, 4, result)
            p.writeData(a, 5, "是")
            driver.save_screenshot("js成功.png")
        else:
            p.writeData(a, 4, result)
            p.writeData(a, 5, "否")
            driver.save_screenshot("js失败.png")
        time.sleep(3)
        driver.quit()
        self.assertEqual(result, expect)