import os
from dm_control import mjcf

class Cups_h:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ065_h_cups', 'cups_h.xml')
        self.mjcf_root = mjcf.from_path(path)
