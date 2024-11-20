import os
from dm_control import mjcf

class Phillips_screwdriver:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ043phillips_screwdriver', 'phillips_screwdriver.xml')
        self.mjcf_root = mjcf.from_path(path)
