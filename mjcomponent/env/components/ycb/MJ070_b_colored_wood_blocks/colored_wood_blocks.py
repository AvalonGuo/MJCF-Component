import os
from dm_control import mjcf

class Colored_wood_block:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ070_b_colored_wood_blocks', 'colored_wood_blocks.xml')
        self.mjcf_root = mjcf.from_path(path)
