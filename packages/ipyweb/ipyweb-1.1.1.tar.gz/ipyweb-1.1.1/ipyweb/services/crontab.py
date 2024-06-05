from ipyweb.logger import logger
from ipyweb.process import process
from ipyweb.thread import thread
from ipyweb.utils import utils


class crontab():
    def run(self, **params):
        params = params.get('kwargs', {}) if params.get('kwargs', None) is not None else params
        crontabIpyweb()._run(params.get('config', {}))


class crontabIpyweb():
    _config = {}
    _event = {}
    _scheduler = None
    _job = None

    def _run(self, config={}):
        self._config = dict(self._config, **config)
        self._event = dict(self._event, **self._config.get('event', {}))
        try:
            self._start()
        except Exception as e:
            onError = self._event.get('onError', self._config.get('onError', None))
            if callable(onError): onError(e)

    def _startJob(self):
        taskSetting = self._config.get('taskSetting', {})
        if taskSetting.get('enable', False):
            run = crontabTasker(taskSetting)._run
        else:
            run = self._event.get('run', self._config.get('run', None))

        onStart = self._event.get('onStart', self._config.get('onStart', None))
        jobTrigger = utils.get(self._config, 'setting.jobTrigger', 'interval')
        jobParams = utils.get(self._config, 'setting.jobParams', {})
        if callable(run):
            self._job = self._scheduler.add_job(run, jobTrigger, kwargs=self._config, **jobParams)
            self._scheduler.start()
            if callable(onStart): onStart(self._scheduler, self._job)

    def _start(self):
        schedulerParams = utils.get(self._config, 'setting.schedulerParams', {})
        try:
            from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler

            if utils.get(self._config, 'setting.scheduler') == 'blocking':
                self._scheduler = BlockingScheduler(**schedulerParams)
            elif utils.get(self._config, 'setting.scheduler') == 'background':
                self._scheduler = BackgroundScheduler(**schedulerParams)
            else:
                self._scheduler = utils.get(self._config, 'setting.scheduler')
            if self._scheduler: self._startJob()

        except ImportError:
            logger.console.error('please install module: apscheduler(pip install apscheduler)')
        except KeyboardInterrupt:
            pass
        except Exception as e:
            logger.console.error(f'An exception occurred while adding the scheduled job:{e}')
        return self


class crontabTasker():
    _config = {}
    _onTasked = None

    def __init__(self, taskSetting={}):
        self._config = dict(self._config, **taskSetting)

    def _run(self, **config):
        self._onTasked = config.get('event', {}).get('onTasked', None)

        try:
            self._start()
        except Exception as e:
            logger.console.error(f'An exception occurred while executing the scheduled task:{e}')

    def _start(self):

        if self._config.get('default', '') == 'openUrl':
            self._openUrl()
        elif self._config.get('default', '') == 'exeCommand':
            self._exeCommand()
        elif self._config.get('default', '') == 'exePython':
            self._exePython()
        elif self._config.get('default', '') == 'invokeCall':
            self._invokeCall()

    def _openUrl(self):
        import requests
        config = self._config.get('openUrl', {})
        try:
            type = config.get('type', 'get')
            if 'type' in config:
                del config['type']
            if type == 'post':
                response = requests.post(**config)
            else:
                response = requests.get(**config)
            response.raise_for_status()
        except Exception as e:
            logger.console.error(f"An exception occurred while requesting access to the website:{e}")
        except requests.exceptions.HTTPError as e:
            logger.console.error(f"An exception occurred while requesting access to the website:{e}")
        except requests.exceptions.RequestException as e:
            logger.console.error(f"An exception occurred while requesting access to the website:{e}")
        else:
            if callable(self._onTasked): self._onTasked(response.text)

    def _exeCommand(self):
        try:
            config = self._config.get('exeCommand')
            runCommand = config.get('runCommand', [])
            if runCommand and len(runCommand) > 0:
                import subprocess
                runParams = dict({
                    'shell': utils.isWin(),
                    'check': True,
                    'text': True

                }, **config.get('runParams', {}))
                result = subprocess.run(runCommand, **runParams)
                if callable(self._onTasked): self._onTasked(result)
        except Exception as e:
            logger.console.error(f"An exception occurred while executing the command:{e}")

    def _exePython(self):
        try:
            exePython = self._config.get('exePython', '')
            if exePython:
                result = exec(exePython)
                if callable(self._onTasked): self._onTasked(result)
        except Exception as e:
            logger.console.error(f"An exception occurred while executing the pythonCommand:{e}")

    def _invokeCall(self):
        try:
            config = self._config.get('invokeCall')
            moduleName = config.get('module', '')
            className = config.get('class', '')
            methodName = config.get('method', 'process')
            methodParams = config.get('params', None)
            import importlib
            module = utils.smartImportModule(className, moduleName)
            print(hasattr(module, className), module, className, moduleName)
            if hasattr(module, className):
                classAttr = getattr(module, className)
                classInstance = classAttr()
                if hasattr(classInstance, methodName):
                    method = getattr(classInstance, methodName)
                    result = method(methodParams) if methodParams else method()
                    if callable(self._onTasked): self._onTasked(result)

        except Exception as e:
            print(type(e))
            logger.console.error(f"An exception occurred while executing the command:{e}")


class crontabRunner():

    def run(self, **config):
        """
             config = {
                'name':'socket',#队列名称 名称不能重复 否则以已存在的名称运行
                'daemon': True,  # 启动线程是否守护执行
                'block': False,  # 启动线程是否阻塞执行
                'usePool': False,  # 是否线程池启动
                'useProcess': False,  # 是否使用进程
                'max': 1,  # 启动线程数量
                'event':{
                   'run': run, #执行回调
                   'onStart':onStart, #开始回调
                   'onError': onError,#错误回调
                   'onTasked': onTasked,#任务已执行
                }
                'setting': { # 配置选项
                   'schedulerType': 'blocking',  #调度器类型 blocking:阻塞计划任务 background:非阻塞计划任务
                   'schedulerParams': {},# 调度器参数
                   'jobTrigger': 'interval',  # 任务触发类型  cron:定时任务  interval:间隔循环任务  date：在指定的时间点触发任务。
                   'jobParams': {  # 任务触发参数
                      'seconds': 3
                     }
                   },
                'taskSetting':{

                 }

               }
               """

        try:
            useProcess = config.get('useProcess', False)  # 默认线程
            usePool = config.get('usePool', False)  # 默认进程
            params = {
                'name': config.get('name', __name__),
                'target': crontab().run,
                'config': config
            }

            if useProcess:
                (process.runPool if usePool else process.run)(**params)
            else:
                (thread.runPool if usePool else thread.run)(**params)

        except Exception as e:
            logger.console.error(f'An exception occurred while starting  the crontab:{e}')
