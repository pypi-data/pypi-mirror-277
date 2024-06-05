from ipyweb.app import app
from ipyweb.config import config
from ipyweb.contracts.ipywebPreload import ipywebPreload
from ipyweb.logger import logger
from ipyweb.service import service
from ipyweb.services.crontab import crontabRunner


class crontabPreload(ipywebPreload):
    # preload加载此模块时调用的配置信息
    ipywebAutoConfig = {
        'enable': True,  # 是否关闭运行
        # 启动节点 True:窗口打开后 False:窗口打开前 默认 False
        'windowsOpen': config.get('app.preload.crontabPreloadAtWindowsOpen', False),
        'daemon': True,  # 是否守护执行 默认True
        'block': False,  # 是否阻塞执行 默认False
        'max': 1,  # 进程池或线程池数量 默认1
        'usePool': False,  # 是否线程池 默认False
    }
    crontabs = {}

    def run(self, **kwargs):
        self.load()
        return self

    def load(self):
        self._loadFromCrontabs(f'{app.ipywebPath}.{app.crontabsName}')
        if config.get('app.autoLoad.loadCrontabsEnable', False) == True:
            self._loadFromCrontabs(f'{app.appPath}.{app.crontabsName}')
        try:
            for name, module in self.crontabs.items():
                moduleConfig = getattr(module, app.ipywebAutoConfigName, {})
                if moduleConfig.get('enable', False) == True: self.crontabRun(name, moduleConfig, module)
        except Exception as e:
            logger.console.error(f'An exception occurred while reading the queue dirs:{e}')
        return self

    def _loadFromCrontabs(self, path=''):
        try:
            modules = service.module(path)
            for name, module in modules.items():
                self.crontabs[name] = module
        except Exception as e:
            logger.console.error(f'An exception occurred while reading the crontab module:{e}')
        return self

    def crontabRun(self, name='', moduleConfig={}, crontabModule=None):
        try:
            config = dict(moduleConfig, **{
                'name': crontabModule.__module__,
                'event': {
                    'run': moduleConfig.get('run', crontabModule.run if hasattr(crontabModule, 'run') else None),
                    'onStart': moduleConfig.get('onStart',
                                                crontabModule.onStart if hasattr(crontabModule, 'onStart') else None),
                    'onError': moduleConfig.get('onError',
                                                crontabModule.onError if hasattr(crontabModule, 'onError') else None),
                    'onTasked': moduleConfig.get('onTasked',
                                                 crontabModule.onTasked if hasattr(crontabModule,
                                                                                   'onTasked') else None),
                }

            })
            crontabRunner().run(**config)
        except Exception as e:
            logger.console.error(f'An exception occurred while starting the crontab module [{name}]:{e}')
        return self
