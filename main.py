from multiprocessing.connection import wait
from pkgutil import extend_path
from time import sleep
from xml.etree.ElementTree import tostring
from playsound import playsound

listOfOptions = ["Avada Kedavera"]

active = True


def playPotter():
    print("\n\n\n")
    sleep(1)

    print("\nHarry Potter,\n")
    playsound("HarryPotterSounds/harryPotter.mp3")

    sleep(.8)

    print("\nthe boy who lived,\n")
    playsound("HarryPotterSounds/theboywholived.mp3")

    sleep(.5)

    # for i in range(3):
    #   print(".")
    #  sleep(.2)

    print("come to die.\n\n")
    playsound("HarryPotterSounds/comeToDie.mp3")

    sleep(2)

    print("AVADA KEDAVRA!!!")
    playsound("HarryPotterSounds/avadacadavera.mp3")


def displayOptions():
    count = 0
    for x in listOfOptions:
        print("\n")
        print(str(count) + ". " + x)
    print("Please enter the number of the track you would like to hear. or -1 to exit")


while active:
    displayOptions()

    userInput = int(input())

    if(userInput == 0):
            playPotter()

    elif(userInput == -1):
            print("Exiting...")
            active = False
    else:
            print("Please enter a valid number.\n")
