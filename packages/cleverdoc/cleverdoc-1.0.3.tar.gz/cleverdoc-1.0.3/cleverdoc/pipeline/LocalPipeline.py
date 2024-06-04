
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'LocalPipeline_e74d57b5536443788757b3183ac86ce7.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
