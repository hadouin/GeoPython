##----- Importation des Modules -----##
from tkinter import *

##-----Définition des Variables globales-----##
G = 9.81
##----- Définition des Classes -----##
class sol: 
    def __init__(self):
        self.y = 550
        self.color = 'black'
    def draw(self):
        dessin.create_line(0, self.y, 1100, self.y, width = 4)

class player:
    def __init__(self):
        self.y = 550
        self.x = 200
        self.vy = 0
        self.width = 5
    def draw(self):
        dessin.create_rectangle(self.x, self.y - self.width, self.x + 50, self.y - 50 - self.width, fill='grey', width=self.width)
    def test(self):
        if self.x + 50 <= Kube:
            pass
##----- Définition des Fonctions -----##
def quitter():
    root.destroy()

##----- Création de la fenêtre -----##
root = Tk()
root.title('Géopython')
root.iconbitmap('images.ico')

##----- Création des boutons -----##
bouton_quitter = Button(root, text='quitter',command=quitter, width=10)
bouton_quitter.grid(row=1,column=1)

##----- Création du canevas -----##
dessin=Canvas(root, bg='white', width=1080, height=720)
dessin.grid(row = 0, column = 0, columnspan = 3, padx=5, pady=5)

##----- Programme principal -----##
Cube = player()
Cube.draw()

Sol = sol()
Sol.draw()

Kube = dessin.create_rectangle(100,100,150,150)
def bouger():
    dessin.move(Kube,5,0)
    root.after(60,bouger)
bouger()
root.mainloop()      