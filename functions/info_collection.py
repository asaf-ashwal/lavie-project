# מעולה. הנה דוגמה פשוטה וחוקית לשימוש ב-pynput כדי לעקוב אחרי לחיצות עכבר ומקלדת, ולתעד את הזמן שזה קרה:

# python
from pynput import mouse, keyboard
from datetime import datetime
import threading
import pygetwindow as gw

# פונקציה לרישום זמן ולחיצה בעכבר
def on_click(x, y, button, pressed):
    if pressed:
        try:
            active_window = gw.getActiveWindow()
            window_title = active_window.title if active_window else "Unknown"
        except Exception:
            window_title = "Unknown"

        print(f"[{datetime.now()}] Click at ({x}, {y}) in window: {window_title}")

mouse.Listener(on_click=on_click).start
# פונקציה לרישום מקשים
def on_press(key):
    try:
        print(f"[{datetime.now()}] Key pressed: {key.char}")
    except AttributeError:
        print(f"[{datetime.now()}] Special key pressed: {key}")

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
# שים לב:
# - זה לא שומר קובץ, רק מדפיס למסך. אפשר להוסיף כתיבה לקובץ אם תרצה.
# - זה מיועד להרצה על מחשב שלך באישורך. אל תשתמש בזה על מחשבים של אחרים בלי רשות מפורשת.
#
# רוצה שאוסיף שמירה לקובץ או אפשרות לעצור עם מקש מסוים?