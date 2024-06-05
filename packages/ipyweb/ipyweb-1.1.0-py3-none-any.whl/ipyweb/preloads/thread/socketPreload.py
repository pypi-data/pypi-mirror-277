from ipyweb.app import app
from ipyweb.config import config
from ipyweb.logger import logger
from ipyweb.service import service
from ipyweb.contracts.ipywebPreload import ipywebPreload


class socketPreload(ipywebPreload):
    # preload加载此模块时调用的配置信息
    ipywebAutoConfig = {
        'enable': True,  # 是否关闭运行
        # 启动节点 True:窗口打开后 False:窗口打开前 默认 False
        'windowsOpen': config.get('app.preload.socketPreloadAtWindowsOpen', False),
        'daemon': True,  # 是否守护执行 默认True
        'block': False,  # 是否阻塞执行 默认False
        'max': 1,  # 进程池或线程池数量 默认1
        'usePool': False,  # 是否线程池 默认False
    }
    sockets = {}

    def run(self, **kwargs):
        self.load()
        return self

    def load(self):
        self._loadFromSockets(f'{app.ipywebPath}.{app.socketsName}')
        if config.get('app.autoLoad.loadSoccketsEnable', False) == True:
            self._loadFromSockets(f'{app.appPath}.{app.socketsName}')

        try:
            for name, module in self.sockets.items():
                moduleConfig = getattr(module, app.ipywebAutoConfigName, {})
                if moduleConfig.get('enable', False) == True: self.socketRun(module, moduleConfig, module)
        except Exception as e:
            logger.console.error(f'An exception occurred while reading the socket dirs:{e}')
        return self

    def _loadFromSockets(self, path=''):
        try:
            modules = service.module(path)
            for name, module in modules.items():
                self.sockets[name] = module
        except Exception as e:
            logger.console.error(f'An exception occurred while reading the socket module:{e}')
        return self

    def socketRun(self, module=None, moduleConfig={}, socketServe=None):
        try:
            from ipyweb.services.socketServer import socketServerRunner
            config = dict(moduleConfig, **{
                'name': module.__module__,
                'event': {
                    'onStart': moduleConfig.get('onStart',
                                                socketServe.onStart if hasattr(socketServe, 'onStart') else None),
                    'onStop': moduleConfig.get('onStop',
                                               socketServe.onStop if hasattr(socketServe, 'onStop') else None),
                    'onServe': moduleConfig.get('onServe',
                                                 socketServe.onServe if hasattr(socketServe, 'onServe') else None),
                    'onConnect': moduleConfig.get('onConnect',
                                                  socketServe.onConnect if hasattr(socketServe, 'onConnect') else None),
                    'onError': moduleConfig.get('onError',
                                                socketServe.onError if hasattr(socketServe, 'onError') else None),
                    'onClosed': moduleConfig.get('onClosed',
                                                 socketServe.onClosed if hasattr(socketServe, 'onClosed') else None),
                    'onMessage': moduleConfig.get('onMessage',
                                                  socketServe.onMessage if hasattr(socketServe, 'onMessage') else None),
                }
            })
            socketServerRunner().run(**config)
        except Exception as e:
            logger.console.error(f'An exception occurred while starting the socket module :{e}')
        return self
