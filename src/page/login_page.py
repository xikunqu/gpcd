from src.page.basepage import BasePage
from selenium.webdriver.common.by import By
from config.p_path import  DATA_PATH
import time,os,json

class LoginPage(BasePage):

    ele_mobile=(By.CSS_SELECTOR,"input[type='text']")
    ele_psd=(By.CSS_SELECTOR,"input[type='password']")
    ele_login=(By.XPATH,"//span[.='登录']")

    def input_mobile(self,mobile):
        self.driver.find_element(*self.ele_mobile).send_keys(mobile)

    def input_psd(self,password):
        self.driver.find_element(*self.ele_psd).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.ele_login).click()

    def login(self,mobile,password):
        self.input_mobile(mobile)
        self.input_psd(password)
        self.click_login()


    def login_by_cookie(self):
        cookies=self.get_cookies()
        for cookie in cookies:
            self.add_cookie(cookie)

        # cookie_file=os.path.join(DATA_PATH,"cookie.txt")
        #
        # with open(cookie_file,"w") as f:
        #     f.write(json.dumps(cookies))
        #
        #
        # with open(cookie_file,"r") as f:
        #     cookies=f.read()
        #     cookie=json.loads(cookies)
        #
# a=LoginPage()
# a.get()
# a.input_mobile("13027153825")
# a.input_psd("qwe123")
# a.click_login()
# time.sleep(5)

# cookies=a.get_cookies()
# print(cookies)
# print(type(cookies))
#
#
# f1=open(cookie_file,'w')
# f1.write(json.dumps(cookies))
# f1.close()

#
# time.sleep(3)
# a.quit()


