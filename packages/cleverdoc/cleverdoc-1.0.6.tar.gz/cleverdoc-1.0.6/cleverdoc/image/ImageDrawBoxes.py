
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'ImageDrawBoxes_f92df27e05c045c5a5b97e22436c5ba5.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
