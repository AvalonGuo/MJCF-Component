import os
from dm_control import mjcf

class Adjustable_wrench:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ042_adjustable_wrench', 'adjustable_wrench.xml')
        self.mjcf_root = mjcf.from_path(path)
