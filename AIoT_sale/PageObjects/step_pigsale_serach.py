import time
import re
from PageLocators.example_page_login import example_page_login as BD
from PageLocators.example_page_pigsale import example_page_pigsale as pig
from Common.basepage import BasePage


class PigsalePage(BasePage, ):


    def search_login(self):
        """
        H5售猪登录
        :return:
        """
        self.input_text(BD.phone, "10086", doc="用户名/手机号")
        self.input_text(BD.password, "123456", doc="登录密码")
        self.click(BD.login, doc="登录")
        time.sleep(3)
        # text_search = self.get_elements_text_value(B)

    def start_pig(self):
        """
        开始育肥猪任务
        :return:
        """
        time.sleep(5)
        self.click(pig.pig,doc="育肥猪")
        #选择主机并确认
        self.click(pig.skseye,doc="选择天眼行")
        # self.click(pig.pig_sele,doc="选择肥猪销售")
        self.click(pig.pig_notarize,doc="确定选择")
        #获取摄像头元素文本值，如果为null进行选择摄像头操作，如果不为空，不进行选择摄像头
        time.sleep(3)
        text = self.get_elements_text_value(pig.camera,doc="选择摄像头")
        if text  is  None :
            self.click(pig.camera,doc="选择摄像头")
            self.click(pig.pig_notarize,doc="确认选择摄像头")
        #选择农场
        self.click(pig.cli_from,doc="选择农场")
        self.click(pig.pig_sele,doc="选择农场XXX")
        self.click(pig.pig_notarize,doc="确认选择农场")
        #下一步并开启任务
        self.click(pig.next_step,doc="下一步")
        self.click(pig.notarize,doc="我知道了")
        self.slide_to_bottom()
        # self.wait_elevisible(pig.start_pig,doc="开始售猪")
        self.click(pig.next_step,doc="开始售猪")
        self.click(pig.task_notarize,doc="确认")
        self.do_save_screenshot()

    def start_pigs(self):
        """
        开始育肥猪任务
        :return:
        """
        time.sleep(5)
        self.click(pig.pig,doc="育肥猪")
        #选择主机并确认
        # self.click(pig.skseye,doc="选择天眼行")
        # self.click(pig.pig_sele,doc="选择肥猪销售")
        # self.click(pig.pig_notarize,doc="确定选择")
        #获取摄像头元素文本值，如果为null进行选择摄像头操作，如果不为空，不进行选择摄像头
        time.sleep(3)
        # text = self.get_elements_text_value(pig.camera,doc="选择摄像头")
        # if text  is  None :
        #     self.click(pig.camera,doc="选择摄像头")
        #     self.click(pig.pig_notarize,doc="确认选择摄像头")
        #选择农场
        # self.click(pig.cli_from,doc="选择农场")
        # self.click(pig.pig_sele,doc="选择农场XXX")
        # self.click(pig.pig_notarize,doc="确认选择农场")
        #下一步并开启任务
        # self.click(pig.next_step,doc="下一步")
        self.click(pig.notarize,doc="我知道了")
        self.slide_to_bottom()
        time.sleep(2)
        # self.wait_elevisible(pig.start_pig,doc="开始售猪")
        self.click(pig.start_pig,doc="开始售猪")
        self.click(pig.task_notarize,doc="确认")
        self.do_save_screenshot()

    def end_pig(self):
        """
        进入任务并结束
        :return:
        """
        time.sleep(5)
        self.slide_to_top()
        # self.get_elements_text_value(pig.taskid,doc="任务列表")
        self.click(pig.taskid,doc="选择任务")
        self.slide_to_bottom()
        self.click(pig.task_end,doc="结束任务")
        self.click(pig.task_notarize,doc="确认结束任务")
        self.do_save_screenshot()

    def end_pigs(self):
        """
        关闭任务
        :return:
        """
        time.sleep(5)
        self.slide_to_top()
        self.click(pig.task_close,doc="关闭任务")
        self.click(pig.task_notarize,doc="确认关闭任务")
        self.do_save_screenshot()



    def abnormal_pig(self):
        """
        开启异常任务
        :return:
        """
        time.sleep(5)
        self.click(pig.task_abnormal,doc="选择异常任务")
        self.click(pig.skseye, doc="选择天眼行")
        # self.click(pig.pig_sele,doc="选择肥猪销售")
        self.click(pig.task_abnormal_notarize, doc="确定选择")
        # 获取摄像头元素文本值，如果为null进行选择摄像头操作，如果不为空，不进行选择摄像头
        time.sleep(3)
        text = self.get_elements_text_value(pig.camera, doc="选择摄像头")
        if text is None:
            self.click(pig.camera, doc="选择摄像头")
            self.click(pig.task_abnormal_notarize, doc="确认选择摄像头")
        # 选择农场
        self.click(pig.cli_from, doc="选择农场")
        # self.click(pig.pig_sele, doc="选择农场XXX")
        self.click(pig.task_abnormal_notarize, doc="确认选择农场")
        #选择开始时间与结束时间
        self.click(pig.startTime,doc="点击选择开始时间")
        self.click(pig.taskTime,doc="选择开始时间")
        self.click(pig.task_abnormal_notarize,doc="确认选择时间")
        #滑到底部
        self.slide_to_bottom()
        self.click(pig.endTime,doc="点击选择结束时间")
        self.click(pig.taskTimes,doc="选择结束时间")
        self.click(pig.task_abnormal_notarize, doc="确认选择时间")
        #开始异常售猪任务
        self.click(pig.startsellingpig,doc="开始异常售猪任务")

        self.click(pig.task_notarize,doc="确认开始售猪")

        self.do_save_screenshot()


    def recheck_pig(self):
        """
        复核
        :return:
        """
        time.sleep(5)
        #选择任务进行复核
        self.click(pig.taskid, doc="选择任务")
        self.slide_to_bottom()
        #判断该元素是否存在  不存在即结束该用例执行
        state = self.get_element_isDisplay(pig.flase_result,doc="选择复核为否")
        if state == True:
            #选择复核为否，查看复核视频
            self.click(pig.flase_result,doc="选择复核为否")
            self.click(pig.recheck_video,doc="查看复核视频")
            self.slide_to_bottom()
            #结束复核，进行任务复核结果确认
            self.click(pig.end_recheck,doc="结束复核")
            self.slide_to_bottom()

            self.click(pig.notarize_recheck,doc="确认复核")
            self.click(pig.task_notarize,doc="确认复核结果")
            self.do_save_screenshot()
        else :
            self.do_save_screenshot()

    def historical_pig_sales(self):
        """
        查看历史售猪列表
        :return:
        """
        time.sleep(5)
        self.click(pig.historical_pig_ico,doc="点击历史售猪ioc")
        time.sleep(1)
        pigvalue = self.get_elements_text_value(pig.historical_pig_sales,doc="历史记录列表")
        print(pigvalue)

        self.click(pig.historical_pig_sale,doc="选择单个任务")

        self.do_save_screenshot()

