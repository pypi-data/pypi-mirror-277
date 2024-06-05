
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'Box_df4269761d0f472b9e641ec79611e00e.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
