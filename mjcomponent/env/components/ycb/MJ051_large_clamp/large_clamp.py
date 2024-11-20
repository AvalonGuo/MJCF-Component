import os
from dm_control import mjcf

class Large_clamp:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ051_large_clamp', 'large_clamp.xml')
        self.mjcf_root = mjcf.from_path(path)
