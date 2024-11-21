import os
from dm_control import mjcf

class Airplane_c:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ072_c_toy_airplane', 'airplane_c.xml')
        self.mjcf_root = mjcf.from_path(path)
