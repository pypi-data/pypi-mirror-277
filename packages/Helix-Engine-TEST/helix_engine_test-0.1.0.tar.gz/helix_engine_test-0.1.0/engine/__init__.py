from . import camera2D
from .defines import *
from .input import *
from .clock import *
from .camera import *
from .mesh3D import *
from .version import *
from .helpers import *
from .scene3D import *
from .managers import *
from .renderer3D import *

class Helix:
    runtime:str
    fupdate_step: float = 1.0 / 60.0
    running: bool = False
    dtime: float = 0.0
    utime: float = 0.0
    ac_time: float = 0.0

    mouse_dx, mouse_dy = 0, 0

    CULL_FACE: bool = False
    MARKER:VoxelMarker = None

    controls: dict = {
        "Left": pg.K_a,
        "Right": pg.K_d,
        "Up": pg.K_SPACE,
        "Forward": pg.K_w,
        "Backward": pg.K_s,
        "Down": pg.K_LSHIFT,
        "Roll-Yaw+": pg.K_q,
        "Roll-Yaw-": pg.K_e,

        "Add Voxel": 1,
        "Add/Rem": 3,

        "Toggles": {
            "Cull-Face": pg.K_F5,
            "Marker": pg.K_F6,
        }
    }

    with open(HLX_CONFIG_DIR, "r") as cfg:
        config: dict = json.load(cfg)

    def __init__(self):
        pg.init()
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(
            pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        pg.display.gl_set_attribute(pg.GL_DEPTH_SIZE, 24)

        self.window = pg.display.set_mode(
            [800, 600], flags=pg.OPENGL | pg.DOUBLEBUF | pg.GL_ACCELERATED_VISUAL)
        
        pg.display.set_icon(pg.image.load(
            f"{HLX_ASSETS_DIR}helix.png"))
        
        self.clock = clock.Clock()
        self.input_handler = InputHandler(helix=self)

        if self.config["runtime"] == "2D":
            self.runtime = "2D"
            hlxLogger.log(hlxLogger.HLX_LOG_INFO, msg="Helix 2D runtime set ( TEST : WILL CALL __init3D__() )")
            self.__init3D__()
        elif self.config["runtime"] == "3D":
            self.runtime = "3D"
            self.__init3D__()
        
    def __init3D__(self):
        hlxLogger.log(hlxLogger.HLX_LOG_INFO, msg="Helix 3D runtime set")
        self.running = True

        self.ctx = mgl.create_context()  # access the context
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.BLEND)
        self.ctx.gc_mode = 'auto'

        pg.event.set_grab(True)  # prevent out of window cursor movement
        pg.mouse.set_visible(False)
        
        self.camera = camera.Camera3D(helix=self)
        self.renderer = renderer3D.Renderer3D(helix=self)
        
        self.resource_manager = ResourceManager(self)

        self.scenes = {
            "Scene-0": Scene3D(self, 10, 3, 5, 32)
            # "Scene-0": scene3D.Scene3D(self, width=10, height=3, depth=10)
        }
        self.scene: str = "Scene-0"

    def _setattr(self, attr: str, value):
        if hasattr(self, attr):
            setattr(self, attr, value)

    def run(self):
        while self.running:
            self.pre_process()
            while self.ac_time >= self.fupdate_step:
                self.fixed_update()
                self.ac_time -= self.fupdate_step

            self.update()
            self.render()
            self.post_process()

    def handle_input(self):
        self.input_handler.process_events()
        if self.input_handler.quit_requested:
            self.running = False

    def pre_process(self):
        self.ctx.clear(color=[0.1, 0.16, 0.25])
        self.handle_input()
        self.dtime = self.clock.tick() / 1000.0
        self.utime += self.dtime # / 1000.0
        self.ac_time += self.dtime
        pg.display.set_caption(f'Helix v{HLX_MAJOR_VER}.{HLX_MINOR_VER}.{HLX_PATCH_VER}+{HLX_YR_EDITION} :: utime: {
                               self.utime:.0f} :: avg.fps: {self.clock._avg:.0f} :: peak.fps: {self.clock._peak:.0f} :: cur.fps: {self.clock._cur:.0f}')

    def post_process(self):
        self.camera.update()
        pg.display.flip()

    def update(self):
        if self.scene in self.scenes:
            self.scenes[self.scene].update(delta_time=self.dtime, scene=self.scenes[self.scene])
        if self.MARKER:
            self.MARKER.update()
        self.resource_manager.process()
        if hasattr(self, 'shaders'): self.shaders.update()

    def fixed_update(self): pass

    def render(self):
        if self.MARKER:
            self.MARKER.render()
        if self.scene in self.scenes:
            self.renderer.render(self.scenes[self.scene])


def _dump() -> str:
    hlxLogger.log(hlxLogger.HLX_LOG_SYSTEM, f"Helix v{HLX_MAJOR_VER}.{HLX_MINOR_VER}.{
          HLX_PATCH_VER}+{HLX_YR_EDITION}")

if "HLX_HIDE_PROMPT" not in os.environ:
    _dump()
