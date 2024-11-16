import os
from dm_control import mjcf

class Plate:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ029_plate', 'plate.xml')
        self.mjcf_root = mjcf.from_path(path)
