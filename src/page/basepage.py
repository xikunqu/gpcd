import logging
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from config.p_path import DRIVER_CHROM,CONFIG_FILE
from src.utils.read_file import YamlRead

class BasePage(object):

    # def __init__(self,remote_url,url,descried_cap):
    #     self.remote_url=remote_url
    #     self.url=url
    #     self.desired_capabilities=descried_cap
    #     self.driver=None
    #
    # def get(self,maximize_window=True, implicitly_wait=30,**kwargs):
    #     self.driver=webdriver.Remote(self.remote_url,self.desired_capabilities)
    #     self.driver.get(self.url)
    #     if maximize_window:
    #         self.driver.maximize_window()
    #     self.driver.implicitly_wait(implicitly_wait)
    #     return self
    brower_url=YamlRead(CONFIG_FILE).read()['url']

    def __init__(self):
        self.url=self.brower_url
        self.driver=None

    def get(self,maximize_window=True, implicitly_wait=30,**kwargs):
        self.driver=webdriver.Chrome(executable_path=DRIVER_CHROM)
        self.driver.get(self.url)
        if maximize_window:
            self.driver.maximize_window()
        self.driver.implicitly_wait(implicitly_wait)
        return self

    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(lambda driver:driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except:
            logging.info("%s页面中未能找到%s元素" % (self, loc))

    def find_elements(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_elements(*loc)
        except:
            logging.info("%s页面中未能找到%s元素" % (self, loc))

    def get_cookies(self):
        self.driver.get_cookies()

    def add_cookie(self,cookie):
        self.driver.add_cookie(cookie)

    def refresh(self):
        self.driver.refresh()

    def close(self):
        self.driver.close()

    def get_url(self):
        return self.driver.current_url

    def quit(self):
        self.driver.quit()


# if __name__=="__main__":
#     page=BasePage()
#     page.get()

