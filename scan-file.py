"""
This script allow automatc you to scan your news files with clamav and move file in respective directory


"""

import os
import tkinter
import glob
import shutil
from os.path import splitext

#Affichage
mainapp=tkinter.Tk()
mainapp.title("Alerte")

#fonction permettant de sorti le nombre de virus
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

#fonction qui gére les rangements
def rangements():
        image = [".jpg", ".png", ".jpeg", ".gif", ".bmp", ".svg", ".drw", ".dwg",".dxf",".eps",".ico",".psd",".tif"]
        pdf = [".pdf"]
        word = [".odt", ".doc", ".docx", ".dot"]
        text = [".txt", ".md",".rtf"]
        presentation = [".odp", ".pptx", ".ppt", ".ppsx",".pps",".ppt",".pub"]
        tableur=[".xls",".xlsx",".ods"]
        compressed = [".zip", ".rar", ".deb", ".tar.xz", ".tar.gz", ".tar.bz2", ".gz", ".tgz",".ace","."]
        music = [".mp3", ".wav",".wmv"]
        video = [".mkv", ".mp4", ".avi", ".wmv", ".mov", ".flv", "webm", ".mpg",".qt"]
        torrent = [".torrent"]
        windows = [".exe",".msi"]
        programmation = [".py", ".sh", ".csv", ".jar", ".java",".jav", ".ino", ".bin",".vcf",".c",".class",".cpp",".css",".dll",".h",".html",".php",".pl",".sql"]
        police=[".ttf"]

        liste = glob.glob("*")
        liste_extension=[]

        for i in liste:
            file_name,extension=splitext(i)
            liste_extension.append(extension)

        liste_extension=set(liste_extension)

        for j in liste_extension:
            if j in image:
                os.system("mv *{0} /home/misterpi/Images".format(j))
            elif j in pdf:
                os.system("mv *{0} /home/misterpi/Documents/pdf".format(j))
            elif j in word:
                os.system("mv *{0} /home/misterpi/Documents/odt-docx".format(j))
            elif j in text:
                os.system("mv *{0} /home/misterpi/Documents/texte".format(j))
            elif j in presentation:
                os.system("mv *{0} /home/misterpi/Documents/presentation".format(j))
            elif j in compressed:
                os.system("mv *{0} /home/misterpi/Compressed".format(j))
            elif j in music:
                os.system("mv *{0} /home/misterpi/Vidéos".format(j))
            elif j in video:
                os.system("mv *{0} /home/misterpi/Musique".format(j))
            elif j in torrent:
                os.system("mv *{0} /home/misterpi/Téléchargements/torrent".format(j))
            elif j in windows:
                os.system("mv *{0} /home/misterpi/Téléchargements/Autre/exe".format(j))
            elif j in programmation:
                os.system("mv *{0} /home/misterpi/Téléchargements/test".format(j))



user=os.getlogin()
os.chdir("/home/{0}/Téléchargements".format(user))
scan=os.popen("clamscan --move=virus | grep Infected").read()
nb_virus=det_virus(scan)
if nb_virus == 0:
    app=tkinter.Label(mainapp,text=("VIRUS PAS TROUVER"))
    app.pack()
elif nb_virus == 1:
    app=tkinter.Label(mainapp,text=("VIRUS TROUVER \n consulter le dossier virus pour voir les copies"))
    app.pack()
elif nb_virus == 2:
    app=tkinter.Label(mainapp,text=("Une erreur (s) s'est produite."))
    app.pack()


rangements()
fini=tkinter.Label(mainapp,text=("vos fichiers sont étaient déplacer avec success"))
fini.pack()

mainapp.mainloop()
