from src.page.login_page import LoginPage
from src.utils.read_file import YamlRead
from config.p_path import DATA_PATH


import logging,os,time

class TestLogin(object):


    data_file=os.path.join(DATA_PATH,"login.yaml")
    mobile=YamlRead(data_file).read()['mobile']
    password=YamlRead(data_file).read()['password']

    def setup(self):
        self.page=LoginPage().get()

    def teardown(self):
        self.page.quit()

    def test_login(self):
        self.page.login(self.mobile,self.password)
        time.sleep(3)
        assert "myIndex" in self.page.get_url()


