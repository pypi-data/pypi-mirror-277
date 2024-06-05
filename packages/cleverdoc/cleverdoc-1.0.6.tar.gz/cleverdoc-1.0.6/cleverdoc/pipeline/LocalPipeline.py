
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'LocalPipeline_34f7497be1d04a85897dda5354cb106d.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
