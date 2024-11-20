import os
from dm_control import mjcf

class Softball:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ054_softball', 'softball.xml')
        self.mjcf_root = mjcf.from_path(path)
