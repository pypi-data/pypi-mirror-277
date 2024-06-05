
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'Ner_f533dfa9faf94057a2adf52178db3bc8.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
