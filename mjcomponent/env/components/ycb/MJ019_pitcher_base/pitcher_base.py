import os
from dm_control import mjcf

class Pitcher_base:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ019_pitcher_base', 'pitcher_base.xml')
        self.mjcf_root = mjcf.from_path(path)