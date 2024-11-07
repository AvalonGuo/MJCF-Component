import os
from dm_control import mjcf

class Master_chef_can:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components', 'master_chef_can', 'master_chef_can.xml')
        self.mjcf_root = mjcf.from_path(path)