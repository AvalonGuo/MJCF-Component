import os
from dm_control import mjcf

class Cups_a:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ065_a_cups', 'cups_a.xml')
        self.mjcf_root = mjcf.from_path(path)
