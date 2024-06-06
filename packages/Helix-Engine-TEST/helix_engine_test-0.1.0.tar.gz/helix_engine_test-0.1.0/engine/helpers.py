# helpers.py
from .defines import *

def timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def debug_mat4(matrix, matrix_name:str="Mat4"):
    print(f"Matrix: {matrix_name}\n")
    print(f"---------------------------\n")
    for i in range(4):
        print(f"| {matrix[i][0]} {matrix[i][1]} {matrix[i][2]} {matrix[i][3]} |\n")
    print(f"---------------------------\n\n")

@nopython
def get_ao(scene_voxels, scene_width, scene_height, scene_depth, chunk_size, local_pos, scene_pos, plane):
    x, y, z = local_pos
    wx, wy, wz = scene_pos
    
    if plane == 'y':
        a = voxel_is_void(scene_voxels, scene_width, scene_height, scene_depth, chunk_size, (x    , y, z - 1), (wx    , wy, wz - 1))
        b = voxel_is_void(scene_voxels, scene_width, scene_height, scene_depth, chunk_size, (x - 1, y, z - 1), (wx - 1, wy, wz - 1))
        c = voxel_is_void(scene_voxels, scene_width, scene_height, scene_depth, chunk_size, (x - 1, y, z    ), (wx - 1, wy, wz    ))
        d = voxel_is_void(scene_voxels, scene_width, scene_height, scene_depth, chunk_size, (x - 1, y, z + 1), (wx - 1, wy, wz + 1))
        e = voxel_is_void(scene_voxels, scene_width, scene_height, scene_depth, chunk_size, (x    , y, z + 1), (wx    , wy, wz + 1))
        f = voxel_is_void(scene_voxels, scene_width, scene_height, scene_depth, chunk_size, (x + 1, y, z + 1), (wx + 1, wy, wz + 1))
        g = voxel_is_void(scene_voxels, scene_width, scene_height, scene_depth, chunk_size, (x + 1, y, z    ), (wx + 1, wy, wz    ))
        h = voxel_is_void(scene_voxels, scene_width, scene_height, scene_depth, chunk_size, (x + 1, y, z - 1), (wx + 1, wy, wz - 1))

    elif plane == 'x':
        a = voxel_is_void(scene_voxels, scene_width, scene_height, scene_depth, chunk_size, (x, y    , z - 1), (wx, wy    , wz - 1))
        b = voxel_is_void(scene_voxels, scene_width, scene_height, scene_depth, chunk_size, (x, y - 1, z - 1), (wx, wy - 1, wz - 1))
        c = voxel_is_void(scene_voxels, scene_width, scene_height, scene_depth, chunk_size, (x, y - 1, z    ), (wx, wy - 1, wz    ))
        d = voxel_is_void(scene_voxels, scene_width, scene_height, scene_depth, chunk_size, (x, y - 1, z + 1), (wx, wy - 1, wz + 1))
        e = voxel_is_void(scene_voxels, scene_width, scene_height, scene_depth, chunk_size, (x, y    , z + 1), (wx, wy    , wz + 1))
        f = voxel_is_void(scene_voxels, scene_width, scene_height, scene_depth, chunk_size, (x, y + 1, z + 1), (wx, wy + 1, wz + 1))
        g = voxel_is_void(scene_voxels, scene_width, scene_height, scene_depth, chunk_size, (x, y + 1, z    ), (wx, wy + 1, wz    ))
        h = voxel_is_void(scene_voxels, scene_width, scene_height, scene_depth, chunk_size, (x, y + 1, z - 1), (wx, wy + 1, wz - 1))

    else:  # Z plane
        a = voxel_is_void(scene_voxels, scene_width, scene_height, scene_depth, chunk_size, (x - 1, y    , z), (wx - 1, wy    , wz))
        b = voxel_is_void(scene_voxels, scene_width, scene_height, scene_depth, chunk_size, (x - 1, y - 1, z), (wx - 1, wy - 1, wz))
        c = voxel_is_void(scene_voxels, scene_width, scene_height, scene_depth, chunk_size, (x    , y - 1, z), (wx    , wy - 1, wz))
        d = voxel_is_void(scene_voxels, scene_width, scene_height, scene_depth, chunk_size, (x + 1, y - 1, z), (wx + 1, wy - 1, wz))
        e = voxel_is_void(scene_voxels, scene_width, scene_height, scene_depth, chunk_size, (x + 1, y    , z), (wx + 1, wy    , wz))
        f = voxel_is_void(scene_voxels, scene_width, scene_height, scene_depth, chunk_size, (x + 1, y + 1, z), (wx + 1, wy + 1, wz))
        g = voxel_is_void(scene_voxels, scene_width, scene_height, scene_depth, chunk_size, (x    , y + 1, z), (wx    , wy + 1, wz))
        h = voxel_is_void(scene_voxels, scene_width, scene_height, scene_depth, chunk_size, (x - 1, y + 1, z), (wx - 1, wy + 1, wz))

    ao = (a + b + c), (g + h + a), (e + f + g), (c + d + e)
    return ao

@nopython
def pack_vertex_data(x, y, z, voxel_id, face_id, ao_id, flip_id):
    # x: 6bit  y: 6bit  z: 6bit  voxel_id: 8bit  face_id: 3bit  ao_id: 2bit  flip_id: 1bit
    a, b, c, d, e, f, g = x, y, z, voxel_id, face_id, ao_id, flip_id

    b_bit, c_bit, d_bit, e_bit, f_bit, g_bit = 6, 6, 8, 3, 2, 1
    fg_bit = f_bit + g_bit
    efg_bit = e_bit + fg_bit
    defg_bit = d_bit + efg_bit
    cdefg_bit = c_bit + defg_bit
    bcdefg_bit = b_bit + cdefg_bit

    packed_data = (
        a << bcdefg_bit |
        b << cdefg_bit |
        c << defg_bit |
        d << efg_bit |
        e << fg_bit |
        f << g_bit | g
    )
    return packed_data

@nopython
def get_chunk_index(scene_width, scene_height, scene_depth, chunk_size, scene_voxel_pos):
    wx, wy, wz = scene_voxel_pos
    cx = wx // chunk_size
    cy = wy // chunk_size
    cz = wz // chunk_size
    
    scene_area = scene_width * scene_depth
    
    if not (0 <= cx < scene_width and 0 <= cy < scene_height and 0 <= cz < scene_depth):
        return -1
    
    index = cx + scene_width * cz + scene_area * cy
    return index

@nopython
def voxel_is_void(scene_voxels, scene_width, scene_height, scene_depth, chunk_size, local_voxel_pos, scene_voxel_pos):
    chunk_area = chunk_size * chunk_size
    chunk_index = get_chunk_index(scene_width, scene_height, scene_depth, chunk_size, scene_voxel_pos)
    
    if chunk_index == -1:
        return False
    
    chunk_voxels = scene_voxels[chunk_index]
    
    x, y, z = local_voxel_pos
    voxel_index = x % chunk_size + z % chunk_size * chunk_size + y % chunk_size * chunk_area
    
    if chunk_voxels[voxel_index]:
        return False
    return True

@nopython
def add_vertex_data(vertex_data, index, *vertices):
    for vertex in vertices:
        vertex_data[index] = vertex
        index += 1
    return index

@nopython
def build_chunk_mesh(scene_voxels, scene_width, scene_height, scene_depth, chunk_size, chunk_voxels, format_size, chunk_pos):
    chunk_area = chunk_size * chunk_size
    chunk_volume = chunk_area * chunk_size
    
    # ARRAY_SIZE = CHUNK_VOL * NUM_VOXEL_VERTICES * VERTEX_ATTRS
    vertex_data = np.empty(chunk_area * 18 * format_size, dtype='uint32')
    index = 0

    for x in range(chunk_size):
        for y in range(chunk_size):
            for z in range(chunk_size):
                voxel_id = chunk_voxels[x + chunk_size * z + chunk_area * y]
                if not voxel_id:
                    continue
                
                # voxel world pos
                cx, cy, cz = chunk_pos
                wx = x + cx * chunk_size
                wy = y + cy * chunk_size
                wz = z + cz * chunk_size

                # top face
                if voxel_is_void(scene_voxels, scene_width, scene_height, scene_depth, chunk_size, (x, y + 1, z), (wx, wy+1, wz)):
                    # get ao values
                    ao = get_ao(scene_voxels, scene_width, scene_height, scene_depth, chunk_size, (x, y + 1, z), (wx, wy+1, wz), plane='y')
                    flip_id = ao[1] + ao[3] > ao[0] + ao[2] # compare face ao values (to solve anisotropia - since the face is comprised of two triangles the interpolation of non linear values along the face lead to weird shadowing)
                    
                    # format: x, y, z, voxel_id, face_id, ao_id
                    # face IDs: 0-top 1-bottom 2-right 3-left 4-back 5-front
                    v0 = pack_vertex_data(x, y+1, z, voxel_id, 0, ao[0], flip_id)
                    v1 = pack_vertex_data(x+1, y+1, z, voxel_id, 0, ao[1], flip_id)
                    v2 = pack_vertex_data(x+1,   y+1, z+1, voxel_id, 0, ao[2], flip_id)
                    v3 = pack_vertex_data(x, y+1, z+1, voxel_id, 0, ao[3], flip_id)

                    # choose correct orientation of the triangles of the face, flipping the orientation of the verticies for each face (isotropic filtering)
                    if flip_id:
                        index = add_vertex_data(
                            vertex_data, index, v1, v0, v3, v1, v3, v2)
                    else:
                        index = add_vertex_data(
                            vertex_data, index, v0, v3, v2, v0, v2, v1)

                # bottom face
                if voxel_is_void(scene_voxels, scene_width, scene_height, scene_depth, chunk_size, (x, y - 1, z), (wx, wy - 1, wz)):
                    # get ao values
                    ao = get_ao(scene_voxels, scene_width, scene_height, scene_depth, chunk_size, (x, y - 1, z), (wx, wy - 1, wz), plane='y')
                    flip_id = ao[1] + ao[3] > ao[0] + ao[2]

                    # format: x, y, z, voxel_id, face_id
                    # face IDs: 0-top 1-bottom 2-right 3-left 4-back 5-front
                    v0 = pack_vertex_data(x, y, z, voxel_id, 1, ao[0], flip_id)
                    v1 = pack_vertex_data(x+1, y, z, voxel_id, 1, ao[1], flip_id)
                    v2 = pack_vertex_data(x+1, y, z+1, voxel_id, 1, ao[2], flip_id)
                    v3 = pack_vertex_data(x, y, z+1, voxel_id, 1, ao[3], flip_id)

                    if flip_id:
                        index = add_vertex_data(
                            vertex_data, index, v1, v3, v0, v1, v2, v3)
                    else:
                        index = add_vertex_data(
                            vertex_data, index, v0, v2, v3, v0, v1, v2)

                # right face
                if voxel_is_void(scene_voxels, scene_width, scene_height, scene_depth, chunk_size, (x + 1, y, z), (wx + 1, wy, wz)):
                    # get ao values
                    ao = get_ao(scene_voxels, scene_width, scene_height, scene_depth, chunk_size, (x + 1, y, z), (wx + 1, wy, wz), plane='x')
                    flip_id = ao[1] + ao[3] > ao[0] + ao[2]

                    # format: x, y, z, voxel_id, face_id
                    # face IDs: 0-top 1-bottom 2-right 3-left 4-back 5-front
                    v0 = pack_vertex_data(x+1, y, z, voxel_id, 2, ao[0], flip_id)
                    v1 = pack_vertex_data(x+1, y+1, z, voxel_id, 2, ao[1], flip_id)
                    v2 = pack_vertex_data(x+1, y+1, z+1, voxel_id, 2, ao[2], flip_id)
                    v3 = pack_vertex_data(x+1, y, z+1, voxel_id, 2, ao[3], flip_id)

                    if flip_id:
                        index = add_vertex_data(
                            vertex_data, index, v3, v0, v1, v3, v1, v2)
                    else:
                        index = add_vertex_data(
                            vertex_data, index, v0, v1, v2, v0, v2, v3)

                # left face
                if voxel_is_void(scene_voxels, scene_width, scene_height, scene_depth, chunk_size, (x - 1, y, z), (wx - 1, wy, wz)):
                    # get ao values
                    ao = get_ao(scene_voxels, scene_width, scene_height, scene_depth, chunk_size, (x - 1, y, z), (wx - 1, wy, wz), plane='x')
                    flip_id = ao[1] + ao[3] > ao[0] + ao[2]

                    # format: x, y, z, voxel_id, face_id
                    # face IDs: 0-top 1-bottom 2-right 3-left 4-back 5-front
                    v0 = pack_vertex_data(x, y, z, voxel_id, 3, ao[0], flip_id)
                    v1 = pack_vertex_data(x, y+1, z, voxel_id, 3, ao[1], flip_id)
                    v2 = pack_vertex_data(x, y+1, z+1, voxel_id, 3, ao[2], flip_id)
                    v3 = pack_vertex_data(x, y, z+1, voxel_id, 3, ao[3], flip_id)

                    if flip_id:
                        index = add_vertex_data(
                            vertex_data, index, v3, v1, v0, v3, v2, v1)
                    else:
                        index = add_vertex_data(
                            vertex_data, index, v0, v2, v1, v0, v3, v2)

                # back face
                if voxel_is_void(scene_voxels, scene_width, scene_height, scene_depth, chunk_size, (x, y, z - 1), (wx, wy, wz - 1)):
                    # get ao values
                    ao = get_ao(scene_voxels, scene_width, scene_height, scene_depth, chunk_size, (x, y, z - 1), (wx, wy, wz - 1), plane='z')

                    # format: x, y, z, voxel_id, face_id
                    # face IDs: 0-top 1-bottom 2-right 3-left 4-back 5-front
                    v0 = pack_vertex_data(x, y, z, voxel_id, 4, ao[0], flip_id)
                    v1 = pack_vertex_data(x, y+1, z, voxel_id, 4, ao[1], flip_id)
                    v2 = pack_vertex_data(x+1, y+1, z, voxel_id, 4, ao[2], flip_id)
                    v3 = pack_vertex_data(x+1, y, z, voxel_id, 4, ao[3], flip_id)

                    if flip_id:
                        index = add_vertex_data(
                            vertex_data, index, v3, v0, v1, v3, v1, v2)
                    else:
                        index = add_vertex_data(
                            vertex_data, index, v0, v1, v2, v0, v2, v3)
                    
                # front face
                if voxel_is_void(scene_voxels, scene_width, scene_height, scene_depth, chunk_size, (x, y, z + 1), (wx, wy, wz + 1)):
                    # get ao values
                    ao = get_ao(scene_voxels, scene_width, scene_height, scene_depth, chunk_size, (x, y, z + 1), (wx, wy, wz + 1), plane='z')
                    flip_id = ao[1] + ao[3] > ao[0] + ao[2]
                    
                    # format: x, y, z, voxel_id, face_id
                    # face IDs: 0-top 1-bottom 2-right 3-left 4-back 5-front
                    v0 = pack_vertex_data(x, y, z+1, voxel_id, 5, ao[0], flip_id)
                    v1 = pack_vertex_data(x, y+1, z+1, voxel_id, 5, ao[1], flip_id)
                    v2 = pack_vertex_data(x+1, y+1, z+1, voxel_id, 5, ao[2], flip_id)
                    v3 = pack_vertex_data(x+1, y, z+1, voxel_id, 5, ao[3], flip_id)

                    if flip_id:
                        index = add_vertex_data(
                            vertex_data, index, v3, v1, v0, v3, v2, v1)
                    else:
                        index = add_vertex_data(
                            vertex_data, index, v0, v2, v1, v0, v3, v2)

    return vertex_data[:index + 1]  # only recieve vertex data from array


""" Objects """
class BitStack:
    def __init__(self, data:list[int]):
        self.offset = 0
        self.depths = []
        self.packed_data = 0
        for d in data:
            self.push([d])  # Initialize the stack with initial data using push

    def bit_length(self, num): return num.bit_length() if num > 0 else 1  # Adjust bit length computation for zero and negative numbers

    def to_ascii(self, data:str): return [ord(c) for c in data]

    def from_ascii(self, data:str): return ''.join(chr(v) for v in data)

    def push(self, data):
        for num in data:
            num_bits = self.bit_length(num)
            self.packed_data |= num << self.offset
            self.offset += num_bits
            self.depths.append(num_bits)  # Update depths each time a new number is pushed
        
    def pop(self):
        if not self.depths:
            return None  # Handle empty stack case
        last_bits = self.depths.pop()
        mask = (1 << last_bits) - 1
        last_value = (self.packed_data >> (self.offset - last_bits)) & mask
        self.packed_data ^= last_value << (self.offset - last_bits)
        self.offset -= last_bits
        return last_value

    def pack(self, data):
        # Compute the total bit size needed and pack data accordingly
        offset = 0
        packed_data = 0
        for value, bits in zip(data, self.depths):
            packed_data |= value << offset
            offset += bits
        return packed_data

    def unpack(self):
        result = []
        temp_offset = 0
        for bits in self.depths:
            mask = (1 << bits) - 1
            result.append((self.packed_data >> temp_offset) & mask)
            temp_offset += bits
        return result
