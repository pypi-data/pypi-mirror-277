
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'NerOutput_f7b0a51ac5814e3c833e85e39128e022.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
