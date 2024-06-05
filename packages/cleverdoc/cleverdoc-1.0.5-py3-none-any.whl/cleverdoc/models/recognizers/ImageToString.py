
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'ImageToString_9b5f5ddd826b41f5a1dc7f122a94d1fd.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
