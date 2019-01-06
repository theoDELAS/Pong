#coding: utf-8
from tkinter import *

#Création de la fenetre principale
fenetre = Tk()
fenetre.title('Pong Game')

#info dimensions ecran et fenetre
ecran_x = fenetre.winfo_screenwidth()
ecran_y = fenetre.winfo_screenheight()
fenetre_x = ecran_x - 5
fenetre_y = ecran_y - 75

#calcul pour faire spawn fenetre au centre de l'ecran
pos_x = (ecran_x // 2) - (fenetre_x //2)
pos_y = (ecran_y // 2) - (fenetre_y //2)

#Position de la fenetre au centre
geo = f'{fenetre_x}x{fenetre_y}+{pos_x}+{pos_y}'
fenetre.geometry(geo)

# Création du canvas
canevas = Canvas(fenetre, width = fenetre_x, height = fenetre_y, bg = "black")

# Coordonnées de la balle
x0 = fenetre_x // 2
x1 = x0 + 20
y0 = fenetre_y // 2
y1 = y0 + 20

# vitesse de la balle facile
dx1 = 5
dy1 = 3

# vitesse de la balle Normal
dx2 = 9
dy2 = 7

# vitesse de la balle Difficile
dx3 = 12
dy3 = 10


# variables relatives aux raquettes
debut_x1 = 10
fin_x1 = 25
debut_y1 = 400
fin_y1 = 525
debut_x2 = fenetre_x - 25
fin_x2 = debut_x2 + 15
debut_y2 = 400
fin_y2 = 525

# affichage des points
pts_j1 = 0
pts_j2 = 0

############### MENU PRINCIPAL #################
def init_canvas_menu():
    canevas.delete(ALL)
    canevas.create_text(fenetre_x // 2, 200, fill = "white", font = ("Roboto", 75), text = "MENU PRINCIPAL")
    bouton_regles.place(relx = 0.5, rely = 0.5, anchor = CENTER)

############### REGLES/CONTROLES ###############
def init_canvas_regles():
    canevas.delete(ALL)  
    bouton_parametres.place(relx = 0.5, rely = 0.8, anchor = CENTER)
    bouton_regles.place_forget()
    canevas.create_text(fenetre_x // 2, 200, fill = "white", font = ("Roboto", 75), text = "RELGES/CONTROLES")
    canevas.create_text(fenetre_x // 2, 400, fill = "white", font = ("Roboto", 25), text = "Le but est de faire passer la balle dans le but adverse")
    canevas.create_text(fenetre_x // 2, 500, fill = "white", font = ("Roboto", 25), text = "Le joueur 1 deplace sa raquette avec les touches du clavier :\n - Z pour monter\n  - S pour descendre")
    canevas.create_text(fenetre_x // 2, 700, fill = "white", font = ("Roboto", 25), text = "Le joueur 2 deplace sa raquette avec les touches directionnelles du clavier :\n - fleche du haut pour monter\n  - fleche du bas pour descendre")

############### PARAMETRES #####################
def init_canvas_parametres():
    canevas.delete(ALL)
    bouton_parametres.place_forget()
    canevas.create_text(fenetre_x // 2, 200, fill = "white", font = ("Roboto", 75), text = "PARAMETRES")
    bouton_facile.place(relx = 0.5, rely = 0.4, anchor = CENTER)
    bouton_normal.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    bouton_difficile.place(relx = 0.5, rely = 0.6, anchor = CENTER)

############### JEU FACILE #####################
def init_canvas_jeu_facile():
    global x0, x1, y0, y1, balle, joueur_1, joueur_2 
    canevas.delete(ALL)
    bouton_facile.place_forget()
    bouton_normal.place_forget()
    bouton_difficile.place_forget()
    bouton_regles.place_forget()
    bouton_quit.place_forget()
    canevas.create_line(fenetre_x // 2, 0, fenetre_x // 2, fenetre_y, fill = "white", width = 5)
    balle = canevas.create_oval(x0, y0, x1, y1, fill = "red")
    joueur_1 = canevas.create_rectangle(debut_x1, debut_y1, fin_x1, fin_y1, fill = "white")
    joueur_2 = canevas.create_rectangle(debut_x2, debut_y2, fin_x2, fin_y2, fill = "white")

    # déplacement de la raquettes
    def bas1(event):
        if canevas.coords(joueur_1)[3] < fenetre_y:
            canevas.move(joueur_1, 0, 70)
    def haut1(event):
        if canevas.coords(joueur_1)[1] > 0:
            canevas.move(joueur_1, 0, -70)
    def bas2(event):
        if canevas.coords(joueur_2)[3] < fenetre_y:
            canevas.move(joueur_2, 0, 70)
    def haut2(event):
        if canevas.coords(joueur_2)[1] > 0:
         canevas.move(joueur_2, 0, -70)
    # bind des touches pour déplacer les raquettes
    canevas.bind_all('<Down>', bas2)
    canevas.bind_all('<Up>', haut2)
    canevas.bind_all('<s>', bas1)
    canevas.bind_all('<z>', haut1)

    # Déplacement perpetuel de la balle
    def deplacement():
        global x0, y0, x1, y1, dx1, dy1, pts_j1, pts_j2
        # Variable collision balle/raquette
        x0_balle = canevas.coords(balle)[0]
        y0_balle = canevas.coords(balle)[1]
        x1_balle = canevas.coords(balle)[2]
        y1_balle = canevas.coords(balle)[3]
        x0_j2 = canevas.coords(joueur_2)[0]
        y0_j2 = canevas.coords(joueur_2)[1]
        x1_j2 = canevas.coords(joueur_2)[2]
        y1_j2 = canevas.coords(joueur_2)[3]
        x0_j1 = canevas.coords(joueur_1)[0]
        y0_j1 = canevas.coords(joueur_1)[1]
        x1_j1 = canevas.coords(joueur_1)[2]
        y1_j1 = canevas.coords(joueur_1)[3]
        # Création composants
        canevas.move(balle, dx1, dy1)
        if canevas.coords(balle)[0] > fenetre_x:
            init_canvas_gameover1()
        if canevas.coords(balle)[2] < 0 :
            init_canvas_gameover2()
        if canevas.coords(balle)[3] > fenetre_y or canevas.coords(balle)[1] < 0 :
            dy1 = -dy1
        if canevas.coords(balle)[2] > x0_j2 and y1_balle > y0_j2 and y0_balle < y1_j2 or canevas.coords(balle)[0] < x1_j1 and y1_balle > y0_j1 and y0_balle < y1_j1:
            dx1 = -dx1

        canevas.after(20,deplacement)
    deplacement()

################# JEU NORMAL ########################
def init_canvas_jeu_normal(): 
    global x0, x1, y0, y1, balle, joueur_1, joueur_2
    canevas.delete(ALL)
    bouton_facile.place_forget()
    bouton_normal.place_forget()
    bouton_difficile.place_forget()
    bouton_regles.place_forget()
    bouton_quit.place_forget()
    canevas.create_line(fenetre_x // 2, 0, fenetre_x // 2, fenetre_y, fill = "white", width = 5)
    balle = canevas.create_oval(x0, y0, x1, y1, fill = "red")
    joueur_1 = canevas.create_rectangle(debut_x1, debut_y1, fin_x1, fin_y1, fill = "white")
    joueur_2 = canevas.create_rectangle(debut_x2, debut_y2, fin_x2, fin_y2, fill = "white")
    # déplacement de la raquettes
    def bas1(event):
        if canevas.coords(joueur_1)[3] < fenetre_y:
            canevas.move(joueur_1, 0, 50)
    def haut1(event):
        if canevas.coords(joueur_1)[1] > 0:
            canevas.move(joueur_1, 0, -50)
    def bas2(event):
        if canevas.coords(joueur_2)[3] < fenetre_y:
            canevas.move(joueur_2, 0, 50)
    def haut2(event):
        if canevas.coords(joueur_2)[1] > 0:
         canevas.move(joueur_2, 0, -50)
    # bind des touches pour déplacer les raquettes
    canevas.bind_all('<Down>', bas2)
    canevas.bind_all('<Up>', haut2)
    canevas.bind_all('<s>', bas1)
    canevas.bind_all('<z>', haut1)

    # Déplacement perpetuel de la balle
    def deplacement():
        global x0, y0, x1, y1, dx2, dy2
        # Variable collision balle/raquette
        x0_balle = canevas.coords(balle)[0]
        y0_balle = canevas.coords(balle)[1]
        x1_balle = canevas.coords(balle)[2]
        y1_balle = canevas.coords(balle)[3]
        x0_j2 = canevas.coords(joueur_2)[0]
        y0_j2 = canevas.coords(joueur_2)[1]
        x1_j2 = canevas.coords(joueur_2)[2]
        y1_j2 = canevas.coords(joueur_2)[3]
        x0_j1 = canevas.coords(joueur_1)[0]
        y0_j1 = canevas.coords(joueur_1)[1]
        x1_j1 = canevas.coords(joueur_1)[2]
        y1_j1 = canevas.coords(joueur_1)[3]
        # Création composants
        canevas.move(balle, dx2, dy2)
        if canevas.coords(balle)[0] > fenetre_x:
            init_canvas_gameover1()
        if canevas.coords(balle)[2] < 0 :
            init_canvas_gameover2()
        if canevas.coords(balle)[3] > fenetre_y or canevas.coords(balle)[1] < 0 :
            dy2 = -dy2
        if canevas.coords(balle)[2] > x0_j2 and y1_balle > y0_j2 and y0_balle < y1_j2 or canevas.coords(balle)[0] < x1_j1 and y1_balle > y0_j1 and y0_balle < y1_j1:
            dx2 = -dx2
        
        canevas.after(20,deplacement)
    deplacement()
############## JEU DIFFICILE #################
def init_canvas_jeu_difficile(): 
    global x0, x1, y0, y1, balle, joueur_1, joueur_2
    canevas.delete(ALL)
    bouton_facile.place_forget()
    bouton_normal.place_forget()
    bouton_difficile.place_forget()
    bouton_regles.place_forget()
    bouton_quit.place_forget()
    canevas.create_line(fenetre_x // 2, 0, fenetre_x // 2, fenetre_y, fill = "white", width = 5)
    balle = canevas.create_oval(x0, y0, x1, y1, fill = "red")
    joueur_1 = canevas.create_rectangle(debut_x1, debut_y1, fin_x1, fin_y1, fill = "white")
    joueur_2 = canevas.create_rectangle(debut_x2, debut_y2, fin_x2, fin_y2, fill = "white")
    # déplacement de la raquettes
    def bas1(event):
        if canevas.coords(joueur_1)[3] < fenetre_y:
            canevas.move(joueur_1, 0, 30)
    def haut1(event):
        if canevas.coords(joueur_1)[1] > 0:
            canevas.move(joueur_1, 0, -30)
    def bas2(event):
        if canevas.coords(joueur_2)[3] < fenetre_y:
            canevas.move(joueur_2, 0, 30)
    def haut2(event):
        if canevas.coords(joueur_2)[1] > 0:
         canevas.move(joueur_2, 0, -30)
    # bind des touches pour déplacer les raquettes
    canevas.bind_all('<Down>', bas2)
    canevas.bind_all('<Up>', haut2)
    canevas.bind_all('<s>', bas1)
    canevas.bind_all('<z>', haut1)

    # Déplacement perpetuel de la balle
    def deplacement():
        global x0, y0, x1, y1, dx3, dy3
        # Variable collision balle/raquette
        x0_balle = canevas.coords(balle)[0]
        y0_balle = canevas.coords(balle)[1]
        x1_balle = canevas.coords(balle)[2]
        y1_balle = canevas.coords(balle)[3]
        x0_j2 = canevas.coords(joueur_2)[0]
        y0_j2 = canevas.coords(joueur_2)[1]
        x1_j2 = canevas.coords(joueur_2)[2]
        y1_j2 = canevas.coords(joueur_2)[3]
        x0_j1 = canevas.coords(joueur_1)[0]
        y0_j1 = canevas.coords(joueur_1)[1]
        x1_j1 = canevas.coords(joueur_1)[2]
        y1_j1 = canevas.coords(joueur_1)[3]
        # Création composants
        canevas.move(balle, dx3, dy3)
        if canevas.coords(balle)[0] > fenetre_x:
            init_canvas_gameover1()
        if canevas.coords(balle)[2] < 0 :
            init_canvas_gameover2()
        if canevas.coords(balle)[3] > fenetre_y or canevas.coords(balle)[1] < 0 :
            dy3 = -dy3
        if canevas.coords(balle)[2] > x0_j2 and y1_balle > y0_j2 and y0_balle < y1_j2 or canevas.coords(balle)[0] < x1_j1 and y1_balle > y0_j1 and y0_balle < y1_j1:
            dx3 = -dx3
        
        canevas.after(20,deplacement)
    deplacement()

############### ECRAN DE GAMEOVER #############
def init_canvas_gameover1():
    canevas.delete(ALL)
    bouton_facile.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    bouton_normal.place(relx = 0.5, rely = 0.6, anchor = CENTER)
    bouton_difficile.place(relx = 0.5, rely = 0.7, anchor = CENTER)
    bouton_quit.place(relx = 0.5, rely = 0.9, anchor = CENTER)
    canevas.create_text(fenetre_x // 2, 100, fill = "red", font = ("Roboto", 75), text = "GAME OVER")
    canevas.create_text(fenetre_x // 2, 400, fill = "red", font = ("Roboto", 45), text = "Rejouer ?")
    canevas.create_text(fenetre_x // 2, 250, fill = "red", font = ("Roboto", 45), text = "Joueur 1 gagne le match")


def init_canvas_gameover2():
    canevas.delete(ALL)
    bouton_facile.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    bouton_normal.place(relx = 0.5, rely = 0.6, anchor = CENTER)
    bouton_difficile.place(relx = 0.5, rely = 0.7, anchor = CENTER)
    bouton_quit.place(relx = 0.5, rely = 0.9, anchor = CENTER)
    canevas.create_text(fenetre_x // 2, 100, fill = "red", font = ("Roboto", 75), text = "GAME OVER")
    canevas.create_text(fenetre_x // 2, 400, fill = "red", font = ("Roboto", 45), text = "Rejouer ?")
    canevas.create_text(fenetre_x // 2, 250, fill = "red", font = ("Roboto", 45), text = "Joueur 2 gagne le match")




# Création des composants
bouton_quit = Button(fenetre, text = "Quit", width = 20, height = 3, command = fenetre.destroy)
bouton_regles = Button(fenetre, text = "Regles/Controles", width = 20, height = 3, command = init_canvas_regles)
bouton_parametres = Button(fenetre, text = "Parametres", width = 20, height = 3, command = init_canvas_parametres)
bouton_facile = Button(fenetre, text = "Facile", width = 20, height = 3, command = init_canvas_jeu_facile)
bouton_normal = Button(fenetre, text = "Normal", width = 20, height = 3, command = init_canvas_jeu_normal)
bouton_difficile = Button(fenetre, text = "Difficile",  width = 20, height = 3, command = init_canvas_jeu_difficile)

# placement des composants
bouton_quit.place(relx = 0.5, rely = 0.9, anchor = CENTER)
canevas.pack()
init_canvas_menu()

# boucle infinie
fenetre.mainloop()