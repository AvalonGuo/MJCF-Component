import os
from dm_control import mjcf

class Cups_f:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ065_f_cups', 'cups_f.xml')
        self.mjcf_root = mjcf.from_path(path)
