
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'SingleImageToPdf_2c704c1f242c4077ade2a554d48e32fe.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
