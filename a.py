from selenium import webdriver

driver=webdriver.Chrome(executable_path="G:\gpcd\driver\chromedriver.exe")
driver.get("http://192.168.8.62:8080/gas/dist/#/")
driver.maximize_window()