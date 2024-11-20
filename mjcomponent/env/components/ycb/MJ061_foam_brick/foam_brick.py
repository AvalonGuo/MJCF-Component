import os
from dm_control import mjcf

class Foam_brick:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ061_foam_brick', 'foam_brick.xml')
        self.mjcf_root = mjcf.from_path(path)
