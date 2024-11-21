import os
from dm_control import mjcf

class Airplane_d:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ072_d_toy_airplane', 'airplane_d.xml')
        self.mjcf_root = mjcf.from_path(path)
