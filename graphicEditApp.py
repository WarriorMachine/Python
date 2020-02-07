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

data_filename = dict()

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

def saveasFichier():
    filedialog.asksaveasfilename(initialdir = "/",title = "Sauvegarder un fichier", initialfile="fichier", defaultextension=".txt", filetypes = (("Texte brute", "*.txt *.gitignore"),("Batch", "*.bat *.cmd"),("C", "*.c"),("C++", "*.cpp *.cc *.cxx *.hpp *.hh *.hxx *.h *.ino *.inl *.ipp"),("C#", "*.cs *.csx *.cake"),("Clojure", "*.clj *.cljs *.cljc *.cljx *.clojure *.edn"),("CoffeeScript", "*.coffee *.cson"),("CSS", "*.css"),("Diff", "*.patch *.diff *.rej"),("Dockerfile", "*.dockerfile"),("F#", "*.fs *.fsi *.fsx *.fsscript"),("Go", "*.go"),("Groovy", "*.groovy *.gvy *.gradle"),("Handlebars", "*.handlebars *.hbs *.hjs"),("HLSL", "*.hlsl *.hlsi *.fx *.fxh *.vsh *.psh *.cginc *.compute"),("HTML", "*.html *.htm *.shtml *.xhtml *.mdoc *.jsp *.asp *.aspx *.jshtm *.volt"),("Ini", "*.ini"),("Java", "*.java *.jav"),("JavaScript", "*.js"),("JavaScript React", "*.jsx"),("JSON", "*.json *.bowerrc *.jshintrc *.jscsrc *.eslintrc *.webmanifest *.js*.map *.css*.map"),("Less", "*.less"),("Lua", "*.lua"),("Log", "*.log *.log*.?"),("Makefile", "*.mk"),("Markdown", "*.md *.mkd *.mdwn *.mdown *.markdown *.markdn *.mdtxt *.mdtext *.workbook"),("Objective-C", "*.m"),("Objective-C++", "*.mm"),("Perl", "*.pl *.pm *.pod *.t *.PL *.psgi"),("Perl 6", "*.p6 *.pl6 *.pm6 *.nqp"),("PHP", "*.php *.php4 *.php5 *.phtml *.ctp"),("PowerShell", "*.ps1 *.psm1 *.psd1 *.pssc *.psrc"),("Properties", "*.properties *.cfg *.conf *.desktop *.directory"),("Pug", "*.jade *.pug"),("Python", "*.py *.pyw *.rpy *.cpy *.gyp *.gypi *.snakefile *.smk *.pyi"),("R", "*.r *.rhistory *.rprofile *.rt"),("Razor", "*.cshtml"),("Ruby", "*.rb *.rbx *.rjs *.gemspec *.rake *.ru *.erb"),("Rust", "*.rs"),("SCSS", "*.scss"),("ShaderLab", "*.shader"),("Shell Script", "*.sh *.bash *.bash *.bashrc *.bash_aliases *.bash_profile *.bash_login *.ebuild *.install *.profile *.bash_logout"),("SQL", "*.sql *.dsql"),("Swift", "*.swift"),("TypeScript", "*.ts"),("TypeScript React", "*.tsx"),("Visual Basic", "*.vb *.brs *.vbs *.bas"),("XML", "*.xsl *.xslt"),("YAML", "*.yml *.eyaml *.eyml *.yaml"),("Sans extention", "*.")))

morePageCount = 1
def moreFichier():
    global morePageCount
    if morePageCount == 1:
        This = Frame(main, bd=0, relief=FLAT, cursor="tcross")
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
        fileText.place(x=290,y=30,width=large-200,height=haut-30)
        stockListbox = StringVar()
        stockListbox = listpara.get(listpara.curselection())
        def detect_key(event):
            print('key : '+str(event.char))
            try:
                numberline.place_forget()
            except:
                pass
            n = 0
            textin = fileText.get(1.0, 'end')
            cache = open(str(repertoire)+"/cacheGraphicTextWidth.wt", "w")
            cache.write(str(textin))
            cache.close()
            texton = open(str(repertoire)+"/cacheGraphicTextWidth.wt", "r")
            while texton.readline():
                 n = n+1
            numberline = Listbox(backFrame, activestyle='none', bd = 0, borderwidth=0, bg = '#111111',highlightthickness=0, fg = 'gray50', selectforeground='gray50', selectbackground='#111111', cursor="cross", font=('Consolas', 10, 'normal'), exportselection=0, selectmode=SINGLE)
            numberline.place(x=250, y=32, width=35, height=haut-28)
            for i in range(1,n+1):
                if i >= 0 and i < 10:
                    n = "   "+str(i)
                elif i >= 10 and i < 99:
                    n = "  "+str(i)
                elif i >= 100 and i < 999:
                    n = " "+str(i)
                elif i >= 1000 and i < 9999:
                    n = ""+str(i)
                numberline.insert("end", str(n))
        if stockListbox[-4:] == ".png" or stockListbox[-4:] == ".PNG" or stockListbox[-4:] == ".jpg" or stockListbox[-4:] == ".JPG" or stockListbox[-5:] == ".jpeg" or stockListbox[-5:] == ".JPEG" or stockListbox[-4:] == ".gif":
            fileText.insert(END," Cette image n'est pas disponnible ")
            numb = len(stockListbox)
            fileText.tag_add("error1", "1.0", "1.100000")
            fileText.tag_config("error1", background="crimson", foreground="white")
            hideFrame = Frame(backFrame, bg='#0c0c0c')
            hideFrame.place(x=250, y=32, width=35, height=haut-28)
        else:
            try:
                cacheread = data_filename['filename']
                finalcacheread = str(cacheread)+"/"+str(stockListbox)
                finalfileread = open(finalcacheread, encoding='UTF8', errors='ignore').read()
                fileText.insert(END,finalfileread)
                hideFrame = Frame(backFrame, bg='#0c0c0c')
                hideFrame.place(x=250, y=32, width=35, height=haut-28)
                fd = open(finalcacheread, 'r')
                n = 0
                while fd.readline():
                    n += 1
                numberline = Listbox(backFrame, activestyle='none', bd = 0, borderwidth=0, bg = '#111111',highlightthickness=0, fg = 'gray50', selectforeground='gray50', selectbackground='#111111', cursor="cross", font=('Consolas', 10, 'normal'), exportselection=0, selectmode=SINGLE)
                numberline.place(x=250, y=32, width=35, height=haut-28)
                for i in range(1,n+1):
                    if i >= 0 and i < 10:
                        n = "   "+str(i)
                    elif i >= 10 and i < 99:
                        n = "  "+str(i)
                    elif i >= 100 and i < 999:
                        n = " "+str(i)
                    elif i >= 1000 and i < 9999:
                        n = ""+str(i)
                    numberline.insert("end", str(n))
            except ALL:
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
                hideFrame = Frame(backFrame, bg='#0c0c0c')
                hideFrame.place(x=250, y=32, width=35, height=haut-28)
        fileText.bind('<KeyPress>', detect_key)
    filename =  filedialog.askdirectory(initialdir = "/",title = "Ouvrir un dossier")
    thedirBRUT = os.listdir(filename)
    data_filename['filename'] = str(filename)
    numberfile = len(thedirBRUT)
    cycler = cycle(thedirBRUT)
    framelistpara = Frame(backFrameFolder, bg = '#0f0f0f')
    framelistpara.place(x=0, y=30, width=200, height=haut-60)
    listpara = Listbox(framelistpara, bd = 0, borderwidth=0, bg = '#0f0f0f',highlightthickness=0, fg = 'gray50', selectforeground='crimson', selectbackground='#111111', cursor="cross", font=('Gotham', 10, 'normal'), exportselection=0, selectmode=SINGLE)
    listpara.place(x=0, y=0, width=250, height=haut-60)
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
augmenter = Button(backFrameBar, text="☐", relief = FLAT, bd = 0, bg = '#111111', fg = 'gray80', cursor="cross", activebackground='#634481')
augmenter.place(x=large-100, y=0, width=50, height=30)
fermer = Button(backFrameBar, text="✕", relief = FLAT, bd = 0, bg = '#111111', fg = 'gray80', cursor="cross", command=CloseAll, activebackground='crimson')
fermer.place(x=large-50, y=0, width=50, height=30)
points = Button(backFrameBar, text="•••", relief = FLAT, bd = 0, bg = '#111111', fg = 'gray80', cursor="cross", activebackground='#111111', font=('Gotham', 11, 'bold'))
points.place(x=0, y=0, width=25, height=30)
points = Button(backFrameBar, text="Fichier", relief = FLAT, bd = 0, bg = '#111111', fg = 'gray80', cursor="cross", activebackground='#111111', font=('Gotham', 9, 'normal'), command=file)
points.place(x=30, y=0, width=50, height=30)
points = Button(backFrameBar, text="Edition", relief = FLAT, bd = 0, bg = '#111111', fg = 'gray80', cursor="cross", activebackground='#111111', font=('Gotham', 9, 'normal'), command=saveasFichier)
points.place(x=80, y=0, width=50, height=30)
points = Button(backFrameBar, text="Affichage", relief = FLAT, bd = 0, bg = '#111111', fg = 'gray80', cursor="cross", activebackground='#111111', font=('Gotham', 9, 'normal'))
points.place(x=130, y=0, width=70, height=30)
points = Button(backFrameBar, text="Aide", relief = FLAT, bd = 0, bg = '#111111', fg = 'gray80', cursor="cross", activebackground='#111111', font=('Gotham', 9, 'normal'))
points.place(x=200, y=0, width=30, height=30)

backFrameFolder = Frame(main, bg='#0f0f0f')
backFrameFolder.place(x=0,y=30,width=250,height=haut)
backFrameFoldr = Frame(main, bg='#111111')
backFrameFoldr.place(x=250,y=30,width=1,height=haut)
choose = Button(backFrameFolder, text='+ Choisir un dossier', anchor='center', bg ='#0f0f0f', fg='gray90', relief=FLAT, bd = 0, cursor="cross", activebackground='mediumseagreen', font=('Gotham', 9, 'normal'),command=file)
choose.place(x=0, y=2, width=250, height=22)

main.mainloop()
