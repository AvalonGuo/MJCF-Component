import os
from dm_control import mjcf

class Sugar_box:
    def __init__(self):
        path = os.path.join('mjcomponent', 'env', 'components','ycb','MJ004_sugar_box', 'sugar_box.xml')
        self.mjcf_root = mjcf.from_path(path)

