import os
from dm_control import mjcf

class Padlock:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ038_padlock', 'padlock.xml')
        self.mjcf_root = mjcf.from_path(path)