import curses


class Window:
    curses_window: curses.window
    x: int
    y: int
    lines: int
    cols: int

    def __init__(self, x: int = 0, y: int = 0, lines: int = 0, cols: int = 0):
        self.x = x
        self.y = y
        self.lines = lines
        self.cols = cols
        self.curses_window = curses.newwin(lines, cols, y, x)

    def layout(self, x: int, y: int, lines: int, cols: int) -> None:
        self.x = x
        self.y = y
        self.lines = lines
        self.cols = cols
        self.curses_window.resize(lines, cols)
        self.curses_window.mvwin(y, x)

    def draw() -> None:
        raise NotImplemented("Only concrete Window classes implement draw")