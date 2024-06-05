from ipyweb.config import config


class windows():
    ipywebAutoConfig = {
        'enable': config.get('windows.guiDriverEnable', False),  # 是否关闭事件监听
    }

    def windows_createReady(self, winCls, **kwargs):
        pass

    def windows_created(self, winCls, **kwargs):
        pass

    def windows_openReady(self, winCls, **kwargs):
        pass

    def windows_opened(self, winCls, **kwargs):
        pass
