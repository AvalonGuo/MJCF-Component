import os
from dm_control import mjcf

class Dice:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ062_dice', 'dice.xml')
        self.mjcf_root = mjcf.from_path(path)
