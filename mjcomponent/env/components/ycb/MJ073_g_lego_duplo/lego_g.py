import os
from dm_control import mjcf

class Lego_g:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ073_g_lego_duplo', 'lego_g.xml')
        self.mjcf_root = mjcf.from_path(path)
