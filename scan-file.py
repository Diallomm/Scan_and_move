"""
This script allow you to scan your news files with clamav

permet de connaitre l'extension d'un fichier
from os.path import splitext
file_name,extension = splitext('/home/lancaster/Downloads/a.ppt')

deplacer un fichier en Python
import shutil
shutil.move("source","Dest")

lister les fichiers dans un dossier
import glob
glob.glob("*")
"""

import os
import tkinter

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
        image = [".jpg", ".png", ".jpeg", ".gif", ".bmp"]
        pdf = [".pdf"]
        word = [".odt", ".doc", ".docx"]
        text = [".txt", ".md"]
        presentation = [".odp", ".pptx", ".ppt", ".ppsx"]
        compressed = [".zip", ".rar", ".deb", ".tar.xz", ".tar.gz", ".tar.bz2", ".gz", ".tgz"]
        music = [".mp3", ".wav"]
        video = [".mkv", ".mp4", ".avi", ".wmv", ".mov", ".flv", "webm"]
        torrent = [".torrent"]



user=os.getlogin()
os.chdir("/home/{0}/Téléchargements".format(user))
scan=os.popen("clamscan --move=virus | grep Infected").read()
nb_virus=det_virus(scan)
if nb_virus == 0:
    #print("VIRUS PAS TROUVER")
    app=tkinter.Label(mainapp,text=("VIRUS PAS TROUVER"))
    app.pack()
elif nb_virus == 1:
    #print("VIRUS TROUVER \n consulter le dossier virus pour voir les copies")
    app=tkinter.Label(mainapp,text=("VIRUS TROUVER \n consulter le dossier virus pour voir les copies"))
    app.pack()
elif nb_virus == 2:
    app=tkinter.Label(mainapp,text=("Une erreur (s) s'est produite."))
    app.pack()
    #print("Une erreur (s) s'est produite.")

mainapp.mainloop()
