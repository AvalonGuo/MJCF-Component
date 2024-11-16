import os
from dm_control import mjcf

class Sponge:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ026_sponge', 'sponge.xml')
        self.mjcf_root = mjcf.from_path(path)