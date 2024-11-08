import os
from dm_control import mjcf

class Tomato_soup_can:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ005_tomato_soup_can', 'tomato_soup_can.xml')
        self.mjcf_root = mjcf.from_path(path)