import sys
import time
from ipyweb.app import app, appIpyweb
from ipyweb.utils import utils
from ipyweb.config import config, configIpyweb
from ipyweb.logger import logger, loggerIpyweb
from ipyweb.singleton import singleton
from ipyweb.pywebview.windows import windows


class appRunner(metaclass=singleton):
    appRunnerDefaultName = 'runner'
    appRunnerDefaultClsName = 'runner'
    appRunnerDefaultAction = 'run'
    appRunner = None
    appRunnerCls = None
    windowsOpenedPreload = None
    appName = ''
    _loaded = False

    @classmethod
    def boot(self):
        try:
            if self.load():
                if hasattr(self.appRunnerCls, self.appRunnerDefaultAction):
                    run = getattr(self.appRunnerCls, self.appRunnerDefaultAction)
                    if config.get('windows.guiDriverEnable', True):
                        windows().run({},
                                      onCreateReady=self._onWindowsCreateReady,
                                      onCreated=self._onWindowsCreated,
                                      onOpenReady=self._onWindowsOpenReady,
                                      onOpened=self._onWindowsOpened
                                      )
                    else:
                        if callable(self.windowsOpenedPreload): self.windowsOpenedPreload(self.appName)
                        run(None)
                        try:
                            while True:
                                time.sleep(3600 * 24 * 30)
                        except KeyboardInterrupt as e:
                            logger.console.debug(f"The application [{self.appName}] has exited normally.")

        except Exception as e:
            logger.console.error(f'An exception occurred during application [{self.appName}]  startup: {e}')
            time.sleep(3)
            sys.exit(0)

        return self

    @classmethod
    def load(self, reload=False):
        if self._loaded == False or reload == True:
            if appIpyweb._loaded == False: appIpyweb.load()
            if loggerIpyweb._loaded == False: loggerIpyweb.load()
            if configIpyweb._loaded == False: configIpyweb.load()
            self.getAppRunner()
            self.getAppRunnerCls()
            self._loaded = True
        return self.appRunner, self.appRunnerCls

    @classmethod
    def getAppRunner(self):
        self.appName = config.moduleMaps('name',
                                         app.getName()) if app.isExe else app.getName()  # 编译后读取module应用名 非编译环境直接读取
        appModulePath = '.'.join([app.appPath, self.appName, self.appRunnerDefaultName])
        try:
            self.appRunner = utils.smartImportModule(self.appRunnerDefaultName, appModulePath, app.rootPath)
        except ModuleNotFoundError as e:
            logger.console.error(f'The application runner module does not exist:[{appModulePath}]')
        except Exception as e:
            logger.console.error(f'An exception occurred while retrieving the runner module:[{appModulePath}]')
        if self.appRunner is None:
            logger.console.error(f'The application runner module does not exist:[{appModulePath}]')
        return self.appRunner

    @classmethod
    def getAppRunnerCls(self):
        try:
            if self.appRunner:
                appRunnerClsAttr = getattr(self.appRunner, self.appRunnerDefaultClsName)
                self.appRunnerCls = appRunnerClsAttr()
        except Exception as e:
            logger.console.error(
                f'An exception occurred while retrieving an instance of the application [{self.appName}] startup module: {e}')
            time.sleep(3)
            sys.exit(0)
        return self.appRunnerCls

    @classmethod
    def _onWindowsCreateReady(self, winCls):
        if hasattr(self.appRunnerCls, 'onCreateReady') and callable(self.appRunnerCls.onCreateReady):
            self.appRunnerCls.onCreateReady(winCls)

    @classmethod
    def _onWindowsCreated(self, winCls):
        if hasattr(self.appRunnerCls, 'onCreated') and callable(self.appRunnerCls.onCreated):
            self.appRunnerCls.onCreated(winCls)

    @classmethod
    def _onWindowsOpenReady(self, winCls):
        if hasattr(self.appRunnerCls, 'onOpenReady') and callable(self.appRunnerCls.onOpenReady):
            self.appRunnerCls.onOpenReady(winCls)

    @classmethod
    def _onWindowsOpened(self, winCls):
        if hasattr(self.appRunnerCls, 'onOpened') and callable(self.appRunnerCls.onOpened): self.appRunnerCls.onOpened()
        if callable(self.windowsOpenedPreload): self.windowsOpenedPreload(self.appName)
        if winCls.windows: self.appRunnerCls.run(winCls.windows)

    @classmethod
    def setWindowsOpenedPreload(self, windowsOpenedPreload=None):
        self.windowsOpenedPreload = windowsOpenedPreload
        return self
