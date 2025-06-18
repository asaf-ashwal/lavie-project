from functions.info_collection import mouse_listener
from functions.info_collection import keyboard_listener
flag = True


def main ():
  try:
    while True:
      pass
  except KeyboardInterrupt:
    mouse_listener.stop()
    keyboard_listener.stop()

  while flag:

    print('x')
#kgjhfkhgfgkgjk