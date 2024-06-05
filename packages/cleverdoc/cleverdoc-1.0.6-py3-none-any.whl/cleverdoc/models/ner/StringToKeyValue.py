
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'StringToKeyValue_a04e025af09c491d9513ac7250471713.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
