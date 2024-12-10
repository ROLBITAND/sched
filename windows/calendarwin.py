import curses
import datetime
from typing import List

from windows.window import Window


class CalendarRow(Window):
    date: datetime.date
    is_selected: bool = False

    @property
    def is_today(self):
        return self.date == datetime.date.today()

    def draw(self):
        if self.is_selected:
            self.curses_window.attron(curses.A_REVERSE)
        if self.is_today:
            self.curses_window.attron(curses.color_pair(1))
        self.curses_window.box()
        date_label = self.date.isoformat()
        # account for the box borders
        padding = self.cols - len(date_label) - 2
        self.curses_window.addstr(1, 1, f"{date_label + (" " * padding)}")
        self.curses_window.refresh()


class CalendarWindow(Window):
    data: any
    selected: int = 0

    @property
    def num_content_rows(self):
        # compensate for the top border
        content_lines = self.lines - 1
        return content_lines // 3

    def select_next_row(self):
        if self.selected < self.num_content_rows - 1:
            self.selected += 1

    def select_previous_row(self):
        if self.selected > 0:
            self.selected -= 1

    def draw(self):
        self.curses_window.addstr(0, 0, ("─" * self.cols))
        self.curses_window.addstr(0, 1, "SCHEDULE", curses.A_REVERSE)
        self.curses_window.refresh()

        for r in range(self.num_content_rows):
            row = CalendarRow(
                x=self.x,
                y=(r * 3) + 1 + self.y,
                lines=3,
                cols=self.cols,
            )
            row.date = datetime.date.today() + datetime.timedelta(r)
            row.is_selected = self.selected == r
            row.draw()
