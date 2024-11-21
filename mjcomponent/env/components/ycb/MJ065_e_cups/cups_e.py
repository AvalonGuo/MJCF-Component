import os
from dm_control import mjcf

class Cups_e:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ065_e_cups', 'cups_e.xml')
        self.mjcf_root = mjcf.from_path(path)
