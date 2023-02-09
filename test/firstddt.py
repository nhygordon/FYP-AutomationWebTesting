import unittest
from ddt import ddt,data,unpack
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import HtmlTestRunner
@ddt
class MyTesting(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.get('http://www.baidu.com')

    @data(['python','python_百度搜索'],['java','java_百度搜索'])
    @unpack
    def test_baidu(self,a,b):
        self.dr.find_element(By.ID,"kw").send_keys(a) # find_element_by_id('kw').send_keys(a)
        self.dr.find_element(By.ID,"su").click() #find_element_by_id('su').click()
        sleep(2)
        c = self.dr.title
        self.assertEqual(b,c)
         
 
    def tearDown(self):
        self.dr.close()
if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HtmlTestRunner.HTMLTestRunner(output='src/KFC/Reports'))

