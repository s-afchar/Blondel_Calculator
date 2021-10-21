# October 2021 - Sâm AFCHAR - EPFL

import math
import random

#Functions

def askInput():
    """Ask user for input, check its validity then lauch the calculation."""

    try:
        floor_height = int(input("Floor to floor height (in cm) : "))
        stairs_length = int(input("Available length (in cm) : "))
        computeBlondel(floor_height, stairs_length)

    except ValueError:
        print("Not a valid Number - Starting over")
        print("----------------")
        askInput()

def computeBlondel(available_height, available_length):
    """Calculate a stair configuration that meets as closely as possible the Blondel criteria.
    (i.e. : (2 * RISER) + TREAD = 61)"""

    BLONDEL_TARGET = 61
    TREAD_MIN = 24 
    TREAD_MAX = 35 # Comfortable range for the step depth = [24 - 35 cm]
    RISER_MAX = 17 # A step higher than 17 cm is not comfortable

    blondel = 63 # I needed to assign a value

    steps = round(available_height / RISER_MAX)

    if steps != 0:
        riser = available_height / steps
        tread = BLONDEL_TARGET - 2 * riser

        if tread >= TREAD_MIN and tread <= TREAD_MAX and tread * steps <= available_length:
            showResults(tread, riser, steps)

        else:
            tread = round(available_length / steps)
            if tread >= TREAD_MIN and tread <= TREAD_MAX and tread * steps <= available_length:
                showResults(tread, riser, steps)

            else:
                tread = math.floor(available_length / steps)
                if tread >= TREAD_MIN and tread <= TREAD_MAX and tread * steps <= available_length:
                    showResults(tread, riser, steps)

                else:
                    while tread > TREAD_MAX:
                        blondel = blondel - 0.01
                        tread = blondel - 2 * riser

                    if tread >= TREAD_MIN and tread <= TREAD_MAX and tread * steps <= available_length:
                        showResults(tread, riser, steps)

                    else:
                        Error()
    else:
        print("Ok.")

def showResults(tread, riser, steps):
    """Show the results in the Terminal. Then start the programm again.
    (Usually I compute a bunch of stairs in a row, so I wanted a loop)"""

    blondel = round(2 * riser + tread, 2)

    print("----------------")
    print(" ") # I don't know how to do line breaks
    print(" ")

    print("tread length = ",round(tread,2)," cm")
    print("riser height = ",round(riser,2)," cm")
    print(steps," steps")
    print("Blondel : ", blondel)

    if steps < 25 and steps >1: # Don't draw the stair diagramm if there are too many steps.
        DrawResults(steps, tread, riser)

    else:
        Total_Length = str(round((tread*steps),2))
        Total_Height = str(round((riser*steps),2))
        print("Total length = " + Total_Length + " cm")
        print("Total Height = " + Total_Height + " cm")

    print(" ")
    print(" ")
    print("----------------")

    askInput()

def DrawResults (steps, tread, riser):
    """Draw a stair diagramm in the Terminal, with the computed number of steps."""

    Total_Length = str(round((tread*steps),2))
    Total_Height = str(round((riser*steps),2))

    Space = "   "
    Floor = "_______"

    print(" ")
    print("_   "+ "___" + "------------------ Total height = " + Total_Height + " cm")
    print("   |"+ "   |___")

    for i in range(1, steps-2):
       Space = "   "
       Floor = "_______"
       for j in range(0,i):
           Space = Space + "    "
           Floor = Floor + "____"
       print("   |"+ Space + "|___")

    Space = Space + "    "

    print("   |"+ Space + "|___")
    print("_  |"+ Floor + "____|" + "< Total length = " + Total_Length + " cm")

def Error():
    """Show an error message. And start the programm again"""

    print("")
    Very_Funny_Joke = random.randint(1,5)

    if Very_Funny_Joke == 1:
        print("*François Blondel has left the chat*")

    elif Very_Funny_Joke == 2:
        print("*François Blondel is rolling in his grave*")

    elif Very_Funny_Joke == 3:
        print("*François Blondel would like to know why you hate him*")

    elif Very_Funny_Joke == 4:
        print("*François Blondel has blocked you*")

    elif Very_Funny_Joke == 5:
        print("*François Blondel is sad*")

    print("You are trying to make me compute a stair that is WAY TOO STEEP")
    print("----------------")
    print("Let's try again...")
    print("(Try to increase length or decrease height)")
    print("")

    askInput()

#Launch amazing programm

askInput() # FINALLY
