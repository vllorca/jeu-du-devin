'''
                    ######################
                    #    Jeu du devin    #
                    ######################
'''

import random           # Pour utiliser random.randint(x,y)

rand_sup = 9999         # Borne max pour le nombre à trouver
rand_inf = 1            # Borne min pour le nombre à trouver

'''
        ###    La machine fait deviner le nombre    ###


R0 : Faire deviner un nombre à l'utilisateur

R1 : Comment faire deviner un nombre :
    - Choisir un nombre
            solution : out
    - Faire deviner ce nombre
            solution : in
            nb essai : out
    - Féliciter ce joueur
            nb essai : in

R2 : Comment "faire deviner ce nombre" ?
    - nb essai = 0
    - Trouvé = False
    - While non trouvé :
        - Demander la proposition de l'utilisateur     
                proposition : out
        - Incrémenter le nombre d'essai
                nb essai : inout 
        - Donner un indice (trop grand, trop petit, ou trouvé)
                proposition : in
                solution : in 
'''


def jeu_devin_user():
    '''
    Faire deviner un nombre à l'utilisateur en un minimum d'essai :
        - La machine choisit un nombre
        - L'utilisateur essaie de deviner le nombre
    '''
    # Choisir un nombre 
    solution = random.randint(rand_inf, rand_sup)
    ans = 0         # Réponse de l'utilisateur
    i = 1           # Nombre d'essai
    print("J'ai choisi un nombre entre 1 et 9999")

    # Demander la proposition à l'utilisateur
    while ans != solution :
        ans = int(input(f'Proposition {i} : '))
        # Répondre en fonction du nombre - machine
        #   Nombre trop petit
        if solution > ans :          
            print("Trop petit !")
        #   Nombre trop grand
        elif solution < ans :
            print("Trop grand !")
        #   Quitter le jeu
        elif solution == 0 :
            ans_mode = input("Voulez vous vraiment abandonner (o/*) ? ")
            if ans_mode == 'o' :
                print("Abandon de la partie !")
        #   Nombre trouvé
        else :
            print(f'Bien joué ! Vous avez trouvé en {i} essais.')
        i += 1      #incrémente le nombre d'essai


'''
        ###   La machine joue au jeu du devin    ###


R0 : Faire deviner un nombre à la machine

R1 : Comment faire deviner un nombre :
    - Demander à l'utilisateur de choisir un nombre
            solution : inout
    - Trouver ce nombre
            solution : in
            nbe : out
    - Recevoir les félicitations
            nbe : in

R2 : Comment "Trouver ce nombre"
    - nb essai = 0
    - Trouvé = False
    - While non trouvé :
        - Proposer le résultat de la dichotomie
                proposition : out
        - Incrémenter le nombre d'essai
                nb essai : inout 
        - Recevoir un indice (trop grand, trop petit, ou trouvé)
                proposition : in
                solution : in 
        - Changer les bornes de la dichotomie

'''

def jeu_devin_machine():
    '''
    Faire deviner un nombre à la machine :
        - L'utilisateur choisit un nombre
        - La machine doit le trouver
    '''

    i = 0                   # nombre d'essai
    a = rand_inf            # borne min
    b = rand_sup            # borne max
    m = (a + b) // 2        # median pour la dichotomie

    ans_user = ''               # réponse de l'utilisateur à la proposition de la machine
    nombre = ''                 # l'utilisateur a-t-il choisi le nombre à faire deviner
    bool_triche = False         # Booléen pour  vérifier si l'utilisateur a triché (simplifié)
    
    while nombre != 'o' :       #Attend que l'utilisateur ai choisi un nombre
        nombre = input("Avez vous choisi un nombre compris entre  1 et 9999 (o/n) ? ")
    
    while (ans_user != 't') and (ans_user != 'T'):  #Attend que la machine trouve le nombre
        m = (a + b) // 2                            # calcul pour la dichotomie
        print(f'Proposition {i} : {m}')
        ans_user = input(f'Trop (g)rand >, trop (p)etit < ou (t)rouvé = ? : ')
        if ans_user == 'p' or ans_user == 'P' or ans_user == '<':       # Trop petit
            a = m                                                           # La borne inf. est modifiée
        elif ans_user == 'g' or ans_user == 'G' or ans_user == '>':     # Trop grand
            b = m                                                           # la borne sup. est modifiée
        elif ans_user == 't' or ans_user == 'T' or ans_user == '=':     # Trouvé 
            if int(input("Quel nombre avez-vous choisi ? : ")) == m :       # On verifie qu'il ny a pas eu de triche
                bool_triche = False
            else :
                bool_triche = True
        elif ans_user == '0' :                                          #l'utilisateur abandonne la partie
            print('Abandon de la partie')
            break
        else :                                                          # Réponse non valide
            print("Je n'ai pas compris la réponse")
        i += 1                                                              # incrémente le nombre d'essai
s
    if ans_user != '0' and bool_triche == False :                       # Sans triche et abandon 
        print(f'Bravo ! Le nombre {m} a été trouvé en {i} essais!')
    elif bool_triche == True :                                          # Si l'utilisateur triche
        print('Il y a eu de la triche !')



'''
                Jeu du devin avec choix du
                        mode de jeu


R0 : Choisir un mode de jeu et continuer de jouer

R1 : Comment "Choisir un mode de jeu et continuer de jouer" ? 
        - Demander à l'utilisateur le mode voulu
                mode : inout
        - Lancer le mode de jeu correspondant
                mode : in
                game_mod : out
        - Demander si l'utilisateur veut rejouer
                next_game = in
'''

def jeu_devin():
    '''
    Jeu du devin avec choix du joueur :
        1. L'utilisateur devine le nombre
        2. La machine devine le nombre
    '''

    bool_next = True        #Booléen pour le choix de continuer à jouer 

    while bool_next :       #Le jeu continue tant que l'utilisateur ne quitte pas
        # Proposer le choix du joueur
        print("1- L'ordinateur choisit un nombre et vous le devinez")
        print("2- Vous choisissez un nombre et l'ordinateur devine")
        print("0- Quitter le programme")
        print('')
        
        # Choisir le mode de jeu
        mode = int(input("Votre choix : "))
        assert 0 <= mode <=2
        print('')

        #Choisir le mode de jeu en fonction du joeur
        #   Quitter le jeu
        if mode == 0 :
            ans_mode = input("Voulez vous vraiment quittez (o/*) ? ")
            if ans_mode == 'o' :
                print("Au revoir ...")
                break
        #   Lancer le jeu avec l'utilisateur
        elif mode == 1 :
            jeu_devin_user()
        #   Lancer le jeu avec la machine
        elif mode == 2 :
            jeu_devin_machine()

        # Demander une nouvelle partie
        next_game = input("\nVoulez vous rejouez (o/n) ?")
        # Choisir de continuer a jouer
        if next_game == 'o' :       #Continuer à jouer
            bool_next = True        
        else :                      #Arrêter de jouer
            bool_next = False
            print("A bientôt ..")     

def main():
    print("\n \t ----- Jeu du devin ----- \n")
    jeu_devin()

if __name__ == "__main__":
    main()