import win32gui

print("[" + str(win32gui.GetCursorPos()[0]) + "- app_rect[0]" + ", " + str(win32gui.GetCursorPos()[1])+ "- app_rect[1]" +"]")
