from pynput import keyboard, mouse
import pyautogui


def on_press(key):
    try:
        print(f'Tecla pressionada: {key.char}')

        if key.char == 'q':  # Pressione 'q' para sair
            return False
        if key.char == 'f':
            posicao = pyautogui.locateOnScreen('img1.png')
            if posicao:
                center = pyautogui.center(posicao)
                pyautogui.click(center)

    except AttributeError:
        print(f'Tecla especial: {key}')
    except Exception as e:
        print(e)


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
