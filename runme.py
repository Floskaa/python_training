import os
print(os.environ['PATH'])
import shutil
print(shutil.which('geckodriver'))
import shutil
from selenium import webdriver
print(shutil.which('chromedriver'))
driver = webdriver.Chrome()
driver.quit()
