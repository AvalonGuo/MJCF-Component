import os
from dm_control import mjcf

class Fork:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ030_fork', 'fork.xml')
        self.mjcf_root = mjcf.from_path(path)
