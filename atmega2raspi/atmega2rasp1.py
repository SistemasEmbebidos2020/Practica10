# !/usr/bin/env python3
# Generated by Proteus Visual Designer for Raspberry Pi

# Modules
from time import sleep
import RPi.GPIO as GPIO
from eserial import *

GPIO.setmode(GPIO.BCM) #puede cambiar a BOARD
global led1
led1 = 4  #si cambiar de BCM a Board defina el número del pin acorde a los pines de la raspberry
global led2
led2 = 5 #si cambiar de BCM a Board defina el número del pin acorde a los pines de la raspberry

GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)

baudios(9600)

# Main function
def main () :
# Infinite loop
 while True :
  prints("Recibiendo datos..  ")
  mensaje = recibir()

  try:
   if int(mensaje)==1:
    GPIO.output(led1,True)
   elif int(mensaje)==0:
    GPIO.output(led1,False)
   elif int(mensaje)==2:
    GPIO.output(led2,True)
   elif int(mensaje)==3:
    GPIO.output(led2,False)


  except:
   pass
  sleep(0.2)
  printsln("ok")
# Command line execution
if __name__ == '__main__' :
 main()
