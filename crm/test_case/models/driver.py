'''
    power by 2zyyyyy    2018/01/25
'''

from selenium.webdriver import Remote
from selenium import webdriver


# 启动浏览器驱动函数
def browser():
    driver = webdriver.Chrome(r'D:\2zyyyyy\chromedriver_win32\chromedriver.exe')
    driver.maximize_window()
    # host = '127.0.0.1:4444'  # 运行主机 默认端口号:127.0.0.1:4444
    # dc = {'browserName': 'chrome'}  # 指定浏览器('chrome', 'firefox')
    # driver = Remote(command_executor='http://' + host + 'wd/hub',
    #                 desired_capabilities=dc)
    return driver


if __name__ == '__main__':
    dr = browser()
    dr.get('http://www.baidu.com')
    dr.quit()
