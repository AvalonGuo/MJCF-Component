import os
from dm_control import mjcf

class Mini_soccer_ball:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ053_mini_soccer_ball', 'mini_soccer_ball.xml')
        self.mjcf_root = mjcf.from_path(path)
