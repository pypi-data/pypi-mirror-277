
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'params_f99e788ac8d145aca451a257cd58c10a.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
