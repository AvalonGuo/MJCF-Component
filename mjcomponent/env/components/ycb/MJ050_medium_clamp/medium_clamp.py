import os
from dm_control import mjcf

class Medium_clamp:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ050_medium_clamp', 'medium_clamp.xml')
        self.mjcf_root = mjcf.from_path(path)
