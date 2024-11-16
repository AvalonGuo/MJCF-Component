import os
from dm_control import mjcf

class Apple:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ013_apple', 'apple.xml')
        self.mjcf_root = mjcf.from_path(path)