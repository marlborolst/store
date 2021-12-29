from HTMLTestRunner import  HTMLTestRunner
import  unittest
import os
#自动获取当前路径用例
tests = unittest.defaultTestLoader.discover(os.getcwd(),pattern="jiaoshi17.py")

runner = HTMLTestRunner.HTMLTestRunner(
    title = "HKR教师查询重置密码测试",
    description="测试结果",
    verbosity=1,
    stream = open(file="HKRJ.html",mode="w+",encoding="utf-8")
)

runner.run(tests)