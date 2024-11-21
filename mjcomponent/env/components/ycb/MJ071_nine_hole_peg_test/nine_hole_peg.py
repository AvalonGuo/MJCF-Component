import os
from dm_control import mjcf

class Nine_hole_peg:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ071_nine_hole_peg_test', 'nine_hole_peg.xml')
        self.mjcf_root = mjcf.from_path(path)
