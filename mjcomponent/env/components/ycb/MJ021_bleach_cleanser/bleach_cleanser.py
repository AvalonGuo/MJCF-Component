import os
from dm_control import mjcf

class Bleach_cleanser:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ021_bleach_cleanser', 'bleach_cleanser.xml')
        self.mjcf_root = mjcf.from_path(path)