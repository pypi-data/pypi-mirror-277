# scene3D.py

import numpy as np
from .mesh3D import *
from .defines import *

class Scene3D:
    def __init__(self, helix, scene_w, scene_h, scene_d, chunk_size):
        self.engine = helix
        self.depth = scene_d
        self.width = scene_w
        self.height = scene_h
        self.area = self.width * self.depth
        self.volume = self.area * self.height
        
        self.chunk_size = chunk_size
        self.h_chunk_size = self.chunk_size // 2
        self.chunk_area = self.chunk_size * self.chunk_size
        self.chunk_volume = self.chunk_area * self.chunk_size
        self.chunks = [None for _ in range(self.volume)]
        
        self.voxels = np.empty([self.volume, self.chunk_volume], dtype='uint8')
        self.voxel_handler = VoxelHandler(helix, self)
        
        self.build_chunks()
        self.build_chunk_mesh()
        
        hlxLogger.log(hlxLogger.HLX_LOG_INFO, msg=f"Scene3D Info| Area: {self.area} | Width: {self.width} | Height: {self.height} | Volume: {self.volume} | Depth: {self.depth}")

    def build_chunks(self):
        for x in range(self.width):
            for y in range(self.height):
                for z in range(self.depth):
                    chunk = VoxelChunk(self.engine, self, position=(x, y, z), chunk_size=self.chunk_size)
                    
                    # calculate chunk index
                    chunk_index = x + self.width * z + self.area * y
                    self.chunks[chunk_index] = chunk
                    
                    # separate voxels into an isolated array
                    self.voxels[chunk_index] = chunk.build_voxels()
                    
                    # retrieve pointer to the voxel array
                    chunk.voxels = self.voxels[chunk_index]

    def build_chunk_mesh(self):
        [chunk.build_mesh() for chunk in self.chunks]

    def update(self, delta_time:float=0.004, **kwargs):
        self.voxel_handler.update()
    
