
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'LocalPipeline_16526ebccb404c60a3c5cb89ea096bda.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
