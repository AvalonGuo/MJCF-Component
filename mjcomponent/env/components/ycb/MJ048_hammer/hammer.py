import os
from dm_control import mjcf

class Hammer:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ048_hammer', 'hammer.xml')
        self.mjcf_root = mjcf.from_path(path)
