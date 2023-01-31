from selenium.webdriver.common.by import By


class example_page_login:
    """
    存放登录页面元素
    """
    #账号
    phone = (By.NAME, 'phone')
    #密码
    password = (By.NAME,'password')
    #登录按钮
    login = (By.XPATH, '//*[@id="app"]/section/div/div/form/div[4]/button')

