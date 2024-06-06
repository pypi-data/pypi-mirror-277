# camera.py

import glm, pygame as pg

class Camera3D:
    def __init__(self, helix, fov:int=90, far:float=2000.0, near:float=0.1, aspec_ratio:float=(800/600), eye=glm.vec3((10*16), (3*32), (10*16)), yaw=-90, pitch=0) -> None:
        self.engine = helix
        
        self.far = far
        self.near = near
        self.fov = glm.radians(fov)
        self.aspec_ratio = aspec_ratio
        
        self.eye = glm.vec3(50, 20, 50)
        # self.eye = glm.vec3(eye)
        self.yaw = glm.radians(yaw)
        self.pitch = glm.radians(pitch)
        self.pitch_max = glm.radians(89)
        
        self.up = glm.vec3(0, 1, 0)
        self.right = glm.vec3(1, 0, 0)
        self.forward = glm.vec3(0, 0, -1)
        self.center = self.eye + self.forward
        
        self.speed = 8.0
        self.rot_speed = 0.003
        self.sensitivity = 0.002
        
        self.m_view = glm.mat4()
        self.m_proj = glm.perspective(
            self.fov, 
            self.aspec_ratio, 
            self.near, 
            self.far)
    
    def rotate_pitch(self, delta_y):
        self.pitch -= delta_y
        self.pitch = glm.clamp(self.pitch, -self.pitch_max, self.pitch_max)
    
    def rotate_yaw(self, delta_x):
        self.yaw += delta_x

    def move_left(self, velocity):
        self.eye -= self.right * velocity
    
    def move_right(self, velocity):
        self.eye += self.right * velocity
    
    def move_up(self, velocity):
        self.eye += self.up * velocity
    
    def move_down(self, velocity):
        self.eye -= self.up * velocity
    
    def move_in(self, velocity):
        self.eye += self.forward * velocity
    
    def move_out(self, velocity):
        self.eye -= self.forward * velocity
    
    def update_m_view(self):
        """Calculate view matrix based on current camera eye and orientation.
        """
        self.m_view = glm.lookAt(self.eye, self.center, self.up)
        
    def update_vectors(self):
        """Recalculates the forward vector of the camera based on the yaw and pitch values, using the cross product to calculate right and up vectors.
        """
        self.forward.x = glm.cos(self.yaw) * glm.cos(self.pitch)
        self.forward.y = glm.sin(self.pitch)
        self.forward.z = glm.sin(self.yaw) * glm.cos(self.pitch)
        
        self.forward = glm.normalize(self.forward)
        self.right = glm.normalize(glm.cross(self.forward, glm.vec3(0,1,0)))
        self.up = glm.normalize(glm.cross(self.right, self.forward))
        self.center = self.eye + self.forward
    
    def update(self):
        self.update_vectors()
        self.update_m_view()
        
    def get_m_proj(self):
        return self.m_proj
