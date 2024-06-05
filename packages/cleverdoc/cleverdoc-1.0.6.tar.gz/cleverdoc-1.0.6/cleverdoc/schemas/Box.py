
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'Box_9ee77bb5c4564ea683e72d5042758466.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
