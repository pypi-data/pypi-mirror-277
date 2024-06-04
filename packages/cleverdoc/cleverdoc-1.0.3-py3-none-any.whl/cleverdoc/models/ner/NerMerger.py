
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'NerMerger_7254ce3dac864743a77ac476bfb5694b.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
