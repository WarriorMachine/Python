# coding: utf8

from tkinter import *
from tkinter import filedialog
from itertools import cycle
import os
import time

repertoire = "E:/"

main = Tk()
main.title("GraphicDir")
try:
    main.iconbitmap("icon.ico")
except:
    print("L'icone de la fenêtre principale n'a pas été chargée")
main.overrideredirect(1)
main.resizable(width=False, height=False)
large = main.winfo_screenwidth()
haut = main.winfo_screenheight()
sL = large/2-(1360/2)
sH = haut/2-(768/2)
screen_resolutionMain = str(round(large))+'x'+str(round(haut))+'+'+str(0)+'+'+str(0)
main.geometry(screen_resolutionMain)

def CloseAll():
    main.destroy()
    sys.exit()

counterfen = 1
def OverRider():
    global counterfen
    if counterfen == 1:
        main.overrideredirect(0)
        counterfen = 0
    else:
        main.overrideredirect(1)
        counterfen = 1

def reduct(): 
    main.overrideredirect(0)
    main.state('iconic')
    while  main.state() == 'iconic':
        main.update()
        time.sleep(0.1)
    main.overrideredirect(1)

morePageCount = 1
def moreFichier():
    global morePageCount
    if morePageCount == 1:
        This = Frame(main, bd=0, relief=FLAT, bg='#0b0b0b', cursor="tcross")
        This.place(x=35, y=30, width=100, height=20)
        newButton = Button(This, text="Nouveau fichier", relief = FLAT, bd = 0, bg = '#0b0b0b', fg = 'gray80', cursor="cross", activebackground='mediumseagreen', font=('Gotham', 9, 'normal'))
        newButton.place(x=0, y=0, width=100, height=20)
        morePageCount = morePageCount-1
    elif morePageCount == 0:
        This.place_forget()
        morePageCount = morePageCount+1

def file():
    def clicListbox(ListBox):
        fileText = Text(backFrame,background="#0c0c0c", maxundo=-1, wrap='none',foreground="gray90",insertbackground='crimson',highlightthickness=0,borderwidth=0,selectbackground='#222222')
        fileText.place(x=200,y=30,width=large-200,height=haut-30)
        stockListbox = StringVar()
        stockListbox = listpara.get(listpara.curselection())
        if stockListbox[-4:] == ".png" or stockListbox[-4:] == ".PNG" or stockListbox[-4:] == ".jpg" or stockListbox[-4:] == ".JPG":
            fileText.insert(END," Cette image est indisponnible ")
            numb = len(stockListbox)
            fileText.tag_add("error1", "1.0", "1.10000")
            fileText.tag_config("error1", background="crimson", foreground="white")
        else:
            try:
                cache = open(str(repertoire)+"/cacheGraphicDir.wt", "r")
                cacheread = cache.read()
                finalcacheread = str(cacheread)+"/"+str(stockListbox)
                finalfileread = open(finalcacheread, encoding='UTF8', errors='ignore').read()
                fileText.insert(END,finalfileread)
                cache.close()
            except:
                fileText.insert(END," Erreur "+str(stockListbox)+" ne peu être lu ")
                numb = len(stockListbox)
                fileText.tag_add("error1", "1.0", "1.8")
                fileText.tag_config("error1", background="crimson", foreground="white")
                var1 = '1.'+str(round(7+numb+1))
                fileText.tag_add("error2", "1.8", var1)
                fileText.tag_config("error2", background="crimson", foreground="black")
                var2 = '1.'+str(round(7+numb+1))
                fileText.tag_add("error3", var2, "1.100000")
                fileText.tag_config("error3", background="crimson", foreground="white")

    filename =  filedialog.askdirectory(initialdir = "/",title = "Ouvrir un dossier")
    thedirBRUT = os.listdir(filename)
    cache = open(str(repertoire)+"/cacheGraphicDir.wt", "w")
    cache.write(str(filename))
    cache.close()
    numberfile = len(thedirBRUT)
    cycler = cycle(thedirBRUT)
    framelistpara = Frame(backFrameFolder, bg = '#0f0f0f')
    framelistpara.place(x=0, y=30, width=200, height=haut-60)
    listpara = Listbox(framelistpara, bd = 0, borderwidth=0, bg = '#0f0f0f',highlightthickness=0, fg = 'gray50', selectforeground='crimson', selectbackground='#111111', cursor="cross", font=('Gotham', 10, 'normal'), exportselection=0, selectmode=SINGLE)
    listpara.place(x=0, y=0, width=200, height=haut-60)
    for i in range(0, numberfile):
        current_dir = next(cycler)
        listpara.insert(i, str(current_dir))
    listpara.bind('<ButtonRelease-1>',clicListbox)
    scrollbarList = Scrollbar(framelistpara)
    scrollbarList.config(command = listpara.yview)

backFrame = Frame(main, bg='#0c0c0c')
backFrame.place(x=0,y=0,width=large,height=haut)

backFrameBar = Frame(main, bg='#111111')
backFrameBar.place(x=0,y=0,width=large,height=30)
reduire = Button(backFrameBar, text="━", relief = FLAT, bd = 0, bg = '#111111', fg = 'gray80', cursor="cross", activebackground='#534692', command=reduct)
reduire.place(x=large-150, y=0, width=50, height=30)
augmenter = Button(backFrameBar, text="☐", relief = FLAT, bd = 0, bg = '#111111', fg = 'gray80', cursor="cross", activebackground='#634481', command=OverRider)
augmenter.place(x=large-100, y=0, width=50, height=30)
fermer = Button(backFrameBar, text="✕", relief = FLAT, bd = 0, bg = '#111111', fg = 'gray80', cursor="cross", command=CloseAll, activebackground='crimson')
fermer.place(x=large-50, y=0, width=50, height=30)
points = Button(backFrameBar, text="•••", relief = FLAT, bd = 0, bg = '#111111', fg = 'gray80', cursor="cross", activebackground='#111111', font=('Gotham', 11, 'bold'))
points.place(x=0, y=0, width=25, height=30)
points = Button(backFrameBar, text="Fichier", relief = FLAT, bd = 0, bg = '#111111', fg = 'gray80', cursor="cross", activebackground='#111111', font=('Gotham', 9, 'normal'), command=file)
points.place(x=30, y=0, width=50, height=30)
points = Button(backFrameBar, text="Edition", relief = FLAT, bd = 0, bg = '#111111', fg = 'gray80', cursor="cross", activebackground='#111111', font=('Gotham', 9, 'normal'))
points.place(x=80, y=0, width=50, height=30)
points = Button(backFrameBar, text="Affichage", relief = FLAT, bd = 0, bg = '#111111', fg = 'gray80', cursor="cross", activebackground='#111111', font=('Gotham', 9, 'normal'))
points.place(x=130, y=0, width=70, height=30)
points = Button(backFrameBar, text="Aide", relief = FLAT, bd = 0, bg = '#111111', fg = 'gray80', cursor="cross", activebackground='#111111', font=('Gotham', 9, 'normal'))
points.place(x=200, y=0, width=30, height=30)

backFrameFolder = Frame(main, bg='#0f0f0f')
backFrameFolder.place(x=0,y=30,width=200,height=haut)
choose = Button(backFrameFolder, text='+ Choisir un dossier', anchor='center', bg ='#0f0f0f', fg='gray90', relief=FLAT, bd = 0, cursor="cross", activebackground='mediumseagreen', font=('Gotham', 9, 'normal'),command=file)
choose.place(x=0, y=2, width=200, height=22)

main.mainloop()
