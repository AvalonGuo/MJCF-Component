import os
from dm_control import mjcf

class Marbles_a:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ063_a_marbles', 'marbles_a.xml')
        self.mjcf_root = mjcf.from_path(path)
