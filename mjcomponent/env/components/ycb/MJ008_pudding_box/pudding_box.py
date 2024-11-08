import os
from dm_control import mjcf

class Pudding_box:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb', 'MJ008_pudding_box', 'pudding_box.xml')
        self.mjcf_root = mjcf.from_path(path)