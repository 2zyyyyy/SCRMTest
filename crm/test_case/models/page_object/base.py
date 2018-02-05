'''
    浅析PO设计模型
    1、基本层(初始化方法以及封装webdriver中的基本方法open()、find_element()等)
    2、页面层(对定位页面元素方法的封装)
    3、逻辑层(对具体业务逻辑的封装)
    有了以上的封装,测试的时候只需要给具体的数据即可
'''


class Page(object):
    '''
    页面基础类
    '''
    bbs_url = 'http://crm.xiaowangmao.com'

    def __init__(self, selenium_driver, base_url=bbs_url, parent=None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent

    # 单下划线_开头表示是私有的，就是通过import*时私有的方法不会被导入
    # _open()方法用于打开URL网站，并检验页面链接加载是否正确
    def _open(self, url):
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(), 'Did not land on %s' % url

    # 重写定位元素的方法，loc==(By.NAME,"email"),是一个元组，Python方法中入参是元组时需要在前面加*
    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    # open()方法通过调用_open()方法打开URL网站
    def open(self):
        self._open(self.url)

    # url地址断言部分
    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def script(self, src):
        return self.driver.execute_script(src)
