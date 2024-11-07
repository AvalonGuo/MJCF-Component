import os
from dm_control import mjcf

class Tuna_fish_can:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components', 'tuna_fish_can', 'tuna_fish_can.xml')
        self.mjcf_root = mjcf.from_path(path)