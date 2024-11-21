import os
from dm_control import mjcf

class Lego_a:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ073_a_lego_duplo', 'lego_a.xml')
        self.mjcf_root = mjcf.from_path(path)
