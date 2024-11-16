import os
from dm_control import mjcf

class Orange:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ017_orange', 'orange.xml')
        self.mjcf_root = mjcf.from_path(path)