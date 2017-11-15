===================================
Informations générales playWithTime
===================================

:Autheur:            `Poltergeist42 <https://github.com/poltergeist42>`_
:Projet:             playWithTime
:dépôt GitHub:       https://github.com/poltergeist42-myLib/playWithTime.git
:documentation:      https://poltergeist42-mylib.github.io/playWithTime/
:Licence:            CC BY-NC-SA 4.0
:Liens:              https://creativecommons.org/licenses/by-nc-sa/4.0/

------------------------------------------------------------------------------------------

Déscription
===========

 Cette librairie pemet de manipuler des éléments de temps :
    
    * Temps écoulé entre deux référence de temps
    * Manipulation du format d'affichage des dates
    
    #. module playWithTime
        Ce module comprend 2 Class :
        
        * C_PlayWithTime (Class mère) qui permet de manipuler le temps sous forme de
          nombres décimaux. Ces décimaux peuvent être calculés soit en fonction de "Epoch"
          soit en fonction de "Clock".
          
        * C_Pwt_U (Class fille) qui permet de manipuler le temps dans un format
          compréhensible sous la forme xxHxxMxxS.
          
    #. module playWithDate
        Ce module comprend 1 Class
        
        * C_PlayWithDate qui permet de manipuler la date sous différentes formes

------------------------------------------------------------------------------------------

Installation
============

**N.B** : vous devez être Root / administrateur pour effectuer cette opération.

 Depuis une invite de commande, ce placer dans le dossier "_3_software\playWithTime_pac" puis
 excuter la commande setup : ::
 
    cd .\_3_software\playWithTime_pac
    python setup.py install

------------------------------------------------------------------------------------------
    
Désinstallation
===============

**N.B** : vous devez être Root / administrateur pour effectuer cette opération.

  Depuis une invite de command, executer la commande : ::
  
    pip list --format=columns
        # permet d'afficher la liste des paquages installés
        
    pip uninstall [nom_du_paquet]
    
    ex :
    pip uninstall playwithtime-pac
    
------------------------------------------------------------------------------------------

Utilisation
===========

Pour pouvoir utiliser ce paquet depuis un script ou depuis votre interpréteur, vous devez
saisir : ::

    from playWithTime_pac.playWithTime import C_PlayWithTime
    from playWithTime_pac.playWithTime import C_Pwt_U
    from playWithTime_pac.playWithDate import C_PlayWithDate

------------------------------------------------------------------------------------------

Arborescence du projet
======================

Pour aider à la compréhension de mon organisation, voici un bref déscrptif de
l'arborescence de se projet.Cette arborescence est à reproduire si vous récupérez ce dépôt
depuis GitHub. ::

	openFile               # Dossier racine du projet (non versionner)
	|
	+--project             # (branch master) contient l'ensemble du projet en lui même
	|  |
	|  +--_1_userDoc       # Contien toute la documentation relative au projet
	|  |   |
	|  |   \--source       # Dossier réunissant les sources utilisées par Sphinx
	|  |
	|  +--_2_modelisation  # contien tous les plans et toutes les modélisations du projet
	|  |
	|  +--_3_software      # Contien toute la partie programmation du projet
	|  |
	|  \--_4_PCB           # Contient toutes les parties des circuits imprimés (routage,
	|                      # implantation, typon, fichier de perçage, etc
	|
	\--webDoc              # Dossier racine de la documentation qui doit être publiée
	   |
	   \--html             # (branch gh-pages) C'est dans se dosier que Sphinx vat
	                       # générer la documentation à publié sur internet

