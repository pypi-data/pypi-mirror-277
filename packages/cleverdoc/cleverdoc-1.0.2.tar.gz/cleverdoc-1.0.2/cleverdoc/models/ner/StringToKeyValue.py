
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'StringToKeyValue_09a9dd2fa66d4e679a39b9d5abb8ffab.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
