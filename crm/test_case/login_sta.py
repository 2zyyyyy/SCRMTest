from time import sleep
import unittest, random, sys
# sys.path.append('./models')
# sys.path.append('./page_object')
from models import myunit, function
from models.page_object.loginPage import Login


class LoginTest(myunit.MyTest):
    '''后台登录测试'''

    # 测试用户登录
    def user_login_verify(self, username='', password=''):
        Login(self.driver).user_login(username, password)

    def test_login_1(self):
        '''用户名、密码为空时登录'''
        self.user_login_verify()
        po = Login(self.driver)
        self.assertEqual(po.user_error(), '邮箱账号不得为空！')
        function.insert_func(self.driver, 'user_pwd_empty.jpg')

    def test_login_2(self):
        '''用户名为空时登录'''
        self.user_login_verify(password='111111')
        po = Login(self.driver)
        self.assertEqual(po.user_error(), '邮箱账号不得为空！')
        function.insert_func(self.driver, 'user_empty.jpg')

    def test_login_3(self):
        '''用户名正确、密码为空时登录'''
        self.user_login_verify(username='android4google@163.com')
        po = Login(self.driver)
        self.assertEqual(po.pass_error(), '密码不得为空！')
        function.insert_func(self.driver, 'pwd_empty.jpg')

    def test_login_4(self):
        '''用户名、密码都不匹配时登录'''
        # character = random.choice('qwertyuiopasdfghjklzxcvbnm')
        # username = character + 'qq.com'
        username = 'android4google@163.com'
        self.user_login_verify(username, password='1321125')
        po = Login(self.driver)
        self.assertEqual(po.pass_error(), '用户名或密码有误！')
        function.insert_func(self.driver, 'user_pwd_error.jpg')

    def test_login_5(self):
        '''用户名、密码匹配时登录'''
        username = 'android4google@163.com'
        self.user_login_verify(username, password='111111')
        po = Login(self.driver)
        self.assertEqual(po.user_login_success(), username)
        function.insert_func(self.driver, 'login_success.jpg')


if __name__ == '__main__':
    unittest.main()
