
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'BinaryToImage_48ad1995ea734b339d791cc845cea83e.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
