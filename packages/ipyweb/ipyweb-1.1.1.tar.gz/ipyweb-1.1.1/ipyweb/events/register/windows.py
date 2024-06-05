from ipyweb.config import config


class windows():
    ipywebAutoConfig = {
        'enable': config.get('windows.guiDriverEnable', False),  # 是否关闭事件注册器
    }

    def createReady(self, eventName='', eventRegister=None):
        pass

    def created(self, eventName='', eventRegister=None):
        pass

    def openReady(self, eventName='', eventRegister=None):
        pass

    def opened(self, eventName='', eventRegister=None):
        pass
