import os, time

"""check if you have tkinter """

print ("Hello! let me to check if your system are ready \nmerci de me laisser vérifier si votre système est pret")
try:
    import tkinter
    print("Super! All is Good")
except ImportError:
    print("I' sorry you don't have tkinter package\n")
    Saisie=input("do you want to install tkinter Y/N ?")
    if Saisie in ["Y","y","yes","YES"]:
        os.system("sudo apt-get install python3-tk")
    else:
        print("OK! Good bye")
        time.sleep(1)
        exit()

"""check if you have respective folder """
Saisie_folder=input("Do you want to check if you have good folder to move respective file ?")
if Saisie_folder in ["Y","y","yes","YES"]:
    
