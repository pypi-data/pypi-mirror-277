# renderer3D.py

class Renderer3D:
    def __init__(self, helix):
        self.engine = helix
        
    def render(self, scene):
        [chunk.render() for chunk in scene.chunks]
        