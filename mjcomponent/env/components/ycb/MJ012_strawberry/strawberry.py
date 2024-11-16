import os
from dm_control import mjcf

class Strawberry:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ012_strawberry', 'strawberry.xml')
        self.mjcf_root = mjcf.from_path(path)