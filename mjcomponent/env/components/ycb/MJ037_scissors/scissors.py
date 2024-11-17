import os
from dm_control import mjcf

class Scissors:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ037_scissors', 'scissors.xml')
        self.mjcf_root = mjcf.from_path(path)
