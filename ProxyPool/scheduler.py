TESTER_CYCLE = 20
GETTER_CYCLE = 20
TESTER_ENABLED = True
GETTER_ENABLED = True
API_ENABLED = True
API_HOST = '127.0.0.1'
API_PORT = 5555

from multiprocessing import Process
from ProxyPool.api import app
from ProxyPool.getter import Getter
from ProxyPool.tester import Tester
import time


class Scheduler():
    def schedule_tester(self, cycle=TESTER_CYCLE):
        """
        定时测试代理
        """
        tester = Tester()
        while True:
            print('正在调度测试模块')
            tester.run()
            time.sleep(cycle)


    def schedule_getter(self, cycle=GETTER_CYCLE):
        """
        定时获取代理
        """
        getter = Getter()
        while True:
            print('正在调度获取模块')
            getter.run()
            time.sleep(cycle)


    def schedule_api(self):
        """
        开启API
        """
        app.run(API_HOST, API_PORT)


    def run(self):
        print('代理池开始运行')
        if TESTER_ENABLED:
            tester_process = Process(target=self.schedule_tester)
            tester_process.start()

        if GETTER_ENABLED:
            getter_process = Process(target=self.schedule_getter)
            getter_process.start()

        if API_ENABLED:
            api_process = Process(target=self.schedule_api)
            api_process.start()

if __name__ == '__main__':
    scheduler = Scheduler()
    scheduler.run()