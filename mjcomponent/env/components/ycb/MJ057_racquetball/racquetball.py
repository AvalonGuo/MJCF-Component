import os
from dm_control import mjcf

class Racquetball:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ057_racquetball', 'racquetball.xml')
        self.mjcf_root = mjcf.from_path(path)
