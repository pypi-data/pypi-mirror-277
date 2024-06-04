
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'enums_0e5cea58090545809976ec7f56347d20.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
