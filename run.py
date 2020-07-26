import unittest
import HTMLTestRunner_cn
from TestCases.test_login_email import TestLogin
from Common.project_path import *


suite = unittest.TestSuite()
loder = unittest.TestLoader()
suite.addTest(loder.loadTestsFromTestCase(TestLogin))

with open(test_report_path, 'wb') as file:
    runner = HTMLTestRunner_cn.HTMLTestRunner(stream=file, title='单元测试', description='测试报告', tester='吴迪')
    runner.run(suite)

