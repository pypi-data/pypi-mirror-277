import asyncio


class socketClient:
    _socketWorker = None

    def connect(self, **params):
        self._socketWorker = socketWorker()
        self._socketWorker.connect(**params)
        return self


class socketWorker:
    setting = {
        'uri': '',
        'timeout': 10
    }

    websocket = None
    config = {}
    event = {}

    def connect(self, **params):
        self.config = dict(self.config, **params.get('config', {}))
        self.event = dict(self.event, **params.get('event', {}))
        self.setting = dict(self.setting, **params.get('setting', {}))
        asyncio.run(self._connect())

    async def _send(self, msg):
        if self.websocket:
            await  self.websocket.send(msg)
            return False
        return False

    async def _connect(self):

        onConnect = self.event.get('onConnect', self.config.get('onReady', None))
        onError = self.event.get('onError', self.config.get('onError', None))
        onClosed = self.event.get('onClosed', self.config.get('onClosed', None))
        import websockets as websocketClient
        try:
            async with websocketClient.connect(**self.setting) as websocket:
                self.websocket = websocket
                if callable(onConnect): await onConnect(websocket)
                await  self._onMesage()
                await websocket.wait_closed()
        except ConnectionRefusedError as e:
            if callable(onError): await onError(e)
        except ConnectionResetError as e:
            if callable(onError): await onError(e)
        except asyncio.TimeoutError as e:
            if callable(onError): await onError(e)
        except websocketClient.exceptions.ConnectionClosed:
            if callable(onClosed): await onClosed()
        except Exception as e:
            if callable(onError): onError(e)
        except KeyboardInterrupt:
            pass
        finally:
            if callable(onClosed): await onClosed()
        return self

    async def _onMesage(self):
        onMessage = self.event.get('onMessage', self.config.get('onMessage', None))
        onClosed = self.event.get('onClosed', self.config.get('onClosed', None))
        onError = self.event.get('onError', self.config.get('onReady', None))
        import websockets as websocketClient
        async for message in self.websocket:
            try:
                if callable(onMessage): await onMessage(message)
            except KeyboardInterrupt:
                pass
            except websocketClient.exceptions.ConnectionClosed:
                if callable(onClosed): await onClosed()
            except Exception as e:
                if callable(onError): onError(e)
        return self
