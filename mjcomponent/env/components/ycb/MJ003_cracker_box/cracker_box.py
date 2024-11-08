import os
from dm_control import mjcf

class Cracker_box:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ003_cracker_box', 'cracker_box.xml')
        self.mjcf_root = mjcf.from_path(path)