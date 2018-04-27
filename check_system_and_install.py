import os, time, os.path, subprocess
user=os.getlogin()
os.chdir("/home/{0}".format(user))

# this function check if you have necessery folder to move all file in Downloads to respective folder
def check_folder():
    """check if you have respective folder """

    folder=["Downloads","Documents","Images","Movie","Music","Compressed"]
    folder_Downloads=["Virus","PDF","Writer","Text","Presentation","Tableur","Torrent","Windows","Os","Font","Code_file"]
    

    Saisie_folder=input("Do you want to check if you have good folder to move respective file ? Y|N: ")

    if Saisie_folder in ["Y","y","yes","YES"]:
        for i in folder:
            if os.path.exists("/home/{0}/{1}".format(user,i)):
                print("{0} exist ✔️".format(i))
            else:
                print("Wait to created {0} folder".format(i))
                os.makedirs("{0}".format(i))

        for j in folder_Downloads:
            if os.path.exists("/home/{0}/Downloads/{1}".format(user,j)):
                print("{0} exist ✔️".format(j))
            else:
                print("Wait to created {0} folder".format(j))
                os.makedirs("/home/{0}/Documents/{1}".format(user,j))



#This function allow you to test if you have clamav (Antivirus)
def check_clamscan():
    soft= subprocess.call(['which','clamscan'])
    if soft == 0:
        print("clamav is installed ✔️✔️✔️")
    else:
        print("A Antivirus clamav is not installed\n")
        rep=input("Do yo want to install clamav? Y/N  ")
        if rep in ["Y","y","yes","YES"]:
            os.system("sudo apt-get install clamav")
        else :
            print("Ok! Your files will not scan")


"""check if you have tkinter """

print ("Hello! let me to check if your system are ready")
try:
    import tkinter
except ImportError:
    print("I' sorry you don't have tkinter package\n")
    Saisie=input("do you want to install tkinter Y/N ?  ")
    if Saisie in ["Y","y","yes","YES"]:
        os.system("sudo apt-get install python3-tk")
        check_folder()
    else:
        print("OK! Good bye")
        time.sleep(1)
        exit()
else:
    print("Super! All is Good ✔️✔️✔️")
    check_folder()

""" check if you have Antivirus clamav"""
check_clamscan()
print("Super! All is Good ✔️✔️✔️")
