#By WarriorMachine (Paul.M.)
from tkinter import *

#1 Blanc
#2 Orange
#3 Jaune
#4 Rouge
#5 Bleu
#6 Vert

f_haute  = [5,5,5, # array corresponding to the upper face
            5,5,5, # tableau correspondant à la face haute
            5,5,5]

f_basse  = [6,6,6, # array corresponding to the lower face
            6,6,6, # tableau correspondant à la face basse
            6,6,6]

f_droite = [4,4,4, # array corresponding to the right face
            4,4,4, # tableau correspondant à la face droite
            4,4,4]

f_gauche = [2,2,2, # array corresponding to the left face
            2,2,2, # tableau correspondant à la face gauche
            2,2,2]

f_fond   = [3,3,3, # array corresponding to the bottom face
            3,3,3, # tableau correspondant à la face du fond
            3,3,3]

f_face   = [1,1,1, # array corresponding to the visible face
            1,1,1, # tableau correspondant à la face de face
            1,1,1]

#start of the part to create the window and manage it
# début de la partie pour créer la fenêtre et la gérer
main = Tk()
main.title("Rubix Game")
w_large, w_haut = main.winfo_screenwidth(), main.winfo_screenheight()
large = 1250
haut = 750
main.geometry("%dx%d+%d+%d" % (large, haut, round(w_large/2-large/2), round(w_haut/2-haut/2)))

backFrame = Frame(main, bg="#0c0c0c")
backFrame.place(x=0,y=0, width=large, height=haut)
rubixSize = 500
contentFrame = Frame(main, bg='gray80')
contentFrame.place(x=round(large/2-(rubixSize+100)/2),y=round(haut/2-(rubixSize+100)/2), width=rubixSize+100, height=rubixSize+100)
rubixFrame = Frame(contentFrame, bg='gray90')
rubixFrame.place(x=50,y=50, width=rubixSize, height=rubixSize)
change = Button(contentFrame, bg='gray80', command=lambda : change_face())
change.place(x=0, y=0, width=50, height=50)

def right_Button():
    button_Placer("→", 550, 25/2, 125, 500/3, 1, [lambda : move(0), lambda : move(1), lambda : move(2)])

def up_Button():
    button_Placer("↑", 125, 500/3, 25/2, 0, 0, [lambda : move(3), lambda : move(4), lambda : move(5)])

def button_Placer(text, p_x, x, p_y, y, side ,command):
    for n in range(0,3):
        key = Button(contentFrame, text=text, bg='gray20', fg='white', border=0, command=command[n])
        if side:
            key.place(x=p_x+x,y=p_y+y*n, width=25, height=25)
        else:
            key.place(x=p_x+x*n,y=p_y+y, width=25, height=25)

def color(n):
    switcher={1:'white',2:'orange',3:'yellow',4:'red',5:'blue',6:'green'}
    return switcher.get(n)
#end of the part to create the window and manage it
#fin de la partie pour créer la fenêtre et la gérer

#display the rendering of the rubik's cube according to the array
#affiche le rendu du rubikscube en fonction des tableaux
def render():
    for i in range(0,9):
        cube_NN = Frame(rubixFrame, bg=color(f_face[i]))
        if i <= 2:
            cube_NN.place(x=500/3*i,y=0, width=500/3, height=500/3)
        elif i <= 5:
            cube_NN.place(x=500/3*(i-3),y=500/3, width=500/3, height=500/3)
        elif i <= 9:
            cube_NN.place(x=500/3*(i-6),y=500/3*2, width=500/3, height=500/3)

#management of array following the rotation chosen
#gestion des tableau suivant la rotaion choisis
def move(arg):
    if arg == 0:
        stock = f_face[0:3]
        f_face[0:3] = f_gauche[0:3]
        f_gauche[0:3] = f_fond[0:3]
        f_fond[0:3] = f_droite[0:3]
        f_droite[0:3] = stock
        stock_fh = f_haute[0:9]
        f_haute[0:1] = stock_fh[2:3]
        f_haute[1:2] = stock_fh[5:6]
        f_haute[2:3] = stock_fh[8:9]
        f_haute[3:4] = stock_fh[1:2]
        f_haute[4:5] = stock_fh[4:5]
        f_haute[5:6] = stock_fh[7:8]
        f_haute[6:7] = stock_fh[0:1]
        f_haute[7:8] = stock_fh[3:4]
        f_haute[8:9] = stock_fh[6:7]
    if arg == 1:
        stock = f_face[3:6]
        f_face[3:6] = f_gauche[3:6]
        f_gauche[3:6] = f_fond[3:6]
        f_fond[3:6] = f_droite[3:6]
        f_droite[3:6] = stock
    if arg == 2:
        stock = f_face[6:9]
        f_face[6:9] = f_gauche[6:9]
        f_gauche[6:9] = f_fond[6:9]
        f_fond[6:9] = f_droite[6:9]
        f_droite[6:9] = stock
        stock_fh = f_basse[0:9]
        f_basse[0:1] = stock_fh[2:3]
        f_basse[1:2] = stock_fh[5:6]
        f_basse[2:3] = stock_fh[8:9]
        f_basse[3:4] = stock_fh[1:2]
        f_basse[4:5] = stock_fh[4:5]
        f_basse[5:6] = stock_fh[7:8]
        f_basse[6:7] = stock_fh[0:1]
        f_basse[7:8] = stock_fh[3:4]
        f_basse[8:9] = stock_fh[6:7]
    if arg == 3:
        stock = None
        var1, var2, var3 = f_face[0:1], f_face[3:4], f_face[6:7]
        f_face[0:1] = f_basse[0:1]
        f_face[3:4] = f_basse[3:4]
        f_face[6:7] = f_basse[6:7]
        f_basse[0:1] = f_fond[0:1]
        f_basse[3:4] = f_fond[3:4]
        f_basse[6:7] = f_fond[6:7]
        f_fond[0:1] = f_haute[0:1]
        f_fond[3:4] = f_haute[3:4]
        f_fond[6:7] = f_haute[6:7]
        f_haute[0:1] = var1
        f_haute[3:4] = var2
        f_haute[6:7] = var3
        stock_fg = f_gauche[0:9]
        f_gauche[0:1] = stock_fg[2:3]
        f_gauche[1:2] = stock_fg[5:6]
        f_gauche[2:3] = stock_fg[8:9]
        f_gauche[3:4] = stock_fg[1:2]
        f_gauche[4:5] = stock_fg[4:5]
        f_gauche[5:6] = stock_fg[7:8]
        f_gauche[6:7] = stock_fg[0:1]
        f_gauche[7:8] = stock_fg[3:4]
        f_gauche[8:9] = stock_fg[6:7]
    if arg == 4:
        stock = None
        var1, var2, var3 = f_face[1:2], f_face[4:5], f_face[7:8]
        f_face[1:2] = f_basse[1:2]
        f_face[4:5] = f_basse[4:5]
        f_face[7:8] = f_basse[7:8]
        f_basse[1:2] = f_fond[1:2]
        f_basse[4:5] = f_fond[4:5]
        f_basse[7:8] = f_fond[7:8]
        f_fond[1:2] = f_haute[1:2]
        f_fond[4:5] = f_haute[4:5]
        f_fond[7:8] = f_haute[7:8]
        f_haute[1:2] = var1
        f_haute[4:5] = var2
        f_haute[7:8] = var3
    if arg == 5:
        stock = None
        var1, var2, var3 = f_face[2:3], f_face[5:6], f_face[8:9]
        f_face[2:3] = f_basse[2:3]
        f_face[5:6] = f_basse[5:6]
        f_face[8:9] = f_basse[8:9]
        f_basse[2:3] = f_fond[2:3]
        f_basse[5:6] = f_fond[5:6]
        f_basse[8:9] = f_fond[8:9]
        f_fond[2:3] = f_haute[2:3]
        f_fond[5:6] = f_haute[5:6]
        f_fond[8:9] = f_haute[8:9]
        f_haute[2:3] = var1
        f_haute[5:6] = var2
        f_haute[8:9] = var3
        stock_fg = f_droite[0:9]
        f_droite[0:1] = stock_fg[6:7]
        f_droite[1:2] = stock_fg[3:4]
        f_droite[2:3] = stock_fg[0:1]
        f_droite[3:4] = stock_fg[7:8]
        f_droite[4:5] = stock_fg[4:5]
        f_droite[5:6] = stock_fg[1:2]
        f_droite[6:7] = stock_fg[8:9]
        f_droite[7:8] = stock_fg[5:6]
        f_droite[8:9] = stock_fg[2:3]

    render()

def change_face():
    move(0)
    move(1)
    move(2)
    move(3)
    move(4)
    move(5)

right_Button()
up_Button()
render()

main.mainloop()
