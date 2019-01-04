from tkinter import *

#Création de la fenetre principale
fenetre = Tk()
fenetre.title('Pong Game')

#info dimensions ecran et fenetre
ecran_x = fenetre.winfo_screenwidth()
ecran_y = fenetre.winfo_screenheight()
fenetre_x = ecran_x - 5
fenetre_y = ecran_y - 100

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

# vitesse de la balle
dx = IntVar()
dy = 5

# variables relatives aux raquettes
debut_x1 = 10
fin_x1 = 25
debut_y1 = 400
fin_y1 = 525
debut_x2 = fenetre_x - 25
fin_x2 = debut_x2 + 15
debut_y2 = 400
fin_y2 = 525

def init_canvas_menu():
    canevas.delete(ALL)
    canevas.create_text(fenetre_x // 2, 200, fill = "white", font = ("Roboto", 75), text = "MENU PRINCIPAL")
    bouton_parametres.grid(row = 1, column = 4)

def init_canvas_parametres():
    canevas.delete(ALL)
    bouton_parametres.destroy()
    canevas.create_text(fenetre_x // 2, 200, fill = "white", font = ("Roboto", 75), text = "PARAMETRES")
    bouton_jouer.grid(row = 1, column = 5)
    vitesse_spin.grid(row = 1, column = 2)

# Création du canevas de jeu
def init_canvas_jeu(): 
    canevas.delete(ALL)
    bouton_menu.grid(row = 1, column = 0)
    canevas.create_line(fenetre_x // 2, 0, fenetre_x // 2, fenetre_y, fill = "white", width = 5)

    global x0, x1, y0, y1
    # Création composants
    balle = canevas.create_oval(x0, y0, x1, y1, fill = "red")
    joueur_1 = canevas.create_rectangle(debut_x1, debut_y1, fin_x1, fin_y1, fill = "white")
    joueur_2 = canevas.create_rectangle(debut_x2, debut_y2, fin_x2, fin_y2, fill = "white")
    # déplacement de la raquettes
    def bas1(event):
        canevas.move(joueur_1, 0, 50)
    def haut1(event):
        canevas.move(joueur_1, 0, -50)
    def bas2(event):
        canevas.move(joueur_2, 0, 50)
    def haut2(event):
        canevas.move(joueur_2, 0, -50)
    # bind des touches pour déplacer les raquettes
    canevas.bind_all('<Down>', bas2)
    canevas.bind_all('<Up>', haut2)
    canevas.bind_all('<s>', bas1)
    canevas.bind_all('<z>', haut1)

    # Déplacement perpetuel de la balle
    def deplacement():
        global x0, y0, x1, y1, dx, dy

        pts_j1 = 0
        pts_j2 = 0
        vitesse_x = int(dx.get())
        canevas.move(balle, vitesse_x, dy)
        if canevas.coords(balle)[0] > fenetre_x or canevas.coords(balle)[2] < 0 :
            canevas.delete('pts')
            init_canvas_jeu()
            pts_j1 += 1
            pts = canevas.create_text(300, 300, fill = "white", font = ("Roboto", 15), text = "Points :"+ str(pts_j1))
        if canevas.coords(balle)[3] > fenetre_y or canevas.coords(balle)[1] < 0 :
            dy = -dy
        if canevas.coords(balle)[2] > canevas.coords(joueur_2)[0] and canevas.coords(balle)[3] > canevas.coords(joueur_2)[1] and canevas.coords(balle)[1] < canevas.coords(joueur_2)[3] or canevas.coords(balle)[0] < canevas.coords(joueur_1)[2] and canevas.coords(balle)[3] > canevas.coords(joueur_1)[1] and canevas.coords(balle)[1] < canevas.coords(joueur_1)[3]:
            vitesse_x = -1 * dx
        
        canevas.after(20,deplacement)
    deplacement()

# Ecran de fin
def init_canvas_gameover():
    canevas.delete(ALL)
    canevas.create_text(fenetre_x // 2, 300, fill = "red", font = ("Roboto", 75), text = "GAME OVER")



# Création des composants
boutton_quit = Button(fenetre, text = "Quit", command = fenetre.destroy)
bouton_menu = Button(fenetre, text = "Menu", command = init_canvas_menu)
bouton_jouer = Button(fenetre, text = "Play", command = init_canvas_jeu)
bouton_parametres = Button(fenetre, text = "Parametres", command = init_canvas_parametres)
vitesse_spin = Spinbox(fenetre, from_ = 1, to = 10, width = 4, textvariable = dx)

# placement des composants
boutton_quit.grid(row = 1, column = 9)
canevas.grid(row = 0, column = 0, columnspan = 10)
init_canvas_menu()

# boucle infinie
fenetre.mainloop()