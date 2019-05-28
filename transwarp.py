# transwarp.py

#数据库引擎对象

class _engine(object):
    def __init__(self,connect):
        self._connect = connect
    def connect(self):
        return self._connect()

engine = None

