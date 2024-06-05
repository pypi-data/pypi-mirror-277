
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'PdfAssembler_4ff0d866936b4a419d4835d28c8af17b.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
