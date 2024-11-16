import os
from dm_control import mjcf

class Bowl:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ024_bowl', 'bowl.xml')
        self.mjcf_root = mjcf.from_path(path)