import os
from dm_control import mjcf

class Mug:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ025_mug', 'mug.xml')
        self.mjcf_root = mjcf.from_path(path)