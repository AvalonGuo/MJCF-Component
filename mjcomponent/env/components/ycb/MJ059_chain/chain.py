import os
from dm_control import mjcf

class Chain:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ059_chain', 'chain.xml')
        self.mjcf_root = mjcf.from_path(path)
