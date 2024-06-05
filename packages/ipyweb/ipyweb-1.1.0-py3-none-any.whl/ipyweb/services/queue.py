import multiprocessing
import queue as pyqueue
from ipyweb.logger import logger
from ipyweb.process import process
from ipyweb.thread import thread


class queue():
    queueIpyweb = None
    queue = None
    thread = None

    def run(self, config={}):
        self.queueIpyweb = queueIpyweb()
        self.queueIpyweb.run(config, self)
        self.queue = self.queueIpyweb._queue
        self.thread = self.queueIpyweb._thread
        return self

    def stop(self):
        self.queueIpyweb.stop()
        return self

    def add(self, **task):
        return self.queueIpyweb._add(**task)

    def clear(self):
        return self.queueIpyweb._clear()

    def size(self):
        return self.queueIpyweb._size()

    def empty(self):
        return self.queueIpyweb._empty()

    def full(self):
        return self.queueIpyweb._full()

    def qsize(self):
        return self.queueIpyweb._qsize()

    def remove(self, name=''):
        return self.queueIpyweb._remove(name)


class queueIpyweb():
    _name = 'default'
    _config = {}
    _event = {}
    _setting = {}
    _queue = None
    _thread = None
    _userQueue = None
    _runnding = True

    def run(self, config={}, userQueue=None):
        self._userQueue = userQueue
        self._config = dict(self._config, **config)
        self._setting = dict(self._setting, **self._config.get('setting', {}))
        self._event = dict(self._event, **self._config.get('event', {}))
        self._name = self._config.get('name', __name__)
        self._setQueue()
        return self

    def stop(self):
        self._runnding = False
        return self

    def _remove(self, name=''):
        count = 0  # 删除个数
        queue = self._getQueue()
        try:
            newItems = []
            while not queue.empty():
                taskTuple = queue.get()
                if name and taskTuple[0] != name:
                    newItems.append(taskTuple)
                else:
                    count += 1
            for taskTuple in newItems:
                queue.put(
                    (taskTuple[0], taskTuple[1]),
                    block=self._setting.get('putBlock', False),
                    timeout=self._setting.get('putTimeout', None)
                )
        except pyqueue.Full:
            onFull = self._event.get('onFull', self._config.get('onFull', None))
            if callable(onFull): onFull()
        except Exception as e:
            msg = f"An exception occurred while deleting the queue: {e}"
            onError = self._event.get('onError', self._config.get('onError', None))
            if callable(onError): onError(msg, e)
            logger.console.error(msg)
        return count

    def _clear(self):
        queue = self._getQueue()
        count = 0
        try:
            while not queue.empty():
                queue.get()
                count += 1
        except Exception as e:
            msg = f"An exception occurred while clearing the queue: {e}"
            onError = self._event.get('onError', self._config.get('onError', None))
            if callable(onError): onError(msg, e)
            logger.console.error(msg)
        return count

    def _add(self, **task):
        name = task.get('name', '')
        if name == '':
            return False
        res = False
        try:
            self._getQueue().put((name, task))
            res = True
        except pyqueue.Full:
            onFull = self._event.get('onFull', self._config.get('onFull', None))
            if callable(onFull): onFull()
        except Exception as e:
            msg = f"An exception occurred while adding the queue: {e}"
            onError = self._event.get('onError', self._config.get('onError', None))
            if callable(onError): onError(msg, e)
            logger.console.error(msg)
        return res

    def _setQueue(self):
        try:
            if self._setting.get('queueType', '') == 'PriorityQueue':
                self.queue = pyqueue.PriorityQueue(maxsize=self._setting.get('maxsize', 0))
            elif self._setting.get('queueType', '') == 'LifoQueue':
                self.queue = pyqueue.LifoQueue(maxsize=self._setting.get('maxsize', 0))
            elif self._setting.get('queueType', '') == 'ProcessQueue':
                self.queue = multiprocessing.Manager().Queue(maxsize=self._setting.get('maxsize', 0))
            else:
                self.queue = pyqueue.Queue(maxsize=self._setting.get('maxsize', 0))

            useProcess = self._config.get('useProcess', False)
            usePool = self._config.get('usePool', True)
            params = dict({
                'name': self._name,
                'target': self._run,
                'config': self._config
            })
            if useProcess:
                (process.runPool if usePool else process.run)(**params)
            else:
                (thread.runPool if usePool else thread.run)(**params)

            onStart = self._event.get('onStart', self._config.get('onStart', None))
            if callable(onStart): onStart(self._userQueue)
            logger.console.info(f"Queue [{self._name}] has been started")
        except Exception as e:
            msg = f"An exception occurred while starting  the queue: {e}"
            onError = self._event.get('onError', self._config.get('onError', None))
            if callable(onError): onError(msg, e)
            logger.console.error(msg)

        return self

    def _getQueue(self):
        if self.queue is None:
            self._setQueue()
        return self.queue

    def _run(self, **kwargs):
        while self._runnding == True:
            queue = self._getQueue()
            try:
                taskTuple = queue.get(
                    block=self._setting.get('getBlock', True),
                    timeout=self._setting.get('getTimeout', None)
                )
                if len(taskTuple) == 2:
                    onRecv = self._event.get('onRecv', self._config.get('onRecv', None))
                    if callable(onRecv): onRecv(taskTuple[1])
                    run = self._event.get('run', None)
                    if callable(run):
                        run(taskTuple[1])
                    if hasattr(queue, 'task_done'): queue.task_done()
            except pyqueue.Empty:
                onEmpty = self._event.get('onEmpty', self._config.get('onEmpty', None))
                if callable(onEmpty): onEmpty()
            except BrokenPipeError as e:
                pass
            except EOFError as e:
                pass
            except Exception as e:
                msg = f"An exception occurred while executing  the queue: {e}"
                onError = self._event.get('onError', self._config.get('onError', None))
                if callable(onError): onError(msg, e)
                if self._setting.get('excepTaskDone', True):
                    try:
                        if hasattr(queue, 'task_done'): queue.task_done()
                    except Exception:
                        pass
                logger.console.debug(msg)

    def _size(self):
        return self._getQueue().qsize()

    def _qsize(self):
        return self._getQueue().qsize()

    def _full(self):
        return self._getQueue().full()

    def _empty(self):
        return self._getQueue().empty()


class queueRunner():

    def run(self, **config):
        """
             config = {
                'name':'socket',#队列名称 名称不能重复 否则以已存在的名称运行
                'daemon': True,  # 是否守护执行
                'block': False,  # 是否阻塞执行
                'max': 1,  # 进程池或线程池数量
                'useProcess': False,  # 是否使用独立进程 默认独立线程
                'usePool': True,  # 是否线程池或进程池,
                'event':{
                   'run': run, #执行回调
                   'onStart': onStart, #队列已启动
                   'onRecv':onRecv, #收到任务
                   'onEmpty': onEmpty,#队列为空
                   'onFull': onFull,#队列已满
                   'onError': onError#发生异常
                }
             }
               """

        try:
            queue().run(config)
        except Exception as e:
            logger.console.error(f'An exception occurred while starting  the queue:{e}')
