import unittest
from models import myunit, function
from models.page_object.shopPage import Shop
from models.page_object.loginPage import Login
from models.driver import *
from time import *


class ShopNameTest(myunit.MyTest):
    '''设置店铺信息测试'''

    def shopName_verify(self, platform, shopName, shopKepper):
        shopSetting(self.driver).shopSetting(platform, shopName, shopKepper)

    def test_setting_1(self):
        Login(self.driver).user_login()


if __name__ == '__main__':
    unittest.main()
