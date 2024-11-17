import os
from dm_control import mjcf

class Large_marker:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ040_large_marker', 'large_marker.xml')
        self.mjcf_root = mjcf.from_path(path)
