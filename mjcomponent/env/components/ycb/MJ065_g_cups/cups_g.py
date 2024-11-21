import os
from dm_control import mjcf

class Cups_g:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ065_g_cups', 'cups_g.xml')
        self.mjcf_root = mjcf.from_path(path)
