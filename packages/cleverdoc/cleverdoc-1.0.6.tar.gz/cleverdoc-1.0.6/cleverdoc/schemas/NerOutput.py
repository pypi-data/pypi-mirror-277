
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'NerOutput_846c3c8b0eb64e73bebffaeb31560e94.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
