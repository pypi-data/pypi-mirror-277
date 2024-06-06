# clock.py
import pygame as pg

class Clock:
    _internal = pg.time.Clock()
    
    def __init__(self, target:int=1000) -> None:
        self._cur = 0
        self._avg = 0
        self._peak = 0
        self._total = 0
        self._target = target
        self._total_frames = 0

    def get_ticks(self): return pg.time.get_ticks()

    def tick(self):
        tick = self._internal.tick(self._target)
        self._cur = self._internal.get_fps()
        
        self._peak = max(self._peak, self._cur)
        
        self._total_frames += 1
        self._total += self._cur
        
        self._avg = self._total / self._total_frames if self._total_frames > 0 else 0
        
        return tick