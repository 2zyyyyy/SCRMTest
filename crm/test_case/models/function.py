'''
    定义截图函数
'''
from selenium import webdriver
import os


# 截图函数
def insert_func(driver, fileName):
    # os.path.dirname(__file__) 返回当前脚本的路径 D:\2zyyyyy\__MACOSX\PythonProject\xiaowangmaoTest\crm\test_case\models
    base_dir = os.path.dirname(os.path.dirname(__file__))  # 获取当前运行脚本的绝对路径（去掉最后一个路径）
    base_dir = str(base_dir)
    # D:/2zyyyyy/__MACOSX/PythonProject/xiaowangmaoTest/crm/test_case
    base_dir = base_dir.replace('\\', '/')  # 将绝对路径的'\\'替换成'/'相对路径
    base = base_dir.split('/test_case')[0]  # 从/test_case切割0次 目的就是去除/test_case
    file_path = base + '/report/images/' + fileName
    print(file_path)
    driver.get_screenshot_as_file(file_path)


if __name__ == '__main__':
    driver = webdriver.Chrome(r'D:\2zyyyyy\chromedriver_win32\chromedriver.exe')
    driver.get('https://www.baidu.com')
    insert_func(driver, 'bd.jpg')
    driver.quit()
