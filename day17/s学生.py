from HTMLTestRunner import  HTMLTestRunner
import  unittest
import os
#自动获取当前路径用例
tests = unittest.defaultTestLoader.discover(os.getcwd(),pattern="day17.py")

runner = HTMLTestRunner.HTMLTestRunner(
    title = "HKR学生查询所有好友测试",
    description="测试结果",
    verbosity=1,
    stream = open(file="HKRS.html",mode="w+",encoding="utf-8")
)

runner.run(tests)