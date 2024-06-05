import json
import os
import sys
from urllib.parse import urlparse
from ipyweb.singleton import singleton


class utils(metaclass=singleton):

    @classmethod
    # 链式获取配置
    def get(self, configData={}, key='', default=None):
        try:
            if key == '':
                return configData;
            if '.' in key:
                keys = key.split('.')
                dict = configData
                for k in keys:
                    if k in dict:
                        dict = dict.get(k, default)
                    else:
                        return default  # 如果某个键不存在，返回None
                return dict
            else:
                return configData.get(key, default)
        except Exception as e:
            return configData

    def isModuleInstalled(name='') -> bool:
        try:
            import importlib
            importlib.import_module(name)
            return True
        except ImportError:
            return False

    @classmethod
    def pathExists(self, path='') -> bool:
        try:
            if os.path.exists(path):
                return True if os.path.isdir(path) else False
            else:
                return False
        except Exception:
            return False
        return False

    @classmethod
    def fileExists(self, filePath='') -> bool:
        try:
            if os.path.exists(filePath):
                return True if os.path.isfile(filePath) else False
            else:
                return False
        except Exception:
            return False
        return False

    @classmethod
    def tuple(self, data=(), index=0, default=None):
        try:
            return data[index]
        except IndexError:
            return default


    @classmethod
    def checkUrl(self, domain, port) -> bool:
        try:
            import socket
            socket.create_connection((domain, port), timeout=1).close()
            return True
        except socket.error as e:
            return False

    @classmethod
    def getDomainPortByUrl(self, url) -> tuple:
        parsed_url = urlparse(url)
        domain = parsed_url.hostname
        port = parsed_url.port
        if domain == None: domain = 'localhost'
        if port == None: port = 80
        return domain, port

    @classmethod
    def isUrl(self, url):
        import re
        url_pattern = re.compile(
            r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        )
        return bool(url_pattern.match(url))

    @classmethod
    def inJson(self, key, json) -> bool:
        return True if key in json else False

    @classmethod
    def isJson(self, strings='') -> bool:
        if isinstance(strings, str):
            try:
                isinstance(int(strings), int)
                return False
            except:
                pass
            try:
                json.loads(strings)
                return True
            except ValueError:
                return False
        else:
            return False

    @classmethod
    def isCls(self, cls=None) -> bool:
        try:
            return True if cls.__class__.name else False
        except Exception:
            return False

    @classmethod
    def isWin(self) -> bool:
        return self.os() == 'win'

    @classmethod
    def os(self) -> str:
        if sys.platform.startswith('win'):
            return 'win'
        elif sys.platform == 'darwin':
            return 'darwin'
        elif sys.platform.startswith('linux'):
            return 'linux'
        else:
            return 'other'

    @classmethod
    def smartImportModule(self, name='', modulePath='', rootPrefix='.', moduleFile=True):
        module = None
        import importlib
        try:
            module = importlib.import_module(modulePath)
        except ImportError as e:
            if moduleFile == True:
                try:
                    modulePath = modulePath.replace('.', '/') + '.py'
                    modulePath = os.path.normpath(f'{rootPrefix}/{modulePath}')
                    if self.fileExists(modulePath):
                        module_spec = importlib.util.spec_from_file_location(name, modulePath)

                        if module_spec:
                            module = importlib.util.module_from_spec(module_spec)
                            module_spec.loader.exec_module(module)
                except Exception as e:
                    print(f'An exception occurred while importing a module from a file [{modulePath}]:{e}')
        except Exception as e:
            print(f'An exception occurred while importing a module [{modulePath}]:{e}')
        return module
