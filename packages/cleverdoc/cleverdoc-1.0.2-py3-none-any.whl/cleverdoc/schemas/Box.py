
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'Box_49f55431f01f4415b1cb527c204c2161.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
