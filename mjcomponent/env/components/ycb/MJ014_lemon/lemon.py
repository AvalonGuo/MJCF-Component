import os
from dm_control import mjcf

class Lemon:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ014_lemon', 'lemon.xml')
        self.mjcf_root = mjcf.from_path(path)