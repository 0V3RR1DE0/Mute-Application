import win32gui
import time

def list_window_names():
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd):
            hwnds.append((hwnd, win32gui.GetWindowText(hwnd), win32gui.GetClassName(hwnd)))
    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    return hwnds

# Print all window names and class names
for hwnd, title, class_name in list_window_names():
    print(f"HWND: {hwnd}, Title: {title}, Class: {class_name}")

# Pause after printing
input("Press Enter to continue...")
