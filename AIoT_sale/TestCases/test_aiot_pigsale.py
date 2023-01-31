import time,os,allure
from PageObjects.step_pigsale_serach import PigsalePage as DB

root = os.path.dirname(os.path.abspath(__file__))
class TestPigsale:

    def test_pigsale_task(self,access_web):
        """
        开始一个任务并结束
        :param access_web:
        :return:
        """
        result_text = DB(access_web).search_login()
        print(result_text)
        time.sleep(3)
        start_end = DB(access_web).start_pig()
        print(start_end)
        time.sleep(240)
        DB(access_web).end_pig()

    def test_pigsale_tasks(self,access_web):
        """
        开始一个任务快速关闭任务
        :param access_web:
        :return:
        """
        result_text = DB(access_web).search_login()
        print(result_text)
        time.sleep(3)
        DB(access_web).start_pigs()
        time.sleep(240)
        DB(access_web).end_pigs()

    def test_pigsale_abnormal(self,access_web):
        """
        开始一个异常任务
        :param access_web:
        :return:
        """
        DB(access_web).abnormal_pig()
        time.sleep(600)

    def test_pigsale_recheck(self,access_web):
        """
        复核一个任务
        :param access_web:
        :return:
        """
        result_text = DB(access_web).search_login()
        print(result_text)
        time.sleep(3)
        DB(access_web).recheck_pig()

    def test_pigsale_historical(self,access_web):
        """
        查看历史售猪列表
        :param access_web:
        :return:
        """
        result_text = DB(access_web).search_login()
        print(result_text)
        time.sleep(3)
        DB(access_web).historical_pig_sales()




