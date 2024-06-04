
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'ImageToString_4f7c084b0de14c5cb7e7917f6a33678c.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
