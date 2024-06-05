from ipyweb.contracts.ipywebPreload import ipywebPreload


class examplePreload(ipywebPreload):
    # preload加载此模块时调用的配置信息
    ipywebAutoConfig = {
        'enable': False,  # 是否关闭运行
        'windowsOpen': False,  # 启动节点 True:窗口打开后 False:窗口打开前 默认 False
        'daemon': True,  # 是否守护执行 默认True
        'block': False,  # 是否阻塞执行 默认False
        'max': 10,  # 进程池或线程池数量 默认1
        'usePool': True,  # 是否线程池 默认False
    }
    queues = {}

    def run(self, **kwargs):
        return self
