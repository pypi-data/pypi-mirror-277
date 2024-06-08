import curses
from .entities import Position, Color, Dimensions
from typing import Callable
import os


STDSRC = None
POS = Position(0, 0)
FOREGROUND = Color(250, 250, 250)
BACKGROUND = Color(0, 0, 0)
DIMENSIONS = None
MAX_PAIRS = -1
MAX_COLORS = -1
ACTIVE_PAIR = 1


def _init_curses():
    pantalla = curses.initscr()

    curses.cbreak()
    curses.start_color()
    pantalla.keypad(True)

    return pantalla


def _end(scr):
    curses.nocbreak()
    scr.keypad(False)
    curses.echo()
    curses.endwin()


def pause(ms: int):
    curses.napms(ms)


def init():
    global STDSRC, POS, DIMENSIONS, MAX_PAIRS, MAX_COLORS
    STDSRC = _init_curses()
    DIMENSIONS = Dimensions(*STDSRC.getmaxyx())
    MAX_PAIRS = curses.COLOR_PAIRS
    MAX_COLORS = curses.COLORS
    pair(FOREGROUND, BACKGROUND)


def finish():
    _end(STDSRC)


def cls(refresh: bool = False):
    STDSRC.clear()
    locate(0, 0)
    if refresh:
        STDSRC.refresh()


def locate(x: int, y: int):
    global POS
    STDSRC.move(y, x)
    _retrievePos()


def Print(cadena: object = "", refresh: bool = False):
    STDSRC.addstr(str(cadena), curses.color_pair(ACTIVE_PAIR))
    _retrievePos()
    locate(0, POS.y + 1)
    _retrievePos()
    if refresh:
        STDSRC.refresh()


def Input(mensaje: str = "") -> str:
    curses.curs_set(1)
    STDSRC.addstr(mensaje, curses.color_pair(ACTIVE_PAIR))
    curses.echo()
    user_input = STDSRC.getstr(curses.color_pair(ACTIVE_PAIR)).decode('utf-8')
    curses.noecho()
    _retrievePos()
    return user_input


def _create_color(ix: int, color: Color):
    curses.init_color(ix, *color.value)


def _retrievePos():
    global POS
    POS = Position(*STDSRC.getyx())


def pair(_pen: Color, _paper: Color, refresh: bool = False):
    global FOREGROUND, BACKGROUND
    _create_color(12, _pen)
    _create_color(13, _paper)
    curses.init_pair(ACTIVE_PAIR, 12, 13)
    FOREGROUND = _pen
    BACKGROUND = _paper
    STDSRC.bkgd(' ', curses.color_pair(ACTIVE_PAIR))
    if refresh:
        STDSRC.refresh()


def pen(color: Color, refresh: bool = False):
    pair(color, BACKGROUND, refresh)


def paper(color: Color, refresh: bool = False):
    pair(FOREGROUND, color, refresh)


def app(func: Callable[..., None]) -> Callable[..., None]:
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        finally:
            _end(STDSRC)

    return wrapper


class Simple_ScreenContextManager:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        finish()
        return False


init()
