from selenium.webdriver.common.by import By

class example_page_pigsale:
    """
    存放智能售猪页面
    """
    #标签：售猪
    sell_pig = (By.CLASS_NAME,'van-tabbar-item__icon')
    #标签：历史售猪
    historical_pig_tab  = (By.CSS_SELECTOR,'#app > div.bottom.van-tabbar__placeholder > div > div.van-tabbar-item.van-tabbar-item--active')
    #育肥猪功能按钮
    pig = (By.XPATH,'//*[@id="app"]/section/div/div/div[1]/div[1]')
    #异常功能按钮
    historical_pig = (By.XPATH,'//*[@id="app"]/section/div/div/div[1]/div[2]')
    #选择天眼行设备
    skseye = (By.XPATH,'//*[@id="app"]/section/div/form/div[2]/div[2]/div/input')
    #选择,根据li[]数来确定选择第几个
    pig_sele = (By.XPATH,'//*[@id="app"]/section/div/form/div[8]/div/div[2]/div[1]/ul/li[1]')
    #下拉框确认
    pig_notarize = (By.XPATH,'//*[@id="app"]/section/div/form/div[8]/div/div[1]/button[2]')
    #摄像头下拉框
    camera = (By.XPATH,'//*[@id="app"]/section/div/form/div[3]/div[2]/div/input')
    #点击农场
    cli_from = (By.XPATH,'//*[@id="app"]/section/div/form/div[4]/div[2]/div[1]/input')
    #下一步
    next_step = (By.XPATH,'//*[@id="app"]/section/div/form/div[9]/button')
    #通过质检页面进行确认
    notarize = (By.XPATH,'//*[@id="app"]/section/div/div[5]/div[3]/button')
    #开始售猪
    start_pig = (By.XPATH,'//*[@id="app"]/section/div/form/div[7]/button')
    # start_pig = (By.XPATH,'//*[@id="app"]/section/div/form/div[9]/button')
    #当前所有任务
    taskid = (By.XPATH,'//*[@id="app"]/section/div/div/div[3]/div[1]')
    #结束当前任务
    task_end = (By.XPATH,'//*[@id="app"]/section/div/div[5]/div/button')
    #确认
    task_notarize = (By.XPATH,'/html/body/div[4]/div[3]/button[2]')
    #关闭任务
    task_close = (By.XPATH,'//*[@id="app"]/section/div/div/div[1]/div[3]')
    #异常任务
    task_abnormal = (By.XPATH,'//*[@id="app"]/section/div/div/div[1]/div[2]')
    #点击开始任务时间
    startTime = (By.NAME,'startTime')
    endTime = (By.NAME,'endTime')
    #选择时间
    taskTime = (By.XPATH,'//*[@id="app"]/section/div/form/div[11]/div/div[2]/div[3]/ul/li[5]')
    taskTimes = (By.XPATH,'//*[@id="app"]/section/div/form/div[11]/div/div[2]/div[4]/ul/li[19]')
    #确认选择
    task_abnormal_notarize = (By.XPATH,'//*[@id="app"]/section/div/form/div[11]/div/div[1]/button[2]')
    #异常开始售猪
    startsellingpig = (By.XPATH,'//*[@id="app"]/section/div/form/div[12]/button')

    #结果确认选择
    flase_result = (By.XPATH,'//*[@id="app"]/section/div/div[4]/div[6]/div[2]/div[2]/div[2]/div/div/div/div[2]/div')
    #查看复核视频
    recheck_video = (By.XPATH,'//*[@id="app"]/section/div/div[4]/div[6]/div[2]/div[3]/div[2]/div/div/button')
    #结束复核
    end_recheck = (By.XPATH,'//*[@id="app"]/section/div/div[4]/div[2]/button')
    #确认复核
    notarize_recheck = (By.XPATH,'//*[@id="app"]/section/div/div[5]/div/button')

    #历史售猪ico
    historical_pig_ico = (By.XPATH,'//*[@id="app"]/div[2]/div/div[1]/div[1]')
    #历史记录列表
    historical_pig_sales = (By.XPATH,'//*[@id="app"]/section/div/div/div[3]')
    #单个任务记录
    historical_pig_sale = (By.XPATH,'//*[@id="app"]/section/div/div/div[3]/div[1]')
