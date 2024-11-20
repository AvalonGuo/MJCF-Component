import os
from dm_control import mjcf

class Tennis_ball:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ056_tennis_ball', 'tennis_ball.xml')
        self.mjcf_root = mjcf.from_path(path)
