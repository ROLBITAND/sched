import curses
import curses.ascii
from datetime import date
from enum import Enum
from typing import Dict, Tuple

from windows.calendarwin import CalendarWindow
from windows.optionswin import OptionsWindow
from windows.window import Window


"""
TODO
- Handle resizing of window
"""


class LayoutStates(Enum):
    SCHEDULER_VIEW = (0,)


def layout(layout_state: Tuple[LayoutStates, Window, Window]) -> None:
    match layout_state[0]:
        # Options bar on top, scheduler main view
        case LayoutStates.SCHEDULER_VIEW:
            layout_state[1].layout(0, 0, 5, curses.COLS)
            layout_state[2].layout(0, 5, curses.LINES - 5, curses.COLS)


def main(stdscr: curses.window) -> None:
    # Setup
    curses.curs_set(False)

    running = True

    # curses window references
    calendar_window = CalendarWindow()
    options_window = OptionsWindow()

    # Finite States
    SCHEDULER_STATE: Tuple[LayoutStates, OptionsWindow, CalendarWindow] = (
        LayoutStates.SCHEDULER_VIEW,
        options_window,
        calendar_window,
    )

    # Initial state
    LAYOUT_STATE = SCHEDULER_STATE

    # COLORS
    # 1 GREEN/BLACK
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

    while running:
        # Draw
        layout(LAYOUT_STATE)
        stdscr.refresh()
        for active_window in LAYOUT_STATE[1:]:
            active_window.draw()

        # Input
        c = stdscr.getch()

        if c == ord("q") or c == ord("Q"):
            running = False

        if LAYOUT_STATE[0] == LayoutStates.SCHEDULER_VIEW:
            if c == curses.KEY_UP:
                SCHEDULER_STATE[2].select_previous_row()
            elif c == curses.KEY_DOWN:
                SCHEDULER_STATE[2].select_next_row()

        # Update


if __name__ == "__main__":
    # wrapper does the curses terminal inits and shutdowns
    curses.wrapper(main)
