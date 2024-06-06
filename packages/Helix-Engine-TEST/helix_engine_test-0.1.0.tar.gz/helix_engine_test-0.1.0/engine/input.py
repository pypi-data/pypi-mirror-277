# input.py
import pygame as pg
from .cmd import toggle_cull_face, toggle_marker

class Keyboard:
    # Letter keys
    A = pg.K_a
    B = pg.K_b
    C = pg.K_c
    D = pg.K_d
    E = pg.K_e
    F = pg.K_f
    G = pg.K_g
    H = pg.K_h
    I = pg.K_i
    J = pg.K_j
    K = pg.K_k
    L = pg.K_l
    M = pg.K_m
    N = pg.K_n
    O = pg.K_o
    P = pg.K_p
    Q = pg.K_q
    R = pg.K_r
    S = pg.K_s
    T = pg.K_t
    U = pg.K_u
    V = pg.K_v
    W = pg.K_w
    X = pg.K_x
    Y = pg.K_y
    Z = pg.K_z

    # Number keys
    Num0 = pg.K_0
    Num1 = pg.K_1
    Num2 = pg.K_2
    Num3 = pg.K_3
    Num4 = pg.K_4
    Num5 = pg.K_5
    Num6 = pg.K_6
    Num7 = pg.K_7
    Num8 = pg.K_8
    Num9 = pg.K_9

    # Function keys
    F1 = pg.K_F1
    F2 = pg.K_F2
    F3 = pg.K_F3
    F4 = pg.K_F4
    F5 = pg.K_F5
    F6 = pg.K_F6
    F7 = pg.K_F7
    F8 = pg.K_F8
    F9 = pg.K_F9
    F10 = pg.K_F10
    F11 = pg.K_F11
    F12 = pg.K_F12

    # Special keys
    Space = pg.K_SPACE
    Escape = pg.K_ESCAPE
    Enter = pg.K_RETURN
    Tab = pg.K_TAB
    Shift = pg.K_LSHIFT  # Left Shift
    Ctrl = pg.K_LCTRL    # Left Control
    Alt = pg.K_LALT      # Left Alt
    RShift = pg.K_RSHIFT  # Right Shift
    RCtrl = pg.K_RCTRL    # Right Control
    RAlt = pg.K_RALT      # Right Alt

    # Arrow keys
    Up = pg.K_UP
    Down = pg.K_DOWN
    Left = pg.K_LEFT
    Right = pg.K_RIGHT

    # Numpad keys
    NumPad0 = pg.K_KP0
    NumPad1 = pg.K_KP1
    NumPad2 = pg.K_KP2
    NumPad3 = pg.K_KP3
    NumPad4 = pg.K_KP4
    NumPad5 = pg.K_KP5
    NumPad6 = pg.K_KP6
    NumPad7 = pg.K_KP7
    NumPad8 = pg.K_KP8
    NumPad9 = pg.K_KP9
    NumPadDivide = pg.K_KP_DIVIDE
    NumPadMultiply = pg.K_KP_MULTIPLY
    NumPadSubtract = pg.K_KP_MINUS
    NumPadAdd = pg.K_KP_PLUS
    NumPadEnter = pg.K_KP_ENTER
    NumPadDecimal = pg.K_KP_PERIOD

    # Modifier keys
    LShift = pg.K_LSHIFT
    RShift = pg.K_RSHIFT
    LCtrl = pg.K_LCTRL
    RCtrl = pg.K_RCTRL
    LAlt = pg.K_LALT
    RAlt = pg.K_RALT
    LMeta = pg.K_LMETA
    RMeta = pg.K_RMETA
    LSuper = pg.K_LSUPER  # Windows key for left
    RSuper = pg.K_RSUPER  # Windows key for right

    # Miscellaneous keys
    CapsLock = pg.K_CAPSLOCK
    NumLock = pg.K_NUMLOCK
    ScrollLock = pg.K_SCROLLOCK
    PrintScreen = pg.K_PRINT
    Pause = pg.K_PAUSE
    Insert = pg.K_INSERT
    Delete = pg.K_DELETE
    Home = pg.K_HOME
    End = pg.K_END
    PageUp = pg.K_PAGEUP
    PageDown = pg.K_PAGEDOWN

    # Symbol keys
    Grave = pg.K_BACKQUOTE  # `~
    Minus = pg.K_MINUS      # -_
    Equals = pg.K_EQUALS    # =+
    LeftBracket = pg.K_LEFTBRACKET   # [{
    RightBracket = pg.K_RIGHTBRACKET # ]}
    Backslash = pg.K_BACKSLASH       # \|
    Semicolon = pg.K_SEMICOLON       # ;:
    Quote = pg.K_QUOTE               # '"
    Comma = pg.K_COMMA               # ,<
    Period = pg.K_PERIOD             # .>
    Slash = pg.K_SLASH               # /?
    BackSpace = pg.K_BACKSPACE
    Tab = pg.K_TAB
    Enter = pg.K_RETURN
    Menu = pg.K_MENU
    

class Mouse:
    LeftClick = 1
    WheelClick = 2
    RightClick = 3
    WheelUp = 4
    WheelDown = 5


class InputHandler:
    quit_requested: bool = False
    def __init__(self, helix):
        self.engine = helix
        self.mouse = {}
        self.keyboard = {}
        self.mouse_pos = (0,0)
        self.mouse_delta = (0,0)
        
        self.mouse_prev = {}
        self.keyboard_prev = {}

    def screen_to_ndc(self, x, y, width, height):
        ndc_x = (x / width) * 2 - 1
        ndc_y = -((y / height) * 2 - 1)  # Negate y to flip the coordinate system
        return ndc_x, ndc_y

    def process_events(self):
        self.mouse_pos = pg.mouse.get_pos()
        self.mouse_prev = self.mouse.copy()
        self.mouse_delta = pg.mouse.get_rel()
        self.mouse_pos_normal = self.screen_to_ndc(*pg.mouse.get_pos(), width=self.engine.window.get_width(), height=self.engine.window.get_height())
        self.keyboard_prev = self.keyboard.copy()
        
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_F12):
                self.quit_requested = True
            if event.type == pg.KEYUP:
                self.keyboard[event.key] = False
            if event.type == pg.KEYDOWN:
                self.keyboard[event.key] = True
                if self.engine.runtime == '3D':
                    if event.key == self.engine.controls["Toggles"]["Cull-Face"]:
                        toggle_cull_face(self.engine)
                    if event.key == self.engine.controls["Toggles"]["Marker"]:
                        toggle_marker(self.engine)
            if event.type == pg.MOUSEBUTTONUP:
                self.mouse[event.button] = False
            if event.type == pg.MOUSEBUTTONDOWN:
                self.mouse[event.button] = True
                if self.engine.runtime == '3D':
                    if event.button == self.engine.controls["Add/Rem"]: # swap edit mode
                        self.engine.scenes[self.engine.scene].voxel_handler.swap_mode()
                    if event.button == self.engine.controls["Add Voxel"]: # swap edit mode
                        self.engine.scenes[self.engine.scene].voxel_handler.set_voxel()

        if self.engine.runtime == '3D':
            kb_state = pg.key.get_pressed()
            vel = self.engine.camera.speed * self.engine.dtime
            if kb_state[self.engine.controls["Up"]]:
                self.engine.camera.move_up(velocity=vel)
            if kb_state[self.engine.controls["Down"]]:
                self.engine.camera.move_down(velocity=vel)
            if kb_state[self.engine.controls["Left"]]:
                self.engine.camera.move_left(velocity=vel)
            if kb_state[self.engine.controls["Right"]]:
                self.engine.camera.move_right(velocity=vel)
            if kb_state[self.engine.controls["Forward"]]:
                self.engine.camera.move_in(velocity=vel)
            if kb_state[self.engine.controls["Backward"]]:
                self.engine.camera.move_out(velocity=vel)
            if kb_state[self.engine.controls["Roll-Yaw+"]]:
                self.engine.camera.rotate_yaw(vel)
            if kb_state[self.engine.controls["Roll-Yaw-"]]:
                self.engine.camera.rotate_yaw(-vel)
                
            self.engine.mouse_dx, self.engine.mouse_dy =  pg.mouse.get_rel()
            if self.engine.mouse_dx:
                self.engine.camera.rotate_yaw(delta_x=self.engine.mouse_dx * self.engine.camera.sensitivity)
            if self.engine.mouse_dy:
                self.engine.camera.rotate_pitch(delta_y=self.engine.mouse_dy * self.engine.camera.sensitivity)

    def is_key_pressed(self, key):
        return self.keyboard.get(key, False)

    def is_key_triggered(self, key):
        return self.keyboard.get(key, False) and not self.keyboard_prev.get(key, False)
    
    def is_mouse_pressed(self, button:int):
        return self.mouse.get(button, False)

    def is_mouse_triggered(self, button):
        return self.mouse.get(button, False) and not self.mouse_prev.get(button, False)
