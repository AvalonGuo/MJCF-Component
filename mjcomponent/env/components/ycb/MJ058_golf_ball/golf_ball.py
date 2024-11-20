import os
from dm_control import mjcf

class Golf_ball:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ058_golf_ball', 'golf_ball.xml')
        self.mjcf_root = mjcf.from_path(path)
