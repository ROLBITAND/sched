from windows.window import Window


class OptionsWindow(Window):
    def draw(self):
        self.curses_window.box()
        self.curses_window.refresh()
