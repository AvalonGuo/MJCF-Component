import os
from dm_control import mjcf

class Cups_b:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ065_b_cups', 'cups_b.xml')
        self.mjcf_root = mjcf.from_path(path)
