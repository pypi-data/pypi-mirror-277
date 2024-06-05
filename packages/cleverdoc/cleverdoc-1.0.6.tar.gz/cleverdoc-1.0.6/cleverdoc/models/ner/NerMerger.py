
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'NerMerger_b127b8acae484deb86072e07f531451d.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
