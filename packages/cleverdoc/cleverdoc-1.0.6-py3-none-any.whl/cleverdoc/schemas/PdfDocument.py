
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'PdfDocument_76d17b281e30421db714e0a28dd5a2eb.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
