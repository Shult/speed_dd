import time
import pyautogui
import pydirectinput

print("Script lancé.") 

pyautogui.FAILSAFE = False 

print("Le script va démarrer dans 5 secondes...")
time.sleep(5)
print("La boucle commence...")

try:
    while True:
        print("Appui sur la touche '&'.")
        pydirectinput.press('1')
        time.sleep(4)

        print("Appui sur la touche 'é'.")
        pydirectinput.press('2')
        time.sleep(4)

except KeyboardInterrupt:
    print("Script interrompu par l'utilisateur.")
