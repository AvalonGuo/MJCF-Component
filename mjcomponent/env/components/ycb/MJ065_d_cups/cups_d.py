import os
from dm_control import mjcf

class Cups_d:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ065_d_cups', 'cups_d.xml')
        self.mjcf_root = mjcf.from_path(path)
