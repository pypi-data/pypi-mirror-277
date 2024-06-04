# original https://github.com/dantmnf & https://github.com/hakaboom/winAuto
import os.path
import re
import threading
import time

import psutil
import win32process
from win32 import win32gui

from ok.capture.windows.window import is_foreground_window, get_window_bounds
from ok.gui.Communicate import communicate
from ok.logging.Logger import get_logger

logger = get_logger(__name__)


class HwndWindow:
    visible = True
    x = 0
    y = 0
    width = 0
    height = 0
    title_height = 0
    border = 0
    scaling = 1
    top_cut = 0
    right_cut = 0
    bottom_cut = 0
    left_cut = 0
    ext_left_bounds = 0  # for BitBlt
    ext_top_bounds = 0  # for BitBlt
    window_change_listeners = []
    frame_aspect_ratio = 0
    hwnd = None
    frame_width = 0
    frame_height = 0
    exists = False
    title = None
    exe_full_path = None

    def __init__(self, exit_event, title, exe_name=None, frame_width=0, frame_height=0):
        super().__init__()
        self.app_exit_event = exit_event
        self.exe_name = exe_name
        self.title = title
        self.stop_event = threading.Event()
        self.visible = False
        self.update_frame_size(frame_width, frame_height)
        self.do_update_window_size()
        self.thread = threading.Thread(target=self.update_window_size, name="update_window_size")
        self.thread.start()

    def update_title_and_exe(self, title, exe):
        self.title = title
        self.exe_name = exe
        self.hwnd = None
        self.visible = False
        self.exists = False
        self.width = 0
        self.height = 0
        self.do_update_window_size()

    def stop(self):
        self.stop_event.set()

    def update_frame_size(self, width, height):
        logger.debug(f"update_frame_size:{self.frame_width}x{self.frame_height} to {width}x{height}")
        if width != self.frame_width or height != self.frame_height:
            self.frame_width = width
            self.frame_height = height
            if width > 0 and height > 0:
                self.frame_aspect_ratio = width / height
                logger.debug(f"HwndWindow: frame ratio:{self.frame_aspect_ratio} width: {width}, height: {height}")

    def update_window_size(self):
        while not self.app_exit_event.is_set() and not self.stop_event.is_set():
            self.do_update_window_size()
            time.sleep(0.2)

    def get_abs_cords(self, x, y):
        return self.x + self.border + x, self.y + y + self.title_height

    def get_top_left_frame_offset(self):
        return self.border, self.title_height

    def do_update_window_size(self):
        try:
            visible, x, y, border, title_height, width, height, scaling, ext_left_bounds, ext_top_bounds = self.visible, self.x, self.y, self.border, self.title_height, self.width, self.height, self.scaling, self.ext_left_bounds, self.ext_top_bounds
            if self.hwnd is None:
                self.hwnd, self.exe_full_path = find_hwnd_by_title_and_exe(self.title, self.exe_name)
                self.exists = self.hwnd is not None
            if self.hwnd is not None:
                self.exists = win32gui.IsWindow(self.hwnd)
                if self.exists:
                    visible = is_foreground_window(self.hwnd)
                    x, y, border, title_height, width, height, scaling, ext_left_bounds, ext_top_bounds = get_window_bounds(
                        self.hwnd)
                    if self.frame_aspect_ratio != 0 and height != 0:
                        window_ratio = width / height
                        if window_ratio < self.frame_aspect_ratio:
                            cropped_window_height = int(width / self.frame_aspect_ratio)
                            title_height += height - cropped_window_height
                            height = cropped_window_height
                    height = height
                    width = width
                    title_height = title_height
                else:
                    self.hwnd = None
                changed = False
                if visible != self.visible or self.scaling != scaling:
                    self.visible = visible
                    self.scaling = scaling
                    changed = True
                if (ext_left_bounds != self.ext_left_bounds or ext_top_bounds != self.ext_top_bounds or
                    x != self.x or y != self.y or border != self.border or title_height != self.title_height or width != self.width or height != self.height or scaling != self.scaling) and (
                        (x >= -1 and y >= -1) or self.visible):
                    self.x, self.y, self.border, self.title_height, self.width, self.height, self.ext_left_bounds, self.ext_top_bounds = x, y, border, title_height, width, height, ext_left_bounds, ext_top_bounds
                    changed = True
                if changed:
                    logger.debug(
                        f"do_update_window_size changed,visible:{self.visible} x:{self.x} y:{self.y} border:{self.border} width:{self.width} height:{self.height} self.title_height:{self.title_height} scaling:{self.scaling}")
                    communicate.window.emit(self.visible, self.x, self.y, self.border, self.title_height, self.width,
                                            self.height, self.scaling)
        except Exception as e:
            logger.error(f"do_update_window_size exception", e)

    def frame_ratio(self, size):
        if self.frame_width > 0 and self.width > 0:
            return int(size / self.frame_width * self.width)
        else:
            return size

    def title_text(self):
        if self.hwnd:
            return win32gui.GetWindowText(self.hwnd)
        return ""

    def __str__(self) -> str:
        return f"title:{self.title}_{self.exe_name}_{self.width}x{self.height}_{self.exists}_{self.visible}"


def find_hwnd_by_title_and_exe(title, exe_name):
    result = []
    if title is None and exe_name is None:
        return None, None

    def callback(hwnd, lParam):
        if len(result) == 0 and win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            if title:
                text = win32gui.GetWindowText(hwnd)
                if isinstance(title, str):
                    if title != text:
                        return True
                elif not re.search(title, text):
                    return True
            name, full_path = get_exe_by_hwnd(hwnd)
            if exe_name:
                if name == exe_name or exe_name == full_path:
                    result.append((hwnd, full_path))
                    return True  # Stop enumeration as we found the first match
            else:
                result.append((hwnd, full_path))
        return True

    win32gui.EnumWindows(callback, None)
    if result:
        return result[0][0], result[0][1]
    else:
        return None, None


def get_exe_by_hwnd(hwnd):
    # Get the process ID associated with the window
    _, pid = win32process.GetWindowThreadProcessId(hwnd)

    # Get the process name and executable path
    process = psutil.Process(pid)
    return process.name(), process.exe()


def enum_windows(emulator_path=None):
    if emulator_path is not None:
        emulator_path = os.path.normpath(emulator_path)

    def callback(hwnd, extra):
        name, full_path = get_exe_by_hwnd(hwnd)
        if emulator_path and emulator_path != full_path:
            return True
        buff = win32gui.GetWindowText(hwnd)
        if buff and win32gui.IsWindowVisible(hwnd):
            rect = win32gui.GetWindowRect(hwnd)
            width = rect[2] - rect[0]
            height = rect[3] - rect[1]
            extra.append((hwnd, buff, width, height))
        return True

    windows = []
    win32gui.EnumWindows(callback, windows)
    return windows
