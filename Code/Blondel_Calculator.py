#NAME

#Functions

import math
import random

def Compute_Blondel(F2F_Height, Stairs_Max_Length):

    Steps = round(F2F_Height / 17)
    Blondel = 63

    Target_Value = 61
    Thread_Min = 24
    Thread_Max = 35

    if Steps != 0:
        Riser = F2F_Height / Steps
        Tread = Target_Value - 2 * Riser

        if Tread >= Thread_Min and Tread <= Thread_Max and Tread * Steps <= Stairs_Max_Length:
            ShowResults(Tread, Riser, Steps)
        else:

            Tread = round(Stairs_Max_Length / Steps)

            if Tread >= Thread_Min and Tread <= Thread_Max and Tread * Steps <= Stairs_Max_Length:
                ShowResults(Tread, Riser, Steps)
            else:
                Tread = math.floor(Stairs_Max_Length / Steps)
                if Tread >= Thread_Min and Tread <= Thread_Max and Tread * Steps <= Stairs_Max_Length:
                    ShowResults(Tread, Riser, Steps)
                else:
                    while Tread > Thread_Max:
                        Blondel = Blondel - 0.01
                        Tread = Blondel - 2 * Riser
                    if Tread >= Thread_Min and Tread <= Thread_Max and Tread * Steps <= Stairs_Max_Length:
                        ShowResults(Tread, Riser, Steps)
                    else:
                        Error()
    else:
        ErreurEscalier()

def Error():

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
    Main()

def ShowResults(Tread, Riser, Steps):

    Blondel = round(2 * Riser + Tread, 2)
    print("----------------")
    print(" ")
    print(" ")
    print("Tread length = ",round(Tread,2)," cm")
    print("Riser height = ",round(Riser,2)," cm")
    print(Steps," steps")
    print("Blondel : ", Blondel)

    if Steps < 25 and Steps >1:
        DrawResults(Steps, Tread, Riser)
    else:
        Total_Length = str(round((Tread*Steps),2))
        Total_Height = str(round((Riser*Steps),2))
        print("Total length = " + Total_Length + " cm")
        print("Total Height = " + Total_Height + " cm")

    print(" ")
    print(" ")
    print("----------------")
    Main()

def Main():

    try:
        Floor_Height = int(input("Floor to floor height (in cm) : "))
        Stairs_Length = int(input("Available length (in cm) : "))
        Compute_Blondel(Floor_Height, Stairs_Length)
    except ValueError:
        print("Not a valid Number - Starting over")
        print("----------------")
        Main()

def DrawResults (Steps, Tread, Riser):

     Total_Length = str(round((Tread*Steps),2))
     Total_Height = str(round((Riser*Steps),2))

     space = "   "
     floor = "_______"

     print(" ")
     print("_   "+ "___" + "------------------ Total height = " + Total_Height + " cm")
     print("   |"+ "   |___")

     for i in range(1, Steps-2):
        space = "   "
        floor = "_______"
        for j in range(0,i):
            space = space + "    "
            floor = floor + "____"
        print("   |"+ space + "|___")

     space = space + "    "

     print("   |"+ space + "|___")
     print("_  |"+ floor + "____|" + "< Total length = " + Total_Length + " cm")

#Launch amazing programm

Main()
