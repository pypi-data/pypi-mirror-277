
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'NerLLM_38fb7d5d344c430c8de2ed9c79675588.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
