import cv2
import pyautogui
import numpy as np

try:
    # Carrega imagem do botão
    template = cv2.imread('imgs/img1.png', cv2.IMREAD_UNCHANGED)
    # covertion
    if template.shape[2] == 4:
        template = cv2.cvtColor(template, cv2.COLOR_BGRA2BGR)
    w, h = template.shape[1], template.shape[0]

    # Screenshot da tela em formato OpenCV (BGR)
    screenshot = pyautogui.screenshot()
    frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Faz template matching
    result = cv2.matchTemplate(frame, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Se achou com confiança >= 0.8
    if max_val >= 0.7:
        x, y = max_loc
        centro = (x + w//2, y + h//2)
        print(f"Botão encontrado em {centro}")

        # Move o mouse e clica
        pyautogui.moveTo(centro)
        pyautogui.click()
    else:
        print("Botão não encontrado")
except Exception as e:
    print(e)