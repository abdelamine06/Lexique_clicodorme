from main.models import *

def exportMots(mots):
    fichier=open("export.txt","w")
    for mot in mots:
        ligne=mot.Mot+' '+str(mot.Table)+' '+mot.Infos+'\n'
        fichier.write(ligne)
    fichier.close()
    return

def exportTousMots():
    mots=Mot.objects.all()
    fichier=open("export.txt","w")
    for mot in mots:
        ligne=mot.Mot+' '+str(mot.Table)+' '+mot.Infos+'\n'
        fichier.write(ligne)
    fichier.close()
    return

def importMots(nom):
    fichier=open(nom, "r")
    lignes=fichier.readlines()
    fichier.close()
    for ligne in lignes:
        elements=ligne.strip().split(' ')
        if len(elements)!=3:
            return False
        mot=Mot(Mot=elements[0],Table=elements[1],Infos=elements[2])
        mot.save()
    return
