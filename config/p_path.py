import os
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_PATH=os.path.join(BASE_PATH,"config")
DRIVER=os.path.join(BASE_PATH,"driver")
DRIVER_CHROM=os.path.join(DRIVER,"chromedriver.exe")
print(DRIVER_CHROM)