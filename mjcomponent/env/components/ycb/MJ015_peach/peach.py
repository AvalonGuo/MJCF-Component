import os
from dm_control import mjcf

class Peach:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ015_peach', 'peach.xml')
        self.mjcf_root = mjcf.from_path(path)