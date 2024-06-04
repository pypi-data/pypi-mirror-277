
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'SingleImageToPdf_f9857f76e14444baa8a06fee68dfa21c.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
