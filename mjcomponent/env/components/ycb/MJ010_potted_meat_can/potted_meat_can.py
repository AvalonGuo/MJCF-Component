import os
from dm_control import mjcf

class Potted_meat_can:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb', 'MJ010_potted_meat_can', 'potted_meat_can.xml')
        self.mjcf_root = mjcf.from_path(path)
