# cmd.py
import moderngl as mgl
from .mesh3D import VoxelMarker

def toggle_cull_face(helix):
    helix._setattr("CULL_FACE", not helix.CULL_FACE)
    if (helix.CULL_FACE):
        helix.ctx.enable(flags=mgl.CULL_FACE)
    else:
        helix.ctx.disable(flags=mgl.CULL_FACE)

def toggle_marker(helix):
    if (helix.MARKER):
        helix._setattr("MARKER", None)
    else:
        helix._setattr("MARKER", VoxelMarker(helix.scenes[helix.scene].voxel_handler))
