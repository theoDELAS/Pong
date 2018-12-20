from tkinter import *

#Création de la fenetre principale
fenetre = Tk()
fenetre.title('Pong Game')

#info dimensions ecran et fenetre
ecran_x = fenetre.winfo_screenwidth()
ecran_y = fenetre.winfo_screenheight()
fenetre_x = 1080
fenetre_y = 720

#calcul pour faire spawn fenetre au centre de l'ecran
pos_x = (ecran_x // 2) - (fenetre_x //2)
pos_y = (ecran_y // 2) - (fenetre_y //2)

#Position de la fenetre au centre
geo = f'{fenetre_x}x{fenetre_y}+{pos_x}+{pos_y}'
fenetre.geometry(geo)

# Création du canevas
canevas = Canvas(fenetre, width = fenetre_x, height = fenetre_y -60, bg = "black")

# Coordonnées de la balle et vitesse
x0 = fenetre_x // 2
y0 = fenetre_y // 2
dx = + 5
dy = + 5

#variable relatives aux raquettes
debut_x1 = 0
debut_x2 = 0
#variable relatives à la balle
y1 = 0
y1 = 0

# Création composants
balle = canevas.create_oval(x0, y0, x0 + 20, y0 + 20, width = 2, fill = "red")
joueur_1 = canevas.create_rectangle(debut_x1 + 5,50,debut_x1 + 20, 175, fill = "white")
joueur_2 = canevas.create_rectangle(fenetre_x - 5, 150, fenetre_x -20, 275, fill = "white")

#def déplacement de la raquettes
def bas1(event):
    canevas.move(joueur_1,0,15)
def haut1(event):
    canevas.move(joueur_1,0,-15)
def bas2(event):
    canevas.move(joueur_2,0,15)
def haut2(event):
    canevas.move(joueur_2,0,-15)

canevas.bind_all('<Down>', bas2)
canevas.bind_all('<Up>', haut2)
canevas.bind_all('<s>', bas1)
canevas.bind_all('<z>', haut1)
# Déplacement perpetuel
def deplacement():
    global x0, y0, dx, dy

    x0 = x0 + dx
    y0 = y0 + dy

    canevas.coords(balle, x0, y0, x0 + 20, y0 + 20)

    if x0 < 0 or x0 > fenetre_x - 20:
        dx = -dx
    if y0 < 0 or y0 > fenetre_y - 80:
        dy = -dy

    canevas.after(20,deplacement)

    return

def action_deplacer():
    deplacement()
    return

# Création des bouttons
boutton_quit = Button(fenetre, text = "Quit", command = fenetre.destroy)
boutton_deplacement = Button(fenetre, text = "Play?", command = action_deplacer)

#placement des composants
boutton_deplacement.pack()
boutton_quit.pack()
canevas.pack()

#boucle infinie
fenetre.mainloop()