#!/usr/local/python
from unittest import TestCase

def func(num):
    return num + 1

def setup():
    print("执行setup函数")


def teardown():
    print("执行teardown函数")

def test_demo1():
    print("测试范例1")

def test_demo2():
    print("测试范例2")

class DemoTestCase(TestCase):
    def setUp(self):
        print("Demo类setUp方法")
    def tearDown(self):
        print("Demo类tearDown方法")
    def testDemo1(self):
        print("Demo类测试范例1")
    def testDemo2(self):
        print("Demo类测试范例2")










