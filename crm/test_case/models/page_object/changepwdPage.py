from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from .base import Page
from models.page_object.loginPage import Login


class ChangePwd(Page):
    # url = '/login.html'
    cac_loc = (By.XPATH, '//*[@id="side-menu"]/li[9]/a/span[1]')  # 账户管理
    changePwd_loc = (By.XPATH, '//*[@id="side-menu"]/li[9]/ul/li/a')  # 修改密码
    oldPwd_loc = (By.ID, 'oldpwd')  # 原始密码
    newPwd1_loc = (By.ID, 'pwd1')  # 新密码
    newPwd2_loc = (By.ID, 'pwd2')  # 确认新密码
    savebtn_loc = (By.ID, 'savePwd')  # 保存

    # Action
    def cac_enter(self):
        self.find_element(*self.cac_loc).click()

    def change_enter(self):
        self.find_element(*self.changePwd_loc).click()

    def switch_frame(self):
        return self.driver.switch_to.frame("iframeId")

    def old_pwd(self, oldPwd):
        self.find_element(*self.oldPwd_loc).send_keys(oldPwd)

    def new_pwd1(self, newPwd1):
        self.find_element(*self.newPwd1_loc).send_keys(newPwd1)

    def new_pwd2(self, newPwd2):
        self.find_element(*self.newPwd2_loc).send_keys(newPwd2)

    def savePwd(self):
        self.find_element(*self.savebtn_loc).click()

    def changePwd(self, old='123456', new1='000000', new2='000000'):
        # self.open()
        self.cac_enter()
        self.change_enter()
        self.switch_frame()
        self.old_pwd(old)
        self.new_pwd1(new1)
        self.new_pwd2(new2)
        self.savePwd()
        sleep(1)

    oldpwdnull_loc = (By.ID, 'pwderr')
    newpwdnull_1_loc = (By.ID, 'pwderr1')
    newpwdnull_2_loc = (By.ID, 'pwderr2')

    # 原始密码错误提示
    def oldpwd_error(self):
        return self.find_element(*self.oldpwdnull_loc).text

    # 新密码错误提示
    def newpwd_1_error(self):
        return self.find_element(*self.newpwdnull_1_loc).text

    # 确认新密码错误提示
    def newpwd_2_error(self):
        return self.find_element(*self.newpwdnull_2_loc).text
