import tkinter as tk
import requests
from tkinter import messagebox, ttk
import webbrowser

version=1.0
Nom_application='Bot'

def mise_a_jour():
    
    try:
        response = requests.get(
            'https://raw.githubusercontent.com/JamesBond65/Hujub/master/Rnadom%201/Random/Version.txt')
        data = response.text
        

        if float(data) > float(version):
            messagebox.showinfo('Software Update', 'Update Available!')
            message = messagebox.askyesno('Update !', f'{Nom_application} {version} needs to update to version {data}')
            if message is True:
                       
                response = requests.get('https://raw.githubusercontent.com/JamesBond65/Hujub/master/Rnadom%201/Principale.py')
                code = response.text
                print(code)

                with open("Random.1/ScredAIO1.py", "w") as f:
                    f.write(code)
                
                pass


            else:
                pass
        else:
            messagebox.showinfo('Software Update', 'No Updates are Available.')
            
    except Exception as e:
        messagebox.showinfo('Software Update', 'Unable to Check for Update, Error:' + str(e))




mise_a_jour()






def afficher_equipements():

    with open("data.txt", "r") as file:
        numérotation = 1

        for ligne in file:
            chaine = ligne.split("#")
            print(numérotation, ")  ", end="")
            numérotation = numérotation + 1

            for valeur in range(len(chaine)):
                print(chaine[valeur], end=" ")

            print("")


def ajouterEquippement():

    processeur = " [1] processeur : #" + input(
        "Entrer le modele et la vitesse du processeur :"
    )
    ram = " [2]ram : #" + input("Entrer la taille de la RAM :")
    bus = " [3]bus : #" + input("Enter le type de bus (PCI, SATA...) :")
    carteGraphique = " [4] carteGraphique : #" + input("Enter le modele de la carte graphique :")
    portVideo = " [5] portVideo : #" + input("Entrer les ports présents sur l'appareil (VGA, HDMI, Thunderbolt,...):")
    resolutionEcran = "[6] resolutionEcran : #" + input("Entrer la résoution de l'écran :")
    tailleEcran = " [7] tailleEcran : #" + input("Entrer la taille de l'ecran :")
    nombreDePortsUSB = " [8] nombreDePortsUSB : #" + input("Entrer le nombre de ports USB :")
    tailleDisqueSSD = " [9] tailleDisqueSSD : #" + input("Indique la capacité du disque du ou du SSD :")
    graveurCD = " [10] graveurCD : #" + input("Indiquez si l'appareil possede un graveur/lecteur CD :")
    carteReseau = " [11] carteReseau : #" + input("Indiquez le constructeur et le débit de la carte reseau :")
    wifi = " [12] wifi : #" + input("Entrer le type et la bande frequence du wifi :")
    bluetooth = " [13] bluetooth : #" + input("Indiquez le type de bleutooth :")
    fabricant = " [14] fabricant : #" + input("Entrer le fabriquant du PC :")
    fournisseur = " [15] fournisseur : #" + input("Entrer le fournisseur du PC :")
    dateAchat = " [16] dateAchat : #" + input("Entrer la date de l'achat:")
    localisation = " [17] localisation : #" + input("Entrer la localisation de l'appereil dans l'établissement :")
    utilisateur = " [18] utilisateur : #" + input("Entrer les utilisateurs ou le nombre d'utilisateur pouvant acceder au PC :")
    # J'ajoute tt les éléments

    sauvegarde = input("Voules vous sauvegarder les données saisies ? tapez 'o' ou 'n' ")

    if sauvegarde == "o":
        file = open("data.txt", "a")
        file.write(
            processeur
            + "#"
            + ram
            + "#"
            + bus
            + "#"
            + carteGraphique
            + "#"
            + portVideo
            + "#"
            + resolutionEcran
            + "#"
            + tailleEcran
            + "#"
            + nombreDePortsUSB
            + "#"
            + tailleDisqueSSD
            + "#"
            + graveurCD
            + "#"
            + carteReseau
            + "#"
            + wifi
            + "#"
            + bluetooth
            + "#"
            + fabricant
            + "#"
            + fournisseur
            + "#"
            + dateAchat
            + "#"
            + localisation
            + "#"
            + utilisateur
        )
        file.close()  # J'enregistre ci dessus les nouveaux parametres dans le fichier

    elif sauvegarde == "n":
        print("Vous avez choisi de ne pas enregister les données, vous allez être redirigé vers le menu principal.")
        input("Appuyez sur une touche pour continuer")
        menu()

    else:
        print("Vous avez saisie une touche non spécifiée.")
        print("Vos données ont été sauvegardées.")
        file = open("data.txt", "a")
        file.write(
            processeur
            + "#"
            + ram
            + "#"
            + bus
            + "#"
            + carteGraphique
            + "#"
            + portVideo
            + "#"
            + resolutionEcran
            + "#"
            + tailleEcran
            + "#"
            + nombreDePortsUSB
            + "#"
            + tailleDisqueSSD
            + "#"
            + graveurCD
            + "#"
            + carteReseau
            + "#"
            + wifi
            + "#"
            + bluetooth
            + "#"
            + fabricant
            + "#"
            + fournisseur
            + "#"
            + dateAchat
            + "#"
            + localisation
            + "#"
            + utilisateur
        )
        file.close()  # J'enregistre ci dessus les nouveaux parametres dans le fichier
        print("Appuyez sur une touche pour continuer.")
        input("")

    x = True
    compteur = 0
    index = 18
    while x == True:
        logiciel_supl = input("Voulez vous rajouter des logiciels ? tapez 'o' ou 'n' ")
        if logiciel_supl == "n":
            file = open("data.txt", "a")
            file.write("#\n")
            file.close()
            x = False  # le break enleve le while du menu donc fallait le faire a la mano

        else:
            compteur += 1
            index += 1
            nomDuLogiciel = (" [%d] nom du system du logiciel  : #" % index) + input("Indiquez le nom du logiciel :")
            index += 1
            editeur = (" [%d] éditeur du logiciel : #" % index) + input("Entrer l'editeur du logiciel :")
            index += 1
            version = (" [%d] éditeur du logiciel : #" % index) + input("Entrer la version du logiciel :")
            index += 1
            dateExpiration = (" [%d] date d'expiration du logiciel  : #" % index) + input("Entrer la date d'expiration de la liscence du logiciel :")
            file = open("data.txt", "a")
            file.write(
                "#"
                + nomDuLogiciel
                + "#"
                + editeur
                + "#"
                + version
                + "#"
                + dateExpiration
            )
            file.close()

    print("\nVos paramètres on bien été enregistrés.")
    print("Appuyez sur une touche pour continuer")
    input("")


def mettre_a_jour():

    afficher_equipements()

    mise_a_jour = int(input("\nQuelle ligne souhaitez vous mettre à jour ?"))
    print("Vous avez choisi la ligne numéro :", mise_a_jour)

    terme_changer = int(input("\nQuel est le numero du terme que vous voulez mettre à jour ? (numéro entre crochets) :"))
    nouvelle_valeur = input("Indiquez la nouvelle valeur :")
    f = open("data.txt", "r")
    lines = f.readlines()

    chaine = lines[mise_a_jour - 1]

    chaine = chaine.split("#")
    del (chaine[len(chaine)-1])
    chaine[(terme_changer * 2) - 1] = nouvelle_valeur
    nouvelle_chaine = ""
    for i in range(len(chaine)):
        nouvelle_chaine = nouvelle_chaine + str(chaine[i]) + "#"
    nouvelle_chaine = nouvelle_chaine + "\n"
    lines[mise_a_jour - 1] = nouvelle_chaine
    f.close()
    f = open("data.txt", "w")
    f.writelines(lines)
    print("\nValeur changée !")
    f.close()
    input("Appuyez sur une touche pour continuer.")
    menu()


def supprimer_equipement():

    choix_supp = int(input("\nVoulez vous supprimer un ordinateur (1) ou un logiciel d'ordinateur (2) ?:"))

    if choix_supp == 1:

        afficher_equipements()
        try:
            ligne_supression = int(input("\nSur quelle ligne se situe l'équippement que vous voulez supprimer ? :"))
            f = open("data.txt", "r")
            lines = f.readlines()
            del lines[ligne_supression-1]
            f.close()
            f = open("data.txt", "w")
            f.writelines(lines)
            f.close()
            print("\nL'ordinateur séléctioné à bien été supprimé.")
            input("Appuyez sur une touche pour continuer.")
            menu()
        
        except IndexError as e:
            print("\nLa ligne que vous avez choisi n'existe pas, veuillez recommencer.")
            input("Appuyez sur une touche pour continuer.")
            supprimer_equipement()

    elif choix_supp == 2:

        afficher_equipements()

        mise_a_jour = int(input("\nQuelle ligne souhaitez vous mettre à jour ? :"))
        print("Vous avez choisi la ligne numéro :", mise_a_jour)

        logiciel_supp = 2 * (
            int(
                input("\nQuel est le numéro du terme que vous voulez mettre à jour ? (numéro entre crochets)")
            )
        )
        f = open("data.txt", "r")
        lines = f.readlines()
        chaine = lines[mise_a_jour - 1]
        chaine = chaine.split("#")
        for qbc in range(8):
            del chaine[logiciel_supp - 2]
        nouvelle_chaine = ""
        for i in range(len(chaine)):
            nouvelle_chaine = nouvelle_chaine + str(chaine[i]) + "#"
            nouvelle_chaine = nouvelle_chaine + "\n"
        lines[mise_a_jour - 1] = nouvelle_chaine
        f.close()
        f = open("data.txt", "w")
        f.writelines(lines)
        print("valeur changée")
        f.close()
        print("Le logiciel séléctioné à bien été supprimé.")
        input("Appuyez sur une touche pour continuer.")
        menu()


def rechercher_par_parametre():

    type_para = int(input("Voulez vous rechercher :\n 1/Hardware\n 2/Software :"))

    if type_para == 1:
        hardware = {
            1: "processeur",
            2: "ram",
            3: "bus",
            4: "carteGraphique",
            5: "portVideo",
            6: "resolutionEcran",
            7: "tailleEcran",
            8: "nombreDePortsUSB",
            9: "tailleDisqueSSD",
            10: "graveurCD",
            11: "carteReseau",
            12: "wifi",
            13: "bluetooth",
            14: "fabricant",
            15: "fournisseur",
            16: "dateAchat",
            17: "localisation",
            18: "utilisateur",
        }
        print(hardware.values())
        type_hardware = str()
        while type(type_hardware) == str:
            type_hardware = str(input("Quel harware souhaitez vous ? Ecrivez le nom du hardware :"))  # Demande le parametre recherché.
            for abc in hardware.keys():
                if hardware[abc] == type_hardware:
                    type_hardware = abc  # je la transfforme en nombre pour l'utiliser dans une liste
                    break
            if type(type_hardware) == str:
                print("valeur inconnue")

        choix_recherche = int(
            input(
                "1) Afficher tout les équipements pour le paramètre demandé.\n 2)Rechercher un équippement spécifique. :"
            )
        )
        f = open("data.txt", "r")
        lines = f.readlines()
        numerotation = 1
        if choix_recherche == 1:
            for i in range(len(lines)):
                chaine = lines[i]
                chaine = chaine.split("#")
                print(
                    numerotation,
                    ")",
                    chaine[2 * type_hardware - 2],
                    chaine[2 * type_hardware - 1],
                )
                numerotation += 1

        elif choix_recherche == 2:
            terme_recherche = str(input("Quel est le terme recherche?"))
            for i in range(len(lines)):
                chaine = lines[i]
                chaine = chaine.split("#")
                if chaine[2 * type_hardware - 1] == terme_recherche:
                    print(
                        numerotation,
                        ")",
                        chaine[2 * type_hardware - 2],
                        chaine[2 * type_hardware - 1],
                    )
                numerotation += 1
        f.close()

    elif type_para == 2:
        software = {1: "nomDuLogiciel", 2: "editeur", 3: "version", 4: "dateExpiration"}
        print(software.items())
        type_software = int(input("Quel software souhaitez vous ?"))
        type_software = 2 * type_software - 1
        choix_recherche = int(input("choix_recherche"))
        f = open("data.txt", "r")
        lines = f.readlines()
        numerotation = 1
        if choix_recherche == 1:
            for i in range(len(lines)):
                chaine = lines[i]
                chaine = chaine.split("#")
                for abc in range(36):
                    del chaine[0]
                for thor in range(type_software, len(chaine), 8):
                    print(numerotation, ")", chaine[thor])
                numerotation += 1

        elif choix_recherche == 2:
            terme_recherche = str(input("quel est le terme recherche?"))
            for i in range(len(lines)):
                chaine = lines[i]
                chaine = chaine.split("#")
                for xyz in range(36):
                    del chaine[0]
                for Odin in range(type_software, len(chaine), 8):
                    if chaine[Odin] == terme_recherche:
                        x = int()
                        for Zeus in range(0, type_software, 8):
                            x = Zeus
                            for Athena in range(8):

                                print(numerotation, ")", chaine[x])
                                x += 1
                numerotation += 1


def menu():

    print(
        "Bienvenue dans le programme\n\n 1.Saisir nouvel équipement.\n 2.Mettre à jour ou supprimer un équipement.\n 3.Voir la liste des équipements.\n 4.Rechercher un équipement. \n 5.Quitter l'application."
    )
    choix = int(input("\nEntrer votre choix :"))

    if choix == 1:
        print("Vous avez choisi : Ajouter un equipement.")
        ajouterEquippement()  # Renvoie à la fonction Ajouter equipement.
        menu()

    if choix == 2:
        print(
            "\nVoulez vous :\n1.Mettre à jour un équipement.\n2.Supprimer un équipement."
        )  # Renvoie à la fonction mettre à jour ou supprimer un équipement.
        second_choix = int(input("Entrer votre choix (1 ou 2):"))

        if second_choix == 1:
            print(
                "Quel équipement souhaitez-vous mettre à jour ?\n "
            )  # Renvoie à la fonction mettre à jour définie ci-dessus.
            mettre_a_jour()

        if second_choix == 2:
            print(
                "Quel équipements souhaitez-vous supprimer ?,\n "
            )  # Renvoie à la fonction supprimer equipement.
            supprimer_equipement()

    if choix == 3:
        print(
            "Voici la liste des équipements:\n"
        )  # Affiche la liste des équipement déja saisis.
        with open("data.txt", "r") as file:
            numérotation = 1
            for ligne in file:
                chaine = ligne.split("#")
                print(numérotation, ")  ", end="")
                numérotation = numérotation + 1

                for valeur in range(len(chaine)):
                    print(chaine[valeur], end=" ")

                print("")

        input("\nAppuyez sur une touche pour continuer.\n")
        menu()

    if choix == 4:
        rechercher_par_parametre()
        menu()

    if choix == 5:
        print("A plus tard !")
        exit(0)

    else:
        print(
            "Le paramètre entré n'est pas un entier de la liste, recommencez s'il vous plait.\n"
        )
        menu()


#while 1:
    #menu()