from selenium import webdriver
from PageObjects.step_pigsale_serach import PigsalePage as DB
import time


driver = webdriver.Chrome()
print("开始")
#访问智能售猪
driver.get('https://znsz.smartahc.com/#/user/login')

DB(driver).search_login()
# DB(driver).abnormal_pig()
DB(driver).start_pigs()
# DB(driver).recheck_pig()
# time.sleep(240)
DB(driver).historical_pig_sales()
# DB(driver).end_pigs()
driver.quit()


