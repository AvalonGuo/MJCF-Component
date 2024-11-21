import os
from dm_control import mjcf

class Lego_e:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ073_e_lego_duplo', 'lego_e.xml')
        self.mjcf_root = mjcf.from_path(path)
