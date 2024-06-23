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
