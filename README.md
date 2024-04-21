# Mute-Application
Mutes an game or application when not in the main window. [The mute application is not made by me.]

[Original Link][1]

[1]: https://superuser.com/questions/1438597/how-do-i-make-windows-mute-background-applications



## Mute Application (Not Made By Me)

```bash
pip install pycaw pywin32
```

```python
from pycaw.pycaw import AudioUtilities
import win32gui
import win32process
import time

target_app_class = "[App Class Name]"

def find_process_id():
    hwnd = win32gui.FindWindow(target_app_class, None)
    if hwnd != 0:
        _, process_id = win32process.GetWindowThreadProcessId(hwnd)
        return process_id
    return None

def app_is_in_foreground():
    try:
        act_name = win32gui.GetClassName(win32gui.GetForegroundWindow())
    except win32gui.error:
        act_name = ""
    
    return act_name == target_app_class

def change_app_mute(process_id, mute=1):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        if session.Process and session.Process.pid == process_id:
            session.SimpleAudioVolume.SetMute(mute, None)

while True:
    process_id = find_process_id()
    if process_id:
        if app_is_in_foreground():
            change_app_mute(process_id, 0)
        else:
            change_app_mute(process_id)
    time.sleep(1)
```


## Find Application Class. (Made By Me)

```bash
pip install pywin32
```

```python
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
```
