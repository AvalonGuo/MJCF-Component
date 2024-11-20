import os
from dm_control import mjcf

class Baseball:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ055_baseball', 'baseball.xml')
        self.mjcf_root = mjcf.from_path(path)
