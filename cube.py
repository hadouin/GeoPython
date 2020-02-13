##----- Importation des Modules -----##
from tkinter import *

##-----Définition des Variables globales-----##

##----- Définition des Classes -----##
class sol: 
    def __init__(self):
        self.y = 550
        self.color = 'black'
    def draw(self):
        dessin.create_line(0, self.y, 1100, self.y, width = 4)

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
dessin.create_rectangle(515, 400, 565, 450, fill='grey', width='5')  

Sol = sol()
Sol.draw()

root.mainloop()      