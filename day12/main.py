import unittest
from HTMLTestRunner import HTMLTestRunner # 测试运行器，就能生成测试报告
# 1.加载5条用例
tests = unittest.defaultTestLoader.discover(r"D:\python\day12\代码",pattern="Test*.py")
# 2.创建运行器 D:\python\day12\代码
runner = HTMLTestRunner.HTMLTestRunner(
    title = "这是计算器的测试报告",
    description="lstの计算器测试报告",
    verbosity=1,
    stream = open(file="计算器.html",mode="w+",encoding="utf-8")
)

# 3.运行
runner.run(tests)
#4.自动化发送邮件，把测试报告当成附件
# 温馨提示：用户名，密码是授权码，去你们163开启smtp授权码
