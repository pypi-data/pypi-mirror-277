
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'NerLLM_5d34cf9aa2924b3c85a97d9d858d52b6.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
