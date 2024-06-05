
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'enums_6e4685167b9244e8bde0c50c5a35cf3a.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
