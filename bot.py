# abrir a media pantalla http://www.trex-game.skipser.com/
from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

class Cordinates():
    replayBtn = (340,390) # coordenadas del botón de repetición para iniciar el juego
    dinosaur = (171,437) # estas coordenadas representan la coordenada superior derecha, que se usará para definir la caja frontal

def restartGame():
    pyautogui.click(Cordinates.replayBtn) # hacemos clic en el botón de reproducción sin interacción del usuario
    pyautogui.keyDown('down') # mantenemos el dinosaurio siempre abajo para no chocar con las aves

def pressSpace():
    pyautogui.keyUp('down') # soltando la tecla Down
    pyautogui.keyDown('space')
    time.sleep(0.10 ) #10
    print("Jump")  #   imprime la tecla Jump en el terminal 
    time.sleep(0.29) #19 
    pyautogui.keyUp('space') # soltando la tecla de espacio
    pyautogui.keyDown('down') # presionamos nuevamente la tecla abajo para tener añ dinosaurio siempre en esa posicion
  
def imageGrab():
	 # definiendo las coordenadas de la caja frente al dinosaurio
 	box = (Cordinates.dinosaur[0]+70, Cordinates.dinosaur[1],
 	Cordinates.dinosaur[0]+120, Cordinates.dinosaur[1]+6)
 	image = ImageGrab.grab(box) # tomando todos los valores de píxeles en forma de tuplas RGB
 	grayImage = ImageOps.grayscale(image) # convertir RGB a escala de grises, facilita el procesamiento y da como resultado más rápido
 	a = array(grayImage.getcolors()) # usando numpy para obtener la suma de todos los píxeles en escala de grises
 	print( a.sum( ))
 	return a.sum() # devolviendo la suma

# función para reiniciar el juego
def main():
	restartGame()
	while True:
		if(imageGrab() !=978): # 697 es la suma de los valores de píxeles blancos de la caja
			pressSpace()       # si el valor devuelto por la función "imageGrab" no es igual a 697, significa que el pájaro o el arbusto estan cerca del dinosaurio
			time.sleep(0.1) # tiempo para reconocer la operación realizada por la función anterior

main()
#restartGame()
#time.sleep(1)
#pressSpace() 
       