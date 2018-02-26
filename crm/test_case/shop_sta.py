import unittest
from models import myunit, function
from models.page_object.shopPage import Shop
from models.page_object.loginPage import Login
from models.page_object.changepwdPage import ChangePwd
from models.driver import *
from time import *


class ShopNameTest(myunit.MyTest):
    '''设置店铺信息测试'''

    def shopName_verify(self, number, shopName='', shopKepper=''):
        Shop(self.driver).shopSetting(number, shopName, shopKepper)

    def test_setting_1(self):
        '''
        平台为淘宝 其他信息为空
        '''
        Login(self.driver).user_login()
        self.shopName_verify(0)
        sleep(5)


if __name__ == '__main__':
    unittest.main()
