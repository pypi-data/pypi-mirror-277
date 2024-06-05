
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'Ner_2372062068b04b17b3deeaab2eaff1cb.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
