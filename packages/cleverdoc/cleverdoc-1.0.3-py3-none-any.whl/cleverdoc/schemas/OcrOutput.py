
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'OcrOutput_ac76e0de77cd4c81a80623d70c86b682.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
