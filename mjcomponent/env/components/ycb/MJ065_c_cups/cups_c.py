import os
from dm_control import mjcf

class Cups_c:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ065_c_cups', 'cups_c.xml')
        self.mjcf_root = mjcf.from_path(path)
