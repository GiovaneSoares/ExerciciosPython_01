# pyautogui.click() -> escrever
# pyautogui.press() -> Pressionar uma tecla
# pyautogui.write() -> Escrever um texto | numero

import pyautogui
import time

pyautogui.PAUSE = 0.6


pyautogui.press("win")

pyautogui.write("Chrome")

pyautogui.press("Enter")

pyautogui.write("https://www.tjpr.jus.br/custas-judiciais-e-taxa-judiciaria")

pyautogui.press("Enter")

pyautogui.click(x=1046, y=671)

pyautogui.write("0002636-41.2024.8.16.0174")

pyautogui.press("Enter")

pyautogui.click(x=1654, y=688)

pyautogui.click(x=594, y=544)

pyautogui.click(x=1125, y=316)

pyautogui.click(x=507, y=788)

pyautogui.click(x=535, y=861)

pyautogui.click(x=820, y=957, clicks=3)

pyautogui.press("Backspace")

pyautogui.click(x=593, y=983)

pyautogui.press("Enter")

pyautogui.click(x=593, y=983, clicks=3)

pyautogui.write("31/12/2025")

pyautogui.press("Tab")

pyautogui.write("21,61")

pyautogui.press("Tab", presses=2)

pyautogui.press("Enter")

pyautogui.click(x=603, y=353)

pyautogui.write("Banco Itaucard S.A ")

pyautogui.press("Tab")

pyautogui.write("17192451000170")

pyautogui.press("Tab")

pyautogui.write("08557-105")

pyautogui.press("Tab", presses=7)

pyautogui.press("Enter")
time.sleep(1)
pyautogui.click(x=1823, y=739)
time.sleep(5)
pyautogui.click(x=1813, y=236)
