import os
from dm_control import mjcf

class Spoon:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ031_spoon', 'spoon.xml')
        self.mjcf_root = mjcf.from_path(path)
