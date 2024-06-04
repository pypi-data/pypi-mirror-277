
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'enums_18575b18f81a403cad7504e861e1121a.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
