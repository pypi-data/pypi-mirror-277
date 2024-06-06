# camera2D.py

import glm

class Camera2D:
    def __init__(self, helix, width:int=800, height:int=600):
        self.engine = helix
        self.zoom = 1.0
        self.width = width
        self.height = height
        self.position = glm.vec2(0, 0)  # 2D position for panning
        self.m_proj = self.get_m_proj()
        self.m_view = glm.mat4()

    def get_m_proj(self):
        # Calculate the bounds based on the current zoom and camera position
        # This will maintain the (0,0) at top-left irrespective of the zoom level
        left =    0 - self.position.x
        right =   self.width - self.position.x
        bottom =  self.height - self.position.y
        top =     0 - self.position.y
        # (left, right, bottom, top, zNear, zFar)
        return glm.ortho(left * self.zoom, right * self.zoom, bottom * self.zoom, top * self.zoom, -1, 1)

    def get_m_proj_center(self):
        left =    self.position.x - self.width / 2 * self.zoom
        right =   self.position.x + self.width / 2 * self.zoom
        bottom =  self.position.y - self.height / 2 * self.zoom
        top =     self.position.y + self.height / 2 * self.zoom
        #               (left  right  bottom  top  zNear  zFar)
        return glm.ortho(left, right, bottom, top, -1, 1)
    
    def update(self): pass

