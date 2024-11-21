import os
from dm_control import mjcf

class Lego_f:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ073_f_lego_duplo', 'lego_f.xml')
        self.mjcf_root = mjcf.from_path(path)
