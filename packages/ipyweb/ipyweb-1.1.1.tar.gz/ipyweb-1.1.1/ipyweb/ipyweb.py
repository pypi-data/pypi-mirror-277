import time
from ipyweb.app import app, appIpyweb
from ipyweb.config import config, configIpyweb
from ipyweb.logger import logger
from ipyweb.logger import loggerIpyweb
from ipyweb.module import moduleIpyweb
from ipyweb.preload import preloadIpyweb
from ipyweb.event import eventIpyweb
from ipyweb.appRunner import appRunner


class ipyweb():

    @classmethod  # 启动系统
    def boot(self, appName='', reload=False):
        sysIpyweb.boot(appName, reload)
        return self

    @classmethod  # 重新启动
    def reboot(self, appName=''):
        sysIpyweb.reboot(appName)
        return self

    @classmethod  # 重启基础数据
    def bootBaser(self, reload=False):
        sysIpyweb.bootBaser(reload)
        return self

    @classmethod  # 获取启动耗时分析数据
    def getBootTime(self):
        return sysIpyweb.bootTime

    @classmethod
    def setOnStart(self, onStart=None):
        sysIpyweb.setOnStart(onStart)
        return self

    @classmethod
    def setOnBased(self, onBased=None):
        sysIpyweb.setOnBased(onBased)
        return self

    @classmethod
    def setOnPreloaded(self, onPreloaded=None):
        sysIpyweb.setOnPreloaded(onPreloaded)
        return self


class sysIpyweb():
    loaded = False
    onStart = None  # 系统启动
    onBased = None  # 基础数据加载完毕=预载器启动前
    onPreloaded = None  # 预载器启动完毕=应用启动前
    bootTime = {
        'ipywebStart': time.time(),
        'ipywebEnd': 0.00,
        'ipywebRun': 0.00,
        'ipywebBoots': {
            'bootBaserStart': 0.00,
            'bootBaserEnd': 0.00,
            'bootBaserRun': 0.00,
            'bootPreloaderStart': 0.00,
            'bootPreloaderEnd': 0.00,
            'bootPreloaderRun': 0.00,
        },
        'windowsStart': 0.00,
        'windowsEnd': 0.00,
        'windowsRun': 0.00,
        'appPreloadStart': 0.00,
        'appPreloadEnd': 0.00,
        'bootAppRun': 0.00,
        'totalTime': 0.00,
    }

    @classmethod  # 启动系统
    def boot(self, appName='', reload=False):
        app.setName(appName)
        self.getAppRunerOnEvent()  # 侦测应用执行钩子
        try:
            if self.loaded == False:
                if callable(self.onStart): self.onStart()
                self.bootBaser(reload)  # 基础加载
                if callable(self.onBased): self.onBased()
                self.bootPreloader()  # 预载器
                self.loaded = True
            self.bootTime['ipywebEnd'] = time.time()
            self.bootTime['ipywebRun'] = self.bootTime['ipywebEnd'] - self.bootTime['ipywebStart']
            if callable(self.onPreloaded): self.onPreloaded()
            self.bootAppRunner()  # 应用启动
        except Exception as e:
            logger.console.error(f'An exception occurred during application [{appName}] boot: {e}')
        return self

    @classmethod  # 重新启动
    def reboot(self, appName=''):
        self.loaded = False
        self.boot(appName, True)
        return self

    @classmethod  # 启动应用
    def bootAppRunner(self):
        self.bootTime['windowsStart'] = time.time()

        def windowsOpened(appName):
            self.bootTime['windowsEnd'] = time.time()
            self.bootTime['windowsRun'] = self.bootTime['windowsEnd'] - self.bootTime['windowsStart']
            self.bootTime['appPreloadStart'] = time.time()
            preloadIpyweb.load().run(False)  # 窗口打开后启动预载器
            self.bootTime['appPreloadEnd'] = time.time()
            self.bootTime['appPreloadRun'] = self.bootTime['appPreloadEnd'] - self.bootTime['appPreloadStart']
            self.bootTime['totalTime'] = self.bootTime['ipywebRun'] + self.bootTime['windowsRun'] + self.bootTime[
                'appPreloadRun']
            logger.console.info(
                f'{appName} - <basic[{round(self.bootTime["ipywebBoots"]["bootBaserRun"], 3)}s] / '
                f'ipywebPreload[{round(self.bootTime["ipywebBoots"]["bootPreloaderRun"], 3)}s] / '
                f'window[{round(self.bootTime["windowsRun"], 3)}s] / '
                f'appPreload[{round(self.bootTime["appPreloadRun"], 3)}s] / '
                f'totalTime[{round(self.bootTime["totalTime"], 3)}s]>'
            )

        appRunner.setWindowsOpenedPreload(windowsOpened).boot()
        return self

    @classmethod  # 应用启动回调生命周期事件
    def getAppRunerOnEvent(self):
        appRunnerModule, appRunnerCls = appRunner.load()
        if hasattr(appRunnerCls, 'onStart'): self.setOnStart(appRunnerCls.onStart)
        if hasattr(appRunnerCls, 'onBased'): self.setOnBased(appRunnerCls.onBased)
        if hasattr(appRunnerCls, 'onPreloaded'): self.setOnPreloaded(appRunnerCls.onPreloaded)
        return self

    @classmethod  # 重启基础数据
    def bootBaser(self, reload=False):
        self.bootTime['ipywebBoots']['bootBaserStart'] = time.time()
        appIpyweb.load(reload)
        loggerIpyweb.load(reload)
        configIpyweb.load(reload)
        moduleIpyweb.load(reload)
        eventIpyweb.load(reload)
        self.bootTime['ipywebBoots']['bootBaserEnd'] = time.time()
        self.bootTime['ipywebBoots']['bootBaserRun'] = self.bootTime['ipywebBoots']['bootBaserEnd'] - \
                                                       self.bootTime['ipywebBoots']['bootBaserStart']
        return self

    @classmethod  # 启动预载模块
    def bootPreloader(self):
        self.bootTime['ipywebBoots']['bootPreloaderStart'] = time.time()
        preloadIpyweb.load().run(True)
        self.bootTime['ipywebBoots']['bootPreloaderEnd'] = time.time()
        self.bootTime['ipywebBoots']['bootPreloaderRun'] = self.bootTime['ipywebBoots']['bootPreloaderEnd'] - \
                                                           self.bootTime['ipywebBoots']['bootPreloaderStart']
        return self

    @classmethod
    def setOnStart(self, onStart=None):
        self.onStart = onStart
        return self

    @classmethod
    def setOnBased(self, onBased=None):
        self.onBased = onBased
        return self

    @classmethod
    def setOnPreloaded(self, onPreloaded=None):
        self.onPreloaded = onPreloaded
        return self
