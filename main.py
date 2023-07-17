```py
import json
import keyboard
import pyautogui

COORDS_FILE = 'instalock_coords.json'

def capture_coordinates():
    print("Hover your mouse over the agent and press Alt to capture the coordinates.")
    while True:
        if keyboard.is_pressed('alt'):
            x, y = pyautogui.position()
            with open(COORDS_FILE, 'w') as file:
                json.dump({'agent': {'x': x, 'y': y}}, file)
            print("Agent coordinates saved.")
            break

    print("Hover your mouse over the lock button and press Alt to capture the coordinates.")
    while True:
        if keyboard.is_pressed('alt'):
            x, y = pyautogui.position()
            with open(COORDS_FILE, 'r+') as file:
                data = json.load(file)
                data['lock_button'] = {'x': x, 'y': y}
                file.seek(0)
                json.dump(data, file)
                file.truncate()
            print("Lock button coordinates saved.")
            break

def load_coordinates():
    try:
        with open(COORDS_FILE, 'r') as file:
            coordinates = json.load(file)
        return coordinates['agent'], coordinates['lock_button']
    except FileNotFoundError:
        return None

def install_lock():
    coords = load_coordinates()

    if not coords:
        capture_coordinates()
        coords = load_coordinates()

    print("Waiting for Alt key press to start the installation process.")

    while True:
        if keyboard.is_pressed('alt'):
            while True:
                pyautogui.click(coords['agent']['x'], coords['agent']['y'])
                pyautogui.click(coords['lock_button']['x'], coords['lock_button']['y'])
                if keyboard.is_pressed('alt'):
                    break

def main():
    install_lock()

if __name__ == '__main__':
    main()
import json
import keyboard
import pyautogui

COORDS_FILE = 'instalock_coords.json'

def capture_coordinates():
    print("Hover your mouse over the agent and press Alt to capture the coordinates.")
    while True:
        if keyboard.is_pressed('alt'):
            x, y = pyautogui.position()
            with open(COORDS_FILE, 'w') as file:
                json.dump({'agent': {'x': x, 'y': y}}, file)
            print("Agent coordinates saved.")
            break

    print("Hover your mouse over the lock button and press Alt to capture the coordinates.")
    while True:
        if keyboard.is_pressed('alt'):
            x, y = pyautogui.position()
            with open(COORDS_FILE, 'r+') as file:
                data = json.load(file)
                data['lock_button'] = {'x': x, 'y': y}
                file.seek(0)
                json.dump(data, file)
                file.truncate()
            print("Lock button coordinates saved.")
            break

def load_coordinates():
    try:
        with open(COORDS_FILE, 'r') as file:
            coordinates = json.load(file)
        return coordinates['agent'], coordinates['lock_button']
    except FileNotFoundError:
        return None

def install_lock():
    coords = load_coordinates()

    if not coords:
        capture_coordinates()
        coords = load_coordinates()

    print("Waiting for Alt key press to start the installation process.")

    while True:
        if keyboard.is_pressed('alt'):
            while True:
                pyautogui.click(coords['agent']['x'], coords['agent']['y'])
                pyautogui.click(coords['lock_button']['x'], coords['lock_button']['y'])
                if keyboard.is_pressed('alt'):
                    break

def main():
    install_lock()

if __name__ == '__main__':
    main()
```
