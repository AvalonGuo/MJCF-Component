import os
from dm_control import mjcf

class Mustard_bottle:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components', 'mustard_bottle', 'mustard_bottle.xml')
        self.mjcf_root = mjcf.from_path(path)