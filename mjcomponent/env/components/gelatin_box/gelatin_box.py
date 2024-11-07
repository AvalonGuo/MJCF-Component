import os
from dm_control import mjcf

class Gelatin_box:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components', 'gelatin_box', 'gelatin_box.xml')
        self.mjcf_root = mjcf.from_path(path)
