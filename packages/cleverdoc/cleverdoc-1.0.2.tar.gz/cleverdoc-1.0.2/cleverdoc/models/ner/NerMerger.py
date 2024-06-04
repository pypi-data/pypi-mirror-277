
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'NerMerger_8e154d61fb7f481394f47f015802d982.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
