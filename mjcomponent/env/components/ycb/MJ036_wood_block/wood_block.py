import os
from dm_control import mjcf

class Wood_block:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ036_wood_block', 'wood_block.xml')
        self.mjcf_root = mjcf.from_path(path)
