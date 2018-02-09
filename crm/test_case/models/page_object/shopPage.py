from .base import Page
from selenium.webdriver.common.by import By
from time import sleep
from .changepwdPage import *


class Shop(Page):
    '''
    小旺猫系统店铺配置
    '''
    basicsConfig_loc = (By.XPATH, '//*[@id="side-menu"]/li[8]/a/span[1]')  # 基础配置
    shopConfig_loc = (By.XPATH, '//*[@id="side-menu"]/li[8]/ul/li[1]/a')  # 店铺配置
    arrow_loc = (By.XPATH, '//*[@id="shopInfoFrom"]/div[1]/div/div/span/i')  # 下拉框
    list = (By.CSS_SELECTOR, 'ul.addSetHidden.cumsetHidden>li')
    # liTmall_LOC = (By.XPATH, '//*[@id="shopInfoFrom"]/div[1]/div/ul/li[1]')  # 淘宝天猫
    # liJd_LOC = (By.XPATH, '//*[@id="shopInfoFrom"]/div[1]/div/ul/li[2]')  # 京东
    shopName_loc = (By.ID, 'shopname')  # 店铺名称
    shopKeeper_loc = (By.ID, 'wangwang')  # 掌柜旺旺
    saveBtn_loc = (By.ID, 'saveBtn')  # 保存

    # Action
    def pullDown(self):
        self.find_element(*self.arrow_loc).click()

    def select_shop(self, number):
        self.find_element(*self.list)[number].click()  # 0淘宝 1京东 2唯品会

    def shopName(self, shopName):
        self.find_element(*self.shopName_loc).send_keys(shopName)

    def shopKepperName(self, shopKepperName):
        self.find_element(*self.shopName_loc).send_keys(shopKepperName)

    def saveBtn(self):
        self.find_element(*self.saveBtn_loc).click()

    def shopSetting(self, platform, shopName, shopKepper):
        ChangePwd.switch_frame()
        self.pullDown()
        self.select_shop(platform)
        self.shopName(shopName)
        self.shopKepperName(shopKepper)
        self.saveBtn()
        sleep(1)
