import os
from dm_control import mjcf

class Flat_screwdriver:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ044_flat_screwdriver', 'flat_screwdriver.xml')
        self.mjcf_root = mjcf.from_path(path)
