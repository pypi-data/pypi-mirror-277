
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'NerMerger_cb26194ff65e4141864a8970c687ebae.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
