import win32gui

application_name = "TiktokBot"


def get_child_windows(parent):
    child_windows = []

    def enum_child_windows_callback(hwnd, child_windows):
        child_windows.append(hwnd)

    win32gui.EnumChildWindows(parent, enum_child_windows_callback, child_windows)
    return child_windows


def get_app_rect(hwnd):
    left, top, right, bottom = win32gui.GetClientRect(hwnd)
    left, top = win32gui.ClientToScreen(hwnd, (left, top))
    right, bottom = win32gui.ClientToScreen(hwnd, (right - left, bottom - top))

    return [left, top, right, bottom]


parent_app = win32gui.FindWindow(None, application_name)
child_app = get_child_windows(parent_app)[0]
app_rect = get_app_rect(child_app)
