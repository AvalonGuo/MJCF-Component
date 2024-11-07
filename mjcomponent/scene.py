import os
import time
import mujoco
import mujoco.viewer
from dm_control import mjcf

class BasicScene:
    def __init__(self,render_mode="human"):
        path = os.path.join('mjcomponent','scene.xml')
        self._mjcf_root = mjcf.from_path(path)
        self.render_mode = render_mode
        

    def attach_objects(self,child,pos:list=[0,0,0],quat:list=[1,0,0,0])->mjcf.Element:
        frame = self._mjcf_root.attach(child)
        frame.add('joint',name="object_x",armature="0",damping="0.000",limited="true",pos=[0,0,0],axis=[1,0,0],stiffness="0",range=[-4.0,4.0],type="slide")
        frame.add('joint',name="object_y",armature="0",damping="0.000",limited="true",pos=[0,0,0],axis=[0,1,0],stiffness="0",range=[-4.0,4.0],type="slide")
        frame.add('joint',name="object_z",armature="0",damping="0.000",limited="true",pos=[0,0,0],axis=[0,0,1],stiffness="0",range=[-2.0,2.0],type="slide")
        frame.add('joint',name="object_rot",armature="0",damping="0.000",pos=[0,0,0],stiffness="0",type="ball")
        frame.pos = pos
        frame.quat = quat
        return frame

    def initialize(self):
        self._physics = mjcf.Physics.from_mjcf_model(self._mjcf_root)
        self.model = self._physics.model.ptr
        self.data = self._physics.data.ptr
        self.viewer = None
        self._timestep = self.model.opt.timestep

    def step_simulation(self):
        if self.viewer == None and self.render_mode == "human":
            self.viewer = mujoco.viewer.launch_passive(model=self.model,data=self.data,show_left_ui=False,show_right_ui=False)
        step_start = time.time()
        mujoco.mj_step(self.model,self.data)
        if self.viewer != None:
            self.viewer.sync()
        time_until_next_step = self._timestep - (time.time() - step_start)
        if time_until_next_step > 0:
            time.sleep(time_until_next_step)
