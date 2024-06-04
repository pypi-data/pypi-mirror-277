
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'SingleImageToPdf_221a0232fa514b10aa3bae0bd194d41d.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
