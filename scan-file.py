#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This script allow automatc you to scan your news files with clamav and move file in respective directory

#Auteur:Mamadou diallo
#Mail:misterdiallo1@gmail.com

"""
#import library
import os
import time
import tkinter
import glob
import shutil
from os.path import splitext

def Scan_print():
    #printing information with tkinter
    mainapp=tkinter.Tk()
    mainapp.title("Alerte")

    #use clamav to scan Downloads folder
    scan=os.popen("clamscan --move=Virus | grep Infected").read()
    nb_virus=det_virus(scan)
    #check and print informations with tkinter
    if nb_virus == 0:
        app=tkinter.Label(mainapp,text=("VIRUS NOT FOUND ✔️"))
        app.pack()
    elif nb_virus == 1:
        app=tkinter.Label(mainapp,text=("VIRUS FOUND ❌\n consult the virus folder to see the copies"))
        app.pack()
    elif nb_virus == 2:
        app=tkinter.Label(mainapp,text=("An error (s) occurred. ❌"))
        app.pack()

    rangements()

    end=tkinter.Label(mainapp,text=("Your files are were moving with success! ✔️"))
    end.pack()

    mainapp.after(10000, mainapp.destroy)
    mainapp.mainloop()


#this function allow you to know if after scanning with clamscan you have virus or not
def det_virus(val):
    chaine=val.split(" ")
    chaine_list=chaine[2]
    #print(chaine_list)
    coup_chaine=[i for i in chaine_list]
    #print(coup_chaine)
    coup_chaine.remove("\n")
    #print(coup_chaine)
    result="".join(coup_chaine)
    finish=int(result)
    return finish

#this function who allow you to move your file in respective folder
# image file in folder image, Music file in Music folder ....

#if you have another extension files, you can add here, on the list
def rangements():
        image = [".jpg", ".png", ".jpeg", ".gif", ".bmp", ".svg", ".drw", ".dwg",".dxf",".eps",".ico",".psd",".tif"]
        pdf = [".pdf"]
        word = [".odt", ".doc", ".docx", ".dot",".dotx"]
        text = [".txt", ".md",".rtf",".list"]
        presentation = [".odp", ".pptx", ".ppt", ".ppsx",".pps",".ppt",".pub"]
        tableur=[".xls",".xlsx",".ods"]
        compressed = [".zip", ".rar", ".deb", ".tar.xz", ".tar.gz", ".tar.bz2", ".gz", ".tgz",".ace",".rmp"]
        music = [".mp3", ".wav",".wmv",".opus",".m4a",".ogg"]
        video = [".mkv", ".mp4", ".avi", ".wmv", ".mov", ".flv", "webm", ".mpg",".qt"]
        torrent = [".torrent"]
        windows = [".exe",".msi"]
        programmation = [".py", ".sh", ".csv", ".jar", ".java",".jav", ".ino", ".bin",".vcf",".c",".class",".cpp",".css",".dll",".h",".html",".php",".pl",".sql"]
        font=[".ttf"]
        Iso=[".iso",".img",".ova"]

        liste = glob.glob("*")
        liste_extension=[]

        for i in liste:
            file_name,extension=splitext(i)
            liste_extension.append(extension)

        liste_extension=set(liste_extension)

# move files in respective folders
        for j in liste_extension:
            if j in image:
                os.system("mv *{0} /home/{1}/Images".format(j,user))
            elif j in pdf:
                os.system("mv *{0} /home/{1}/Documents/PDF".format(j,user))
            elif j in word:
                os.system("mv *{0} /home/{1}/Documents/Writer".format(j,user))
            elif j in text:
                os.system("mv *{0} /home/{1}/Documents/Text".format(j,user))
            elif j in presentation:
                os.system("mv *{0} /home/{1}/Documents/Presentation".format(j,user))
            elif j in compressed:
                os.system("mv *{0} /home/{1}/Compressed".format(j,user))
            elif j in music:
                os.system("mv *{0} /home/{1}/Movie".format(j,user))
            elif j in video:
                os.system("mv *{0} /home/{1}/Music".format(j,user))
            elif j in torrent:
                os.system("mv *{0} /home/{1}/Downloads/Torrent".format(j,user))
            elif j in windows:
                os.system("mv *{0} /home/{1}/Downloads/Windows".format(j,user))
            elif j in programmation:
                os.system("mv *{0} /home/{1}/Downloads/Code_file".format(j,user))
            elif j in font:
                os.system("mv *{0} /home/{1}/Downloads/Font".format(j,user))
            elif j in Iso:
                os.system("mv *{0} /home/{1}/Downloads/Os".format(j,user))


#get name of user
user=os.getlogin()
os.chdir("/home/{0}/Downloads".format(user))
Scan_print()
exit()
