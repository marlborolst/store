'''
    unittest
    1.子类继承TestCase
    2.写用例，test开头！！！
'''
from unittest import TestCase
#from Calc import Calc
class Calc:
    def add(self,a,b):
        return a + b
    def minus(self,a,b):
        return a - b
    def multi(self,a,b):
        return a *b
    def devision(self,a,b):
        return a // b

class TestCalc(TestCase):
    def testAdd1(self):
        a = 6
        b = 5
        c = 11
        calc = Calc()
        s = calc.add(a,b)
        self.assertEqual(s,c)#断言，若s=c，返回true；若s！=c，返回false。
    def testAdd2(self):
        a = -6
        b = -5
        c = -11
        calc = Calc()
        s = calc.add(a, b)
        self.assertEqual(s, c)
    def testAdd3(self):
        a = -6
        b = 5
        c = -1
        calc = Calc()
        s = calc.add(a, b)
        self.assertEqual(s, c)
    def testAdd4(self):
        a = 6
        b = -5
        c = 1
        calc = Calc()
        s = calc.add(a, b)
        self.assertEqual(s, c)

    def testmin1(self):
        a = 6
        b = 5
        c = 1
        calc = Calc()
        s = calc.minus(a, b)
        self.assertEqual(s, c)  # 断言，若s=c，返回true；若s！=c，返回false。

    def testmin2(self):
        a = -6
        b = -5
        c = -1
        calc = Calc()
        s = calc.minus(a, b)
        self.assertEqual(s, c)

    def testmin3(self):
        a = -6
        b = 5
        c = -11
        calc = Calc()
        s = calc.minus(a, b)
        self.assertEqual(s, c)

    def testmin4(self):
        a = 6
        b = -5
        c = 11
        calc = Calc()
        s = calc.minus(a, b)
        self.assertEqual(s, c)

    def testmul1(self):
        a = 6
        b = 5
        c = 30
        calc = Calc()
        s = calc.multi(a, b)
        self.assertEqual(s, c)  # 断言，若s=c，返回true；若s！=c，返回false。

    def testmul2(self):
        a = -6
        b = -5
        c = 30
        calc = Calc()
        s = calc.multi(a, b)
        self.assertEqual(s, c)

    def testmul3(self):
        a = -6
        b = 5
        c = -30
        calc = Calc()
        s = calc.multi(a, b)
        self.assertEqual(s, c)

    def testmul4(self):
        a = 6
        b = -5
        c = -30
        calc = Calc()
        s = calc.multi(a, b)
        self.assertEqual(s, c)

    def testdev1(self):
        a = 6
        b = 2
        c = 3
        calc = Calc()
        s = calc.devision(a, b)
        self.assertEqual(s, c)  # 断言，若s=c，返回true；若s！=c，返回false。

    def testdev2(self):
        a = -6
        b = -2
        c = 3
        calc = Calc()
        s = calc.devision(a, b)
        self.assertEqual(s, c)

    def testdev3(self):
        a = -6
        b = 2
        c = -3
        calc = Calc()
        s = calc.devision(a, b)
        self.assertEqual(s, c)

    def testdev4(self):
        a = 6
        b = -3
        c = -2
        calc = Calc()
        s = calc.devision(a, b)
        self.assertEqual(s, c)














