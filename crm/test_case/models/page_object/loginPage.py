from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from .base import Page


class Login(Page):
    '''
    小旺猫系统用户登录界面
    '''
    url = '/login.html'
    username_loc = (By.XPATH, '//*[@id="email"]')
    password_loc = (By.XPATH, '//*[@id="pwd"]')
    btn_loc = (By.ID, 'loginBtn')

    # Acitons
    def login_username(self, username):
        self.find_element(*self.username_loc).send_keys(username)

    def login_password(self, password):
        self.find_element(*self.password_loc).send_keys(password)

    def submit(self):
        self.find_element(*self.btn_loc).click()

    # 定义 统一登录入口
    def user_login(self, username='android4google@163.com', password='111111'):
        self.open()
        self.login_username(username)
        self.login_password(password)
        self.submit()
        sleep(1)

    user_error_hint_loc = (By.ID, 'emialerr')
    pass_error_hint_loc = (By.ID, 'pwderr')
    userInfo_success_loc = (By.XPATH, '//*[@id="page-wrapper"]/div[1]/nav/div[2]/h4/span')

    # 用户名错误提示
    def user_error(self):
        return self.find_element(*self.user_error_hint_loc).text

    # 密码错误提示
    def pass_error(self):
        return self.find_element(*self.pass_error_hint_loc).text

    # 登录成功的用户信息
    def user_login_success(self):
        return self.find_element(*self.userInfo_success_loc).text
