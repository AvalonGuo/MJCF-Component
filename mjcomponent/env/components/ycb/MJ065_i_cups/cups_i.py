import os
from dm_control import mjcf

class Cups_i:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ065_i_cups', 'cups_i.xml')
        self.mjcf_root = mjcf.from_path(path)
