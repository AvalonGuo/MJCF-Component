import os
from dm_control import mjcf

class Cups_j:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ065_j_cups', 'cups_j.xml')
        self.mjcf_root = mjcf.from_path(path)
