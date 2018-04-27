import os, time, os.path, subprocess
user=os.getlogin()
os.chdir("/home/{0}".format(user))

# this function check if you have necessery folder to move all file in Downloads to respective folder
def check_folder():
    """check if you have respective folder """

    Saisie_folder=input("Do you want to check if you have good folder to move respective file ? Y|N")
    if Saisie_folder in ["Y","y","yes","YES"]:
        # make Downloads folders
        if os.path.exists("/home/{0}/Downloads".format(user)):
            print("Downloads exist ✔️")
        else:
            print("Wait to created Downloads folder")
            os.makedirs("Downloads")

        # make image folder
        if os.path.exists("/home/{0}/Images".format(user)):
            print("Images exist ✔️")
        else:
            print("Wait to created Images folder")
            os.makedirs("Images")

        # make Documents folder
        if os.path.exists("/home/{0}/Documents".format(user)):
            print("Documents exist ✔️")
        else:
            print("Wait to created Documents folder")
            os.makedirs("Documents")

        # make PDF folder for (.PDF)
        if os.path.exists("/home/{0}/Documents/PDF".format(user)):
            print("PDF ✔️")
        else:
            print("Wait to created PDF folder")
            os.makedirs("Documents/PDF")

        #make Writer folder for (.odt,.docx)
        if os.path.exists("/home/{0}/Documents/Writer".format(user)):
            print("Writer exist ✔️")
        else:
            print("Wait to created Writer folder")
            os.makedirs("Documents/Writer")

        #make Text folder for (.txt )
        if os.path.exists("/home/{0}/Documents/Text".format(user)):
            print("Text exist ✔️")
        else:
            print("Wait to created Text folder")
            os.makedirs("Documents/Text")

        #make impress and powerpoint folder for (.pptx, .odp )
        if os.path.exists("/home/{0}/Documents/Presentation".format(user)):
            print("Presentation exist ✔️")
        else:
            print("Wait to created Presentation folder")
            os.makedirs("Documents/Presentation")

        #make tableur folder for (.xls, .xlsx )
        if os.path.exists("/home/{0}/Documents/Tableur".format(user)):
            print("Tableur exist ✔️")
        else:
            print("Wait to created Tableur folder")
            os.makedirs("Documents/Tableur")

        #make compressed folder for (.zip, .tar.bz2, .deb )
        if os.path.exists("/home/{0}/Compressed".format(user)):
            print("Compressed exist ✔️")
        else:
            print("Wait to created Compressed folder")
            os.makedirs("Compressed")

        #make Music folder for (.mp3, .ogg, .opus )
        if os.path.exists("/home/{0}/Music".format(user)):
            print("Music exist ✔️")
        else:
            print("Wait to created Music folder")
            os.makedirs("Music")

        #make Movie folder for (.mp4, .mkv )
        if os.path.exists("/home/{0}/Movie".format(user)):
            print("Movie exist ✔️")
        else:
            print("Wait to created Movie folder")
            os.makedirs("Movie")

        #make torrent folder for (.torrent )
        if os.path.exists("/home/{0}/Downloads/Torrent".format(user)):
            print("Torrent exist ✔️")
        else:
            print("Wait to created Torrent folder")
            os.makedirs("Downloads/Torrent")

        #make windows folder for (.exe, .msi, .bat,... )
        if os.path.exists("/home/{0}/Downloads/Windows".format(user)):
            print("Windows exist ✔️")
        else:
            print("Wait to created Windows folder")
            os.makedirs("Downloads/Windows")

        #make Code file folder for (.html, .jav, .pl )
        if os.path.exists("/home/{0}/Downloads/Code_file".format(user)):
            print("Code_file exist ✔️")
        else:
            print("Wait to created Code_file folder")
            os.makedirs("Downloads/Code_file")

        #make font folder for (.mp4, .mkv )
        if os.path.exists("/home/{0}/Downloads/Font".format(user)):
            print("Font exist ✔️")
        else:
            print("Wait to created Font folder")
            os.makedirs("Downloads/Font")

        #make image os folder for (.iso, .img )
        if os.path.exists("/home/{0}/Downloads/Os".format(user)):
            print("Os exist ✔️")
        else:
            print("Wait to created Os folder")
            os.makedirs("Downloads/Os")


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
