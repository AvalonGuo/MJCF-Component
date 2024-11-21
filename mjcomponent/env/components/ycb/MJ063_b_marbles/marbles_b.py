import os
from dm_control import mjcf

class Marbles_b:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ063_b_marbles', 'marbles_b.xml')
        self.mjcf_root = mjcf.from_path(path)
