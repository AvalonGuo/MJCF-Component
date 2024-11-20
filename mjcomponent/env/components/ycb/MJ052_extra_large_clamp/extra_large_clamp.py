import os
from dm_control import mjcf

class Extra_large_clamp:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ052_extra_large_clamp', 'extra_large_clamp.xml')
        self.mjcf_root = mjcf.from_path(path)
