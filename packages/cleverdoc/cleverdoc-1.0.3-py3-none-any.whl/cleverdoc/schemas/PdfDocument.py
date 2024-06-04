
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'PdfDocument_b11c5b78c7ff48f792ccdf582f5e25cb.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
