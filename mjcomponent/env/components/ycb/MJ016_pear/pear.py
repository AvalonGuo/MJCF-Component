import os
from dm_control import mjcf

class Pear:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ016_pear', 'pear.xml')
        self.mjcf_root = mjcf.from_path(path)