import os
from dm_control import mjcf

class Airplane_a:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ072_a_toy_airplane', 'airplane_a.xml')
        self.mjcf_root = mjcf.from_path(path)
