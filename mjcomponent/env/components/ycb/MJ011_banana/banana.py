import os
from dm_control import mjcf

class Banana:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ011_banana', 'banana.xml')
        self.mjcf_root = mjcf.from_path(path)