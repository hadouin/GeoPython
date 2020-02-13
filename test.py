<<<<<<< HEAD
from tkinter import *

fen = Tk()       # Objet stocké dans la variable "fen"
##----- Zones de texte -----##
Titre = Label(fen, text='Ceci n\'est pas un morpion')
Titre.grid(row=0, column=0, columnspan=2)
##----- Boutons -----##
bouton_recommencer = Button(fen, text='recommencer',command=fen.destroy)
bouton_recommencer.grid(row = 2, column = 0, padx = 3, pady = 3)

bouton_quitter = Button(fen, text='Quitter',command=fen.destroy)
bouton_quitter.grid(row = 2, column = 1, padx = 3, pady = 3)
##----- Canevas -----##
dessin = Canvas(fen,bg="white", width=303, height=303)
dessin.grid(row = 1, column = 0, columnspan=2)

##-----Programme principal-----##
fen.mainloop()     # Boucle d'attente des événements
=======
ok ta mère
>>>>>>> f1ed4cf4b3ac65c945ff557e2dec41c9cfbf29f9
