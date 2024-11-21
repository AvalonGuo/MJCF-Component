import os
from dm_control import mjcf

class Airplane_b:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ072_b_toy_airplane', 'airplane_b.xml')
        self.mjcf_root = mjcf.from_path(path)
