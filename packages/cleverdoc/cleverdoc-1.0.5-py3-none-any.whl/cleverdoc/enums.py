
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'enums_64266823e1b0472b800c6f27a6ace4ed.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
