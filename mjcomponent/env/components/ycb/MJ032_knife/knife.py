import os
from dm_control import mjcf

class Knife:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ032_knife', 'knife.xml')
        self.mjcf_root = mjcf.from_path(path)
