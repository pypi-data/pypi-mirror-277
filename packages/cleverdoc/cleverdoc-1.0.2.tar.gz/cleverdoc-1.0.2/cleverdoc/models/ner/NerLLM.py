
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'NerLLM_8e51ac074b2c408380ad3e4afde5d60e.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
