import os
import asyncio

import websockets

from ipyweb.logger import logger
from ipyweb.process import process
from ipyweb.singleton import singleton
from ipyweb.thread import thread


class socketServer(metaclass=singleton):

    @classmethod
    def run(self, *args, **params):
        # pool版携带参数嵌套kwargs
        params = params.get('kwargs', {}) if params.get('kwargs', None) is not None else params
        return socketWorker._run(**params)

    @classmethod
    async def sendToAll(self, msg, client_ids=None, exclude_client_id=None):
        return await socketWorker._sendToAll(msg, client_ids, exclude_client_id)

    @classmethod
    async def sendToClient(self, client_id, msg):
        return await socketWorker._sendToClient(client_id, msg)

    @classmethod
    async def sendToUid(self, uid, msg):
        return await socketWorker._sendToUid(uid, msg)

    @classmethod
    async def sendToGroup(self, group, msg, client_ids=None, exclude_client_id=None):
        return await socketWorker._sendToGroup(group, msg, client_ids, exclude_client_id)

    @classmethod
    def broadcast(self, msg, connections=None):
        return socketWorker._broadcast(msg, connections)

    @classmethod
    async def closeClient(self, client_id):
        return await socketWorker._closeClient(client_id)

    @classmethod
    def isOnline(self, client_id):
        return socketWorker._isOnline(client_id)

    @classmethod
    def bindUid(self, client_id, uid):
        return socketWorker._bindUid(client_id, uid)

    @classmethod
    def unbindUid(self, client_id, uid):
        return socketWorker._unbindUid(client_id, uid)

    @classmethod
    def isUidOnline(self, uid):
        return socketWorker._isUidOnline(uid)

    @classmethod
    def getClientIdByUid(self, uid):
        return socketWorker._getClientIdByUid(uid)

    @classmethod
    def getUidByClientId(self, client_id):
        return socketWorker._getUidByClientId(client_id)

    @classmethod
    def joinGroup(self, client_id, group):
        return socketWorker._joinGroup(client_id, group)

    @classmethod
    def leaveGroup(self, client_id, group):
        return socketWorker._leaveGroup(client_id, group)

    @classmethod
    def leaveGroups(self, client_id):
        return socketWorker._leaveGroups(client_id)

    @classmethod
    def delGroup(self, group):
        return socketWorker._delGroup(group)

    @classmethod
    def getClientIdListByGroup(self, group):
        return socketWorker._getClientIdListByGroup(group)

    @classmethod
    def getUidListByGroup(self, group):
        return socketWorker._getUidListByGroup(group)

    @classmethod
    def getAllGroupIdList(self):
        return socketWorker._getAllGroupIdList()

    @classmethod
    def getAllUidList(self):
        return socketWorker._getAllUidList()

    @classmethod
    def getAllClientIdList(self):
        return socketWorker._getAllClientIdList()

    @classmethod
    def getConnections(self):
        return socketWorker._connections

    @classmethod
    def getConnectionByClientId(self, client_id):
        return socketWorker._getConnectionByClientId(client_id)

    @classmethod
    def getConnectionByClientIds(self, client_ids):
        return socketWorker._getConnectionByClientIds(client_ids)


class socketWorker(metaclass=singleton):
    _connections = {}
    _client_ids = set()
    _uids = {}
    _groups = {}
    _name = ''
    _config = {}
    _setting = {
        'host': 'localhost',
        'port': 8765
    }
    _event = {}
    _logUseTxt = ''

    @classmethod
    def _run(self, **params):

        self._name = params.get("name", "")
        self._config = dict(self._config, **params.get('config'))
        self._setting = dict(self._setting, **self._config.get('setting', {}))
        self._event = dict(self._event, **self._config.get('event', {}))
        useProcess = 'process' if self._config.get("useProcess", True) else 'thread'
        usePool = 'pool' if self._config.get("usePool", True) else ''
        self._logUseTxt = f'{useProcess}{usePool}'
        if self._setting.get('autoKill', True): self._autoKillPort()
        asyncio.run(self._startWoker())
        return self

    @classmethod
    async def _startWoker(self):
        onStart = self._event.get('onStart', self._config.get('onStart', None))
        if callable(onStart): await onStart(socketServer)
        try:
            await  self._runServe()
        except OSError as e:
            if e.errno == 10048 and self._setting.get('autoKill', True):
                logger().console.debug(f'Socket [{self._name}] port is occupied')
                self._autoKillPort()
                await self._runServe()
            else:
                logger().console.error(
                    f'An exception occurred while killing the socket [{self._name}] process:{e} ')
            onError = self._event.get('onError', self._config.get('onError', None))
            if callable(onError): await onError(e)
        except KeyboardInterrupt:
            pass
        except Exception as e:
            logger().console.error(
                f'An exception occurred while starting the socket [{self._name}] using  {self._logUseTxt}:{e} ')
            onError = self._event.get('onError', self._config.get('onError', None))
            if callable(onError): await onError(e)
        finally:
            onStop = self._event.get('onStop', self._config.get('onStop', None))
            if callable(onStop): await onStop(socketServer)

    @classmethod
    async def _runServe(self):

        try:
            import websockets
            import psutil
        except ImportError:
            logger.console.error('please installer the module: websockets and psutil (pip install websockets psutil)')
            return self

        serveConfig = dict(self._config.get('serveConfig', {}), **{
            'ws_handler': lambda wss, path: self._onMessage(wss, path),
            'host': self._setting.get('host'),
            'port': self._setting.get('port'),
        })

        if self._setting.get('ssl', False) and self._setting.get('serveConfig', {}).get('ssl', None) is None:
            import ssl
            from webview import generate_ssl_cert
            ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            keyfile, certfile = generate_ssl_cert()
            ssl_context.load_cert_chain(certfile=certfile, keyfile=keyfile)
            serveConfig['ssl'] = ssl_context
        async with websockets.serve(**serveConfig) as server:
            logger().console.info(
                f'Socket [{self._name}][ws://{self._setting.get("host")}:{self._setting.get("port")}] use [{self._logUseTxt}] has been started [PID:{os.getpid()}]')
            onServe = self._event.get('onServe', self._config.get('onServe', None))
            if callable(onServe): await onServe(server)
            await server.wait_closed()

    @classmethod
    async def _onMessage(self, websocket, path):
        client_id = id(websocket)
        if client_id not in self._connections:
            self._client_ids.add(client_id)
            self._connections[client_id] = websocket
            onConnect = self._event.get('onConnect', self._config.get('onConnect', None))
            header = websocket.request_headers._dict
            header['remote_ip'] = websocket.remote_address[0]
            if callable(onConnect): await onConnect(path, header, client_id)

        onMessage = self._event.get('onMessage', self._config.get('onMessage', None))
        try:
            async for message in websocket:
                try:
                    if callable(onMessage): await onMessage(message, id(websocket))
                except Exception as e:
                    onError = self._event.get('onError', self._config.get('onError', None))
                    if callable(onError):
                        await onError(e)
        except websockets.ConnectionClosedOK:
            pass
        except websockets.exceptions.ConnectionClosedError:
            pass
        except websockets.ConnectionClosed:
            await self._onClosed(websocket)

        except KeyboardInterrupt:
            pass
        except Exception as e:
            onError = self._event.get('onError', self._config.get('onError', None))
            if callable(onError): await onError(e)
        finally:
            await self._onClosed(websocket)

    @classmethod
    async def _onClosed(self, websocket):

        client_id = id(websocket)
        if id(websocket) in self._connections:
            del self._connections[client_id]
        self._client_ids.remove(client_id)
        uid = self._getUidByClientId(client_id)
        self._unbindUid(client_id, uid)
        self._leaveGroups(client_id)

        onClosed = self._event.get('onClosed', self._config.get('onClosed', None))
        if callable(onClosed): await onClosed(client_id)

    @classmethod
    def _joinGroup(self, client_id, group) -> bool:
        if group not in self._groups:
            self._groups[group] = set()
        if client_id: self._groups[group].add(client_id)

        return True

    @classmethod
    def _leaveGroups(self, client_id) -> bool:
        self._groups = {k: v for k, v in self._groups.items() if client_id not in v}
        self._groups = {k: v for k, v in self._groups.items() if v}
        return True

    @classmethod
    def _leaveGroup(self, client_id, group) -> bool:
        self._groups = {
            key: (value - {client_id}) if key == group else value
            for key, value in self._groups.items()
        }
        if not self._groups.get(group, set()): del self._groups[group]

        return True

    @classmethod
    def _delGroup(self, group) -> bool:
        if group in self._groups:
            del self._groups[group]
            return True
        return False

    @classmethod
    def _isUidOnline(self, uid):
        return uid in self._uids

    @classmethod
    def _unbindUid(self, client_id, uid) -> bool:
        self._uids = {
            key: (value - {client_id}) if key == uid else value for key, value in self._uids.items()
        }
        return True

    @classmethod
    def _bindUid(self, client_id, uid) -> bool:
        if uid not in self._uids:
            self._uids[uid] = set()
        self._uids[uid].add(client_id)
        return True

    @classmethod
    def _getUidByClientId(self, client_id):
        return next((key for key, value in self._uids.items() if client_id in value), None)

    @classmethod
    def _getClientIdByUid(self, uid):
        return self._uids.get(uid, 0)

    @classmethod
    def _getAllUidList(self) -> dict:
        return self._uids

    @classmethod
    def _getAllGroupIdList(self):
        return set(self._groups.keys())

    @classmethod
    def _getClientIdListByGroup(self, group) -> set:
        return self._groups.get(group, set())

    @classmethod
    def _getUidListByGroup(self, group) -> set:
        clientIds = self._groups.get(group, set())
        uids = {key for key, value_set in self._uids.items() if
                any(value in value_set for value in clientIds)}
        return uids

    @classmethod
    def _getAllClientIdList(self) -> set:
        return self._client_ids

    @classmethod
    def _isOnline(self, client_id) -> bool:
        return client_id in self._client_ids

    @classmethod
    def _getConnectionByClientId(self, client_id):
        return self._connections.get(client_id, None)

    @classmethod
    def _getConnectionByClientIds(self, client_ids):
        if client_ids is None or type(client_ids) != set:
            client_ids = set()
        return {self._connections[key] for key in client_ids if key in self._connections}

    @classmethod
    async def closeClientId(self, client_id) -> bool:
        if client_id not in self._connections:
            self._connections[client_id].close()
            return True
        return False

    @classmethod
    async def _sendToGroup(self, group, msg, client_ids=None, exclude_client_id=None) -> bool:
        if client_ids is None or type(client_ids) != set:
            client_ids = set()
        if exclude_client_id is None or type(exclude_client_id) != set:
            exclude_client_id = set()
        groupClientIds = self._groups.get(group, set())
        sendConnects = self._getConnectionByClientIds(groupClientIds)
        if len(client_ids) > 0:
            sendConnects = self._getConnectionByClientIds(client_ids)
        if len(exclude_client_id) > 0:
            sendConnects = sendConnects - self._getConnectionByClientIds(client_ids)
        websockets.broadcast(sendConnects, msg)
        return False

    @classmethod
    async def _sendToUid(self, uid, msg) -> bool:
        clients = self._uids.get(uid, set())
        sendConnects = self._getConnectionByClientIds(clients)
        websockets.broadcast(sendConnects, msg)
        return True

    @classmethod
    async def _sendToClient(self, client_id, msg) -> bool:
        if client_id in self._connections:
            await  self._connections[client_id].send(msg)
            return True
        return False

    @classmethod
    async def _sendToAll(self, msg, client_ids=None, exclude_client_id=None) -> int:
        if client_ids is None or type(client_ids) != set:
            client_ids = set()
        if exclude_client_id is None or type(client_ids) != set:
            exclude_client_id = set()
        sendConnects = self._connections.values()
        if len(client_ids) > 0:
            sendConnects = self._getConnectionByClientIds(client_ids)
        if len(exclude_client_id) > 0:
            sendConnects = sendConnects - self._getConnectionByClientIds(client_ids)
        websockets.broadcast(sendConnects, msg)
        return len(sendConnects)

    @classmethod
    async def _closeClient(self, client_id) -> bool:
        if client_id in self._connections:
            await  self._connections[client_id].close()
            return True
        return False

    @classmethod
    async def _broadcast(self, msg, connections=None):
        if connections is None:
            connections = self._connections.values()
        websockets.broadcast(connections, msg)
        return True

    @classmethod
    def _autoKillPort(self):
        try:
            port = self._setting.get('port')
            if port and porter.isPort(port) and self._setting.get('autoKill', True):
                porter.closePort(port)
        except Exception:
            pass
        return self


class socketServerRunner():
    @classmethod
    def run(self, **config):
        """
             config = {
                'name':'socket',#socket名称 名称不能重复 否则以已存在的名称运行
                'daemon': True,  # 是否守护执行
                'block': False,  # 是否阻塞执行
                'max': 1,  # 进程池或线程池数量
                'useProcess': False,  # 是否使用独立进程 默认独立线程
                'usePool': True,  # 是否线程池或进程池,
                'event':{
                    'onStart': onStart, #启动连接
                    'onStop': onStop, #结束事件
                    'onServe': onServe, #服务事件
                    'onConnect':onConnect, #连接事件
                    'onError': onError,#错误事件
                    'onClosed': onClosed,#关闭事件
                    'onMessage': onMessage#消息事件
                }
                'setting':{
                    'host': 'localhost',  # 服务地址
                    'port': 8765,  # 服务端口
                    'ssl': False,  # 是否开启wss
                    'autoKill': True,  # 端口被占用时自动杀死进程 建议开启 进程不能有效关闭时该功能有效果
                    'serveConfig': {}
                }
             }
               """

        try:
            useProcess = config.get('useProcess', False)
            usePool = config.get('usePool', False)
            params = dict({
                'name': config.get('name', __name__),
                'target': socketServer().run,
                'config': config
            })

            if useProcess:
                (process.runPool if usePool else process.run)(**params)
            else:
                (thread.runPool if usePool else thread.run)(**params)

        except Exception as e:
            logger.console.error(f'An exception occurred while starting the socket:{e}')


class porter:

    @classmethod
    def closePort(self, port):
        pid = 0
        try:
            process_info = self.findProcessByPort(port)
            if process_info:
                pid = process_info['pid']
                self.killPid(pid)
        except Exception as e:
            pass
        return pid

    @classmethod
    def killPid(self, pid, myself=False):
        try:
            if os.getpid() != pid or (myself == True and os.getpid() == pid):
                os.kill(pid, 9)
        except OSError:
            pass

    @classmethod
    def findProcessByPort(self, port):
        import psutil
        for proc in psutil.process_iter(['pid', 'name']):
            for conn in proc.connections():
                if conn.laddr[1] == port:
                    return proc.info
        return None

    @classmethod
    def isPort(self, port, host='127.0.0.1') -> bool:
        import socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.connect((host, port))
                return True
            except ConnectionRefusedError:
                return False
