import os
from dm_control import mjcf

class Power_drill:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ035_power_drill', 'power_drill.xml')
        self.mjcf_root = mjcf.from_path(path)

