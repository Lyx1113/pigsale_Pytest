import pytest,time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture(scope='function',autouse=True)
def access_web():
    #前置：打开浏览器
    #修改页面加载策略
    desired_capabilities = DesiredCapabilities.CHROME
    desired_capabilities["pageLoadStrategy"] = "none"

    #实例化对象
    driver = webdriver.Chrome()
    print("开始")
    #访问智能售猪
    driver.get('https://znsz.smartahc.com/#/user/login')
    #页面最大化
    # driver.maximize_window()
    #等待
    time.sleep(4)
    #通过yield传递driver参数
    yield driver
    #关闭浏览器
    driver.quit()
    return driver

# @pytest.fixture(scope='function')
# def refesh():
#     print(access_web)
#     yield access_web
#     #刷新页面
#     access_web.refresh()
#     access_web
#
#     time.sleep(1)
