import os
from dm_control import mjcf

class Spatula:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ033_spatula', 'spatula.xml')
        self.mjcf_root = mjcf.from_path(path)
