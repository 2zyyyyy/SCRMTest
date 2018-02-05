import unittest
from models import myunit, function
from models.page_object.changepwdPage import *
from models.page_object.loginPage import Login
from models.driver import *
from time import *


class ChangeTest(myunit.MyTest):
    '''后台修改密码测试'''
    def change_verify(self, old='', new1='', new2=''):
        ChangePwd(self.driver).changePwd(old, new1, new2)

    def test_changePwd_1(self):
        '''原始密码、新密码都为空时'''
        Login(self.driver).user_login()
        self.change_verify()
        po = ChangePwd(self.driver)
        self.assertEqual(po.oldpwd_error(), '原始密码不能为空！')
        function.insert_func(self.driver, 'oldpwd_null.jpg')

    def test_changePwd_2(self):
        '''新密码都为空时'''
        Login(self.driver).user_login()
        self.change_verify(old='111111')
        po = ChangePwd(self.driver)
        self.assertEqual(po.newpwd_1_error(), '新密码不能为空！')
        function.insert_func(self.driver, 'newpwd1_null.jpg')

    def test_changePwd_3(self):
        '''确认新密码为空时'''
        Login(self.driver).user_login()
        self.change_verify(old='111111', new1='123456')
        po = ChangePwd(self.driver)
        self.assertEqual(po.newpwd_2_error(), '确认密码不能为空！')
        function.insert_func(self.driver, 'newpwd2_null.jpg')

    def test_changePwd_4(self):
        '''两次密码不一致时'''
        Login(self.driver).user_login()
        self.change_verify(old='111111', new1='123456', new2='147852')
        po = ChangePwd(self.driver)
        self.assertEqual(po.newpwd_2_error(), '两次密码输入不一致！')
        function.insert_func(self.driver, 'pwd_unlike.jpg')

    def test_changePwd_5(self):
        '''原始密码错误时'''
        Login(self.driver).user_login()
        self.change_verify(old='sdfewr', new1='123456', new2='123456')
        po = ChangePwd(self.driver)
        self.assertEqual(po.oldpwd_error(), '原始密码错误！')
        function.insert_func(self.driver, 'oldpwd_error.jpg')

    # def test_changePwd_6(self):
    #     '''新密码与旧密码相同时'''
    #     Login(self.driver).user_login()
    #     self.change_verify(old='111111', new1='111111', new2='111111')
    #     po = ChangePwd(self.driver)
    #     self.assertEqual(po.oldpwd_error(), '新密码不能与原始密码相同！')
    #     function.insert_func(self.driver, 'notlike.jpg')

    def test_changePwd_7(self):
        '''修改成功时'''
        Login(self.driver).user_login()
        self.change_verify(old='111111', new1='111111', new2='111111')
        # po = ChangePwd(self.driver)
        # self.assertEqual(driver.current_url(), 'http://crm.xiaowangmao.com/logout.html')
        function.insert_func(self.driver, 'changepwd_suc.jpg')

if __name__ == '__main__':
    unittest.main()
