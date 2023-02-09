import unittest
import HtmlTestRunner
from loginpage_test import LoginPageTest
from order_shop_test import OrderTest
# get all tests from SearchProductTest and HomePageTest class
loginpage_tests = unittest.TestLoader().loadTestsFromTestCase(LoginPageTest)
orderpage_tests = unittest.TestLoader().loadTestsFromTestCase(OrderTest)
# create a test suite combining search_test and home_page_test
smoke_tests = unittest.TestSuite([loginpage_tests, orderpage_tests])
# run the suite
runner = HtmlTestRunner.HTMLTestRunner(output='src/KFC/Reports',report_title='Test Report',descriptions='Smoke Tests')
# run the suite using HTMLTestRunner
runner.run(smoke_tests)