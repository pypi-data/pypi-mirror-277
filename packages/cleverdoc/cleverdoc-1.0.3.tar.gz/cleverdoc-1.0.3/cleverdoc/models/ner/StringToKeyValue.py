
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'StringToKeyValue_26de7d9d038e499494cb28303532a624.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
