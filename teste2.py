import cv2
import pyautogui
import numpy as np

# Carrega imagem do botão
template = cv2.imread('botao.png', cv2.IMREAD_UNCHANGED)
w, h = template.shape[1], template.shape[0]

# Screenshot da tela em formato OpenCV (BGR)
screenshot = pyautogui.screenshot()
frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

# Faz template matching
result = cv2.matchTemplate(frame, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# Se achou com confiança >= 0.8
if max_val >= 0.8:
    x, y = max_loc
    centro = (x + w//2, y + h//2)
    print(f"Botão encontrado em {centro}")

    # Move o mouse e clica
    pyautogui.moveTo(centro)
    pyautogui.click()
else:
    print("Botão não encontrado")