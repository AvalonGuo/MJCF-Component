import os
from dm_control import mjcf

class Lego_b:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ073_b_lego_duplo', 'lego_b.xml')
        self.mjcf_root = mjcf.from_path(path)
