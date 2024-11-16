import os
from dm_control import mjcf

class Plum:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ018_plum', 'plum.xml')
        self.mjcf_root = mjcf.from_path(path)