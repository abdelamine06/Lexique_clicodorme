<p align="center" style="display: flex; 
align-items: baseline; 
justify-content: space-evenly;
flex-direction: row";
>
<img src="https://www.u-bordeaux.fr/var/ezdemo_site/storage/images/media/site-institutionnel/images/images-blandine-test/banniere-idv-gif-anime/16065-1-fre-FR/Banniere-idv-gif-anime_Grande.gif" width="250">
<img src="http://www.labri.fr/perso/bpinaud/images/logo-LaBRI-2011.jpg" width="100">
</p>

# Master 1 Informatique - Projet de programmation
-----------------

# Sommaire
1. [Projet : Le Clicodrome de LeFFF](#project)
2. [1ère release - 21 février 2019](#realease1)
3. [Release finale - Avril 2019](#releaseFinal)
4. [Pré-requis](#requirements)  
5. [Manuel d'installation](#manuel)  
5.1 [Déploiement d'une base de données](#deployment)  
5.2 [Importation d'un lexique en base de données](#import)  
5.3 [Lancement de l'application web](#launch)
6. [Arborescence du projet](#manuel)
7. [L'équipe](#team)
8. [Références](#references)
9. [Licence](#license)

<a name="project"></a>
## Projet : Le Clicodrome de LeFFF

Le Lexique des formes fĺechies du francais, appelé le **LeFFF** est un lexique contenant des mots ainsi que les formes fléchies de chacun des mots (conjugaison et déclinaisons du mot). 
Aujourd'hui il n'existe pas d'outil permettant d'interagir avec ce lexique, que ce soit pour l'enrichir ou le corriger.
L'objectif du projet est donc de réaliser une application web facilitant la manipulation de ce lexique, tout en permettant aux contributeurs d'enrichir la base de donnée du lexique à travers l'ajout d'expressions ou de mots.
<a name="realease1"></a>
## 1ère release - 15 février 2019
A ce stade du développment à été développé :
- La base de données
- L'interface graphique
    * écran d'accueil
    * écran de recherche
    * écran d'ajout d'un mot

- Traitement back-end 
    * Recherche de mot dans la base de données
    * Ajout d'un mot en base de données (début)
    * Consultation d'un mot (sans génération des formes fléchies)

<a name="releaseFinal"></a>
## Release finale - Avril 2019
todo************
**Amélioration possibles :**
todo************

<a name="requirements"></a>
## Pré-requis
python 3 : [Python](https://www.python.org)3.7.6 ou une version supérieure
Django 3 : [django](https://www.djangoproject.com)3.0.1 ou une version supérieure
  
<a name="manuel"></a>
## Manuel d'installation

commencez par obténir la copie du projet avec la commande :

git clone https://services.emi.u-bordeaux.fr/projet/git/clicodrome

<a name="deployment"></a>
### **Déploiement d'une base de données**
Pour déployer une base de données sur votre machine, il vous faut installer MySQL.   
    
__Pour mac os :__ 
Installer python3 avec la commande :  

    $ brew install python

Installer django : 

    $ python -m pip install Django

    $ python3 -m pip3 install Django

Installer MySQL :   
    
    $ brew install mysql

  
__Pour Linux :__ 
Installer python3 avec la commande :  
    
     $ sudo apt-get install python3

Installer django : 

    $ pip install Django
    $ pip3 install Django

Installer MySQL :   
    
    $ sudo apt install mysql-server


Vous pouvez consultez l'état de votre serveur à l'adresse [http://localhost](http://localhost). Pour accéder à l'administration de django, rendez-vous à l'adresse [http://localhost/admin](http://localhost/admin)

__Création de la base de données de la base:__  
Après avoir configuré les accès pour MySQL/Django,connectez-vous et créez une nouvelle base de données.  
Nous vous conseillons de nommer votre nouvelle base "db_clicodrome" afin d'évitez des configuration supplémentaires.

__Génération de l'architecture de la base de données :__  
Le framework Django et son ORM va nous permettre de générer l'architecture de la base de données automatiquement. 
il suffit de faire les configurations dans setting.py

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_clicodrome',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '3306',
    }
} 
'''

La dernière étape consiste à installer les dépendances du projet  
et les migrations d'architecture de la base de données avec les commandes :   

    $ python3 manage.py migrate

    $ python3 manage.py makemigrations

***Félicitations, votre base est enfin configurée et prête à être utilisée !***

<a name="import"></a>
### **Importation d'un lexique en base de données**

******todo

<a name="launch"></a>
### **Lancement de l'application web**

    $ python3 manage.py runserver
    

***Félicitations, votre application web est lancée. Rendez-vous à l'adresse [http://localhost:8000](http://localhost:8000) pour y accéder !***

<a name="tree"></a>

## Arborescence du projet
```
.
|-- data
|-- docs
|-- organiz
|-- src
    |-- clicodrome
    
```

Vous trouverez dans le répertoire ``` organiz``` les comptes rendus des différents TDs réalisés avec notre chargé de TD, au format .tex. 

Vous trouverez dans le répertoire ``` docs ```  la documentation du projet (cachier des besoins et mémoire) au format LaTeX.

Vous trouverez dans le répertoire ``` src ```  le code de l'application web du projet. Cette application possède un back-end réalisé en Python avec [Django](https://www.djangoproject.com) et le front réalisé avec [js, css,html, jquery](https://XXXXXXXX/).  


<a name="team"></a>
## L'équipe

* DIALLO Abdoul Ghadiri
* ROUSSEL Damien
* DAOUDI Yassir
* MEHDAOUI Abdelamine 
* El GUERCH Souhail 

<a name="reference"></a>
## Références

* [http://www.labri.fr/perso/clement/lefff/](http://www.labri.fr/perso/clement/lefff/)
                            
* [http://alpage.inria.fr/~sagot/](http://alpage.inria.fr/~sagot/)
                                 
* **Sagot B 2018** *"Informatiser le lexique: Modélisation, développement et exploitation de lexiques morphologiques, syntaxiques et sémantiques"*, HDR in Computer Science, Sorbonne Université, Paris, France
        
* **Clément, L., B. Sagot et B. Lang. 2004**, *« Morphology based automatic acquisition of large- coverage lexica»*, dans Proceedings of the 4th International Conference on Language Resources and Evaluation (LREC 2004), Lisbonne, Portugal, p. 1841–1844.
                 
* **Sagot, B. 2010,** *« The Lefff , a freely available, accurate and large-coverage lexicon for french »*, dans Proceedings of the 7th International Conference on Language Resources and Evaluation (LREC 2010), La Valette, Malte.

<a name="license"></a>
## Licence libre
Le Clicodrome de LeFFF est un projet universitaire - Université de Bordeaux. 
