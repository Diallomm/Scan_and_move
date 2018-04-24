import os, time

print ("Hello! let me to check if your system are ready \nmerci de me laisser vérifier si votre système est pret")
try:
    import tkinter
    print("Super! All is Good")
except ImportError:
    print("I' sorry you don't have tkinter package\n")
    Saisie=input("do you want to install tkinter Y/N ?")
    if Saisie == "Y" or  "yes" or "YES" or "y":
        os.system("sudo apt-get install python3-tk")
    else:
        print("OK! Good bye")
        time.sleep(2)
        exit()
