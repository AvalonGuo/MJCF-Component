import os
from dm_control import mjcf

class Lego_c:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ073_c_lego_duplo', 'lego_c.xml')
        self.mjcf_root = mjcf.from_path(path)
