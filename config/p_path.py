import os
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_PATH=os.path.join(BASE_PATH,"config")
CONFIG_FILE=os.path.join(CONFIG_PATH,"config.yaml")
DRIVER=os.path.join(BASE_PATH,"driver")
DRIVER_CHROM=os.path.join(DRIVER,"chromedriver.exe")
DATA_PATH=os.path.join(BASE_PATH,"data")
