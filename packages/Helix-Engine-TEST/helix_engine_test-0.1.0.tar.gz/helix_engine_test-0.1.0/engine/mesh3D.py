# hlx3D.py
from .defines import *
from .helpers import *

class Mesh3D:
    def __init__(self) -> None:
        self.ctx = None
        """OpenGL context"""

        self.program = None
        """shader program"""

        self.vbo_format = None
        """vertex buffer data type format: "3f, 3f" """

        self.attrs: tuple[str, ...] = None
        """attribute names according to the format: ("in_position", "in_color")"""

        self.vao = None
        """vertex array object"""

    def get_vertex_data(self) -> np.array: ...

    def get_vao(self):
        vertex_data = self.get_vertex_data()
        vbo = self.ctx.buffer(vertex_data)
        vao = self.ctx.vertex_array(
            self.program, [(vbo, self.vbo_format, *self.attrs)])
        return vao

    def render(self) -> None:
        self.vao.render()

class VoxelChunkMesh(Mesh3D):
    def __init__(self, helix, chunk_object) -> None:
        super().__init__()
        self.chunk = chunk_object
        self.ctx = helix.ctx

        # self.program = helix.shaders.bank['chunk']
        self.program = helix.resource_manager.get_shader(shader_id="chunk")

        self.vbo_format = '1u4'
        self.format_size = sum(int(fmt[:1]) for fmt in self.vbo_format.split())

        # packed attrs: x y z voxel_id face_id ao_id flip_id
        self.attrs = ('packed_data',)
        self.vao = self.get_vao()

    def rebuild(self):
        self.vao = self.get_vao()

    def get_vertex_data(self):
        mesh = build_chunk_mesh(
            scene_voxels=self.chunk.scene.voxels,
            scene_width=self.chunk.scene.width,
            scene_height=self.chunk.scene.height,
            scene_depth=self.chunk.scene.depth,
            chunk_size=self.chunk.size,
            chunk_voxels=self.chunk.voxels,
            format_size=self.format_size,
            chunk_pos=self.chunk.position
        )
        return mesh

class CubeMesh(Mesh3D):
    def __init__(self, engine):
        super().__init__()
        self.engine = engine
        self.ctx = self.engine.ctx
        self.program = engine.resource_manager.get_shader(shader_id="marker")

        self.vbo_format = '2f2 3f2'
        self.attrs = ('in_tex_coord_0', 'in_position')
        self.vao = self.get_vao()

    @staticmethod
    def get_data(vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data, dtype='float16')

    def get_vertex_data(self):
        vertices = [
            (0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1),
            (0, 1, 0), (0, 0, 0), (1, 0, 0), (1, 1, 0)
        ]
        indices = [
            (0, 2, 3), (0, 1, 2),
            (1, 7, 2), (1, 6, 7),
            (6, 5, 4), (4, 7, 6),
            (3, 4, 5), (3, 5, 0),
            (3, 7, 4), (3, 2, 7),
            (0, 6, 1), (0, 5, 6)
        ]
        vertex_data = self.get_data(vertices, indices)

        tex_coord_vertices = [(0, 0), (1, 0), (1, 1), (0, 1)]
        tex_coord_indices = [
            (0, 2, 3), (0, 1, 2),
            (0, 2, 3), (0, 1, 2),
            (0, 1, 2), (2, 3, 0),
            (2, 3, 0), (2, 0, 1),
            (0, 2, 3), (0, 1, 2),
            (3, 1, 2), (3, 0, 1),
        ]
        tex_coord_data = self.get_data(tex_coord_vertices, tex_coord_indices)
        vertex_data = np.hstack([tex_coord_data, vertex_data])
        return vertex_data

class VoxelMarker:
    def __init__(self, voxel_handler):
        self.engine = voxel_handler.engine
        self.handler = voxel_handler
        self.position = glm.vec3(0)
        self.m_model = self.get_model_matrix()
        self.mesh = CubeMesh(self.engine)

    def update(self):
        if self.handler.voxel_id:
            if self.handler.mode:
                self.position = self.handler.voxel_scene + self.handler.voxel_normal
            else:
                self.position = self.handler.voxel_scene

    def set_uniform(self):
        self.mesh.program['mode_id'] = self.handler.mode
        self.mesh.program['m_model'].write(self.get_model_matrix())

    def get_model_matrix(self):
        m_model = glm.translate(glm.mat4(), glm.vec3(self.position))
        return m_model

    def render(self):
        if self.handler.voxel_id:
            self.set_uniform()
            self.mesh.render()

class VoxelChunk:
    def __init__(self, helix, scene3D, position, chunk_size) -> None:
        self.is_void = True
        self.engine = helix
        self.scene = scene3D
        self.position = position
        self.voxels: np.array = None
        self.mesh: VoxelChunkMesh = None
        
        self.size = chunk_size
        self.area = chunk_size * chunk_size
        self.volume = self.area * self.size
        
        self.voxel_size = 8
        
        self.m_model = self.get_model_matrix()

    def set_uniform(self):
        self.mesh.program['m_model'].write(self.m_model)

    def get_model_matrix(self):
        return glm.translate(glm.mat4(), glm.vec3(self.position) * self.size)

    def build_mesh(self):
        self.mesh = VoxelChunkMesh(self.engine, self)

    def build_voxels(self):
        # empty chunk
        voxels = np.zeros(self.volume, dtype='uint8')

        # fill the chunk
        cx, cy, cz = glm.ivec3(self.position) * self.size
        rng = random.randrange(1, 100)
        
        for x in range(self.size):
            for z in range(self.size):
                wx = x + cx
                wz = z + cz
                field_height = int(glm.simplex(glm.vec2(wx, wz) * 0.01) * self.size + self.size)
                local_height = min(field_height - cy, self.size)
                
                for y in range(local_height):
                    wy = y + cy
                    voxels[x+self.size*z+self.area*y] = rng
                    # voxels[x+self.size*z+self.area*y] = wy + 1
        if np.any(voxels):
            self.is_void = False
        return voxels

    def render(self):
        if not self.is_void:
            self.set_uniform()
            self.mesh.render()

class VoxelHandler:
    def __init__(self, helix, scene):
        self.scene = scene
        self.engine = helix
        self.chunks = scene.chunks

        # ray casting result
        self.ray_max = 8
        self.chunk = None
        self.voxel_id = None
        self.voxel_index = None
        self.voxel_local = None
        self.voxel_scene = None
        self.voxel_normal = None

        self.mode = 0  # 0: rem voxel   1: add voxel
        self.new_id = 1

    def swap_mode(self):
        self.mode = not self.mode

    def set_voxel(self):
        if self.mode:
            self.add_voxel()
        else:
            self.rem_voxel()

    def rem_voxel(self):
        if self.voxel_id:
            self.chunk.voxels[self.voxel_index] = 0

            self.chunk.mesh.rebuild()
            self.rebuild_adj()

    def add_voxel(self):
        if self.voxel_id:
            # check voxel id along normal
            result = self.get_voxel_id(self.voxel_scene + self.voxel_normal)

            # is the new place empty?
            if not result[0]:
                _, voxel_index, _, chunk = result
                chunk.voxels[voxel_index] = self.new_id
                chunk.mesh.rebuild()

                # was it an empty chunk?
                if chunk.is_void:
                    chunk.is_void = False

    def rebuild_adj_chunk(self, adj_voxel_pos):
        index = get_chunk_index(self.scene.width, self.scene.height, self.scene.depth, self.scene.chunk_size, adj_voxel_pos)
        if index != -1:
            self.chunks[index].mesh.rebuild()

    def rebuild_adj(self):
        lx, ly, lz = self.voxel_local
        wx, wy, wz = self.voxel_scene

        if lx == 0:
            self.rebuild_adj_chunk((wx - 1, wy, wz))
        elif lx == self.scene.chunk_size - 1:
            self.rebuild_adj_chunk((wx + 1, wy, wz))

        if ly == 0:
            self.rebuild_adj_chunk((wx, wy - 1, wz))
        elif ly == self.scene.chunk_size - 1:
            self.rebuild_adj_chunk((wx, wy + 1, wz))

        if lz == 0:
            self.rebuild_adj_chunk((wx, wy, wz - 1))
        elif lz == self.scene.chunk_size - 1:
            self.rebuild_adj_chunk((wx, wy, wz + 1))
     
    def ray_cast(self):
        # start point
        x1, y1, z1 = self.engine.camera.eye
        # end point
        x2, y2, z2 = self.engine.camera.eye + self.engine.camera.forward * self.ray_max

        current_voxel_pos = glm.ivec3(x1, y1, z1)
        self.voxel_id = 0
        self.voxel_normal = glm.ivec3(0)
        step_dir = -1

        dx = glm.sign(x2 - x1)
        delta_x = min(dx / (x2 - x1), 10_000_000.0) if dx != 0 else 10_000_000.0
        max_x = delta_x * (1.0 - glm.fract(x1)) if dx > 0 else delta_x * glm.fract(x1)

        dy = glm.sign(y2 - y1)
        delta_y = min(dy / (y2 - y1), 10_000_000.0) if dy != 0 else 10_000_000.0
        max_y = delta_y * (1.0 - glm.fract(y1)) if dy > 0 else delta_y * glm.fract(y1)

        dz = glm.sign(z2 - z1)
        delta_z = min(dz / (z2 - z1), 10_000_000.0) if dz != 0 else 10_000_000.0
        max_z = delta_z * (1.0 - glm.fract(z1)) if dz > 0 else delta_z * glm.fract(z1)

        while not (max_x > 1.0 and max_y > 1.0 and max_z > 1.0):
            
            # each step check if voxel is void, if not update attribs for ray casting
            result = self.get_voxel_id(voxel_scene=current_voxel_pos)
            if result[0]:
                self.voxel_id, self.voxel_index, self.voxel_local, self.chunk = result
                self.voxel_scene = current_voxel_pos

                if step_dir == 0:
                    self.voxel_normal.x = -dx
                elif step_dir == 1:
                    self.voxel_normal.y = -dy
                else:
                    self.voxel_normal.z = -dz
                return True

            # the direction of step dir is an identifier to determine the normal to the current voxel ( needed to determine the choice of position when setting new voxels )
            if max_x < max_y:
                if max_x < max_z:
                    current_voxel_pos.x += dx
                    max_x += delta_x
                    step_dir = 0
                else:
                    current_voxel_pos.z += dz
                    max_z += delta_z
                    step_dir = 2
            else:
                if max_y < max_z:
                    current_voxel_pos.y += dy
                    max_y += delta_y
                    step_dir = 1
                else:
                    current_voxel_pos.z += dz
                    max_z += delta_z
                    step_dir = 2
        return False

    def get_voxel_id(self, voxel_scene):
        cx, cy, cz = chunk_pos = voxel_scene / self.scene.chunk_size

        if 0 <= cx < self.scene.width and 0 <= cy < self.scene.height and 0 <= cz < self.scene.depth:
            chunk_index = cx + self.scene.width * cz + self.scene.area * cy
            chunk = self.chunks[chunk_index]

            lx, ly, lz = voxel_local = voxel_scene - chunk_pos * self.scene.chunk_size

            voxel_index = lx + self.scene.chunk_size * lz + self.scene.chunk_area * ly
            voxel_id = chunk.voxels[voxel_index]

            return voxel_id, voxel_index, voxel_local, chunk
        return 0, 0, 0, 0

    def update(self):
        self.ray_cast()
