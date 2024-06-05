
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'license_4db04a3c9c2247bab874712ede248d4a.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
