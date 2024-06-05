import os, re
from ipyweb.app import app
from ipyweb.config import config
from ipyweb.logger import logger
from ipyweb.utils import utils
from ipyweb.event import event


class windows:

    def run(self, windowsParams={}, **event):
        self.windowsIpyweb = windowsIpyweb()
        return (
            self.windowsIpyweb._setParams(windowsParams)  # 设置参数
            ._setOnCreateReady(event.get('onCreateReady', None))  # 窗口创建之前
            ._setOnCreated(event.get('onCreated', None))  # 窗口创建成功
            ._setOnOpenReady(event.get('onOpenReady', None))  # 窗口打开之前
            ._setOnOpened(event.get('onOpened', None))  # 窗口打开成功
            ._run()
        )


class windowsIpyweb:
    _params = {
        'title': 'ipyweb',
        'url': '',
        'html': '',
        'width': 400,
        'height': 750,
        'x': None,
        'y': None,
        'resizable': False,
        'min_size': (400, 800),
        'text_select': False,
        'confirm_close': False,
        'on_top': False,
        'frameless': False,
        'easy_drag': False,
        'minimized': False,
        'shadow': False,
        'focus': False,
        'zoomable': False,
        'vibrancy': False,
        'background_color': '#FFFFFF',
        'transparent': False,
        'hidden': False,
        'fullscreen': False,
        'server': None,
        'server_args': {},

        'func': None,
        'args': None,
        'private_mode': False,
        'localization': {},
        'storage_path': '',
        'debug': False,
        'http_server': False,
        'http_port': 8080,
        'user_agent': None,
        'gui': '',
        'menu': [],
        'ssl': False
    }
    _createParams = {},
    _startParams = {}
    _supportWindowsParams = ['title', 'url', 'html', 'width', 'x', 'y', 'resizable', 'min_size', 'confirm_close',
                             'on_top',
                             'frameless',
                             'easy_drag', 'minimized', 'shadow', 'focus', 'zoomable', 'vibrancy', 'background_color',
                             'transparent', 'hidden', 'fullscreen', 'server', 'server_args', 'js_api']
    _supportStartsParams = ['func', 'args', 'private_mode', 'localization', 'storage_path', 'debug', 'http_server',
                            'http_port', 'user_agent', 'gui', 'menu', 'server', 'server_args', 'ssl']
    _tartget = {}
    _onCreateReady = None
    _onCreated = None
    _onOpenReady = None
    _onOpened = None
    name = 'main'
    windows = None

    def _checkGui(self):

        if config.get('windows.gui') == 'cef' and utils.os() == 'win':
            try:
                import cefpython3
            except ImportError:
                logger.console.error('please installer the module: cefpython3 (pip install cefpython3)')
                return False
        if config.get('windows.gui') == 'qt':
            try:
                from qtpy import QtCore
                from PySide2 import QtCore
            except ImportError:
                logger.console.error('please installer the module: ptqy and pyside2  (pip install ptqy pyside2)')
                return False
        if utils.os() == 'linux' and (config.get('windows.gui') == 'gtk' or config.get('windows.gui') == ''):
            try:
                import cairo, gi
            except ImportError:
                logger.console.error(
                    'please installer the module: pycairo and pygobject (pip install pycairo pygobject)')
                return False
        return True

    def _run(self):

        if self._checkGui() == False:
            return 'guiDriver module ImportError'

        self._parseParams()
        _checkParams = self._checkParams()
        if _checkParams != True and type(_checkParams) == str:
            return _checkParams
        try:

            try:
                import webview
            except ImportError:
                logger.console.error('please installer the module: ipywebview (pip install ipywebview)')
                return self
            event.emit('windows_createReady', self, name=self.name, windows=self.windows)  # 创建之前事件
            if callable(self._onCreateReady): self._onCreateReady(self)  # 创建之前回调
            if self._tartget.get('enable', False):
                self._createParams = dict(self._createParams, **{
                    "html": self._tartget.get('html', ''),
                    "url": self._tartget.get('url', ''),
                })
            self.windows = webview.create_window(**self._createParams)  # 创建窗口
            event.emit('windows_created', self, name=self.name, windows=self.windows)  # 创建成功事件
            if callable(self._onCreated): self._onCreated(self)  # 创建成功回调

            self._settingsUpdate()  # 设置窗口实例及更新配置
            self._startParams = dict(self._params, **{
                'func': self._onOpenedCallable,
                'args': self,
                'storage_path': os.path.normpath(f'{app.runtimePath}/{str(self._params.get("storage_path", "cache"))}'),
            })
            if callable(self._onOpenReady): self._onOpenReady(self)
            event.emit('windows_openReady', self, name=self.name, windows=self.windows)
            self._startParams = {k: v for k, v in self._startParams.items() if k in self._supportStartsParams}

            if self._tartget.get('enable', False):
                self._startParams = dict(self._startParams, **{
                    "http_server": False,
                })

            webview.start(**self._startParams)  # 启动窗口

        except Exception as e:
            msg = f'An exception occurred while opening the window [{self.name}] :{e}'
            logger.console.error(msg)
            return msg

    def _onOpenedCallable(self, winCls):
        event.emit('windows_opened', winCls, name=self.name, windows=self.windows)
        if callable(self._onOpened): self._onOpened(winCls)

    def setStartParams(self, startParams={}):
        self._startParams = dict(self._startParams, **startParams)
        return self

    def setCreateParams(self, createParams={}):
        self._createParams = dict(self._createParams, **createParams)
        return self

    def _parseParams(self):
        if self._params.get('target', False):
            self._tartget = {
                'enable': True,
                "html": self._params.get('html', ''),
                "url": self._params.get('url', ''),
                'http_server': False
            }
        self._createParams = {k: v for k, v in self._params.items() if k in self._supportWindowsParams}

        return self

    def _setParams(self, params={}):
        self._params = dict(self._params, **config.get('windows', {}))
        self.name = self._params.get('name', 'main')
        return self

    def _checkParams(self) -> bool or str:
        try:
            if self.name == '' or (self._tartget.get('enable', False) and self.name == 'main'):
                return f'The window name must be unique '
            self.name = re.sub(r'[^A-Za-z0-9]', '', self.name)
            if self.name == '':
                return f'The window name can only contain uppercase and lowercase letters and numbers'
        except Exception as e:
            return f'An exception occurred while detecting the window parameters:{e}'
        return True

    def _setOnOpenReady(self, onOpenReady=None):
        if callable(onOpenReady):
            self._onOpenReady = onOpenReady
        return self

    def _setOnCreateReady(self, onCreateReady=None):
        if callable(onCreateReady):
            self._onCreateReady = onCreateReady
        return self

    def _setOnCreated(self, onCreated=None):
        if callable(onCreated):
            self._onCreated = onCreated
        return self

    def _setOnOpened(self, onOpened=None):
        if callable(onOpened):
            self._onOpened = onOpened
        return self

    def _settingsUpdate(self):
        import webview
        webview_settings = self._params.get('webview_settings', {})
        if webview_settings and len(webview_settings):
            for key, value in webview_settings.items():
                webview.settings[key] = value
        if utils.isWin() and utils.isModuleInstalled('cefpython3') and config.get('windows.gui', '') == 'cef':
            # To pass custom settings to CEF, import and update settings dict
            # See the complete set of options for CEF, here: https://github.com/cztomczak/cefpython/blob/master/api/ApplicationSettings.md
            try:
                from webview.platforms.cef import settings, browser_settings
                settings.update(self._params.get('cef_settings', {}).get('settings', {}))
                browser_settings.update(self._params.get('cef_settings', {}).get('browser_settings', {}))
            except Exception as e:
                pass
