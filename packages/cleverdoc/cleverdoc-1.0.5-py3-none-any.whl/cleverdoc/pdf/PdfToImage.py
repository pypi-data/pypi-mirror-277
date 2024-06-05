
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'PdfToImage_08d5dca8125440529845ccad8c5e0c67.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
