
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'ImageToPdf_180c2e3bcb3b4cbebe0718416c50f1c4.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
