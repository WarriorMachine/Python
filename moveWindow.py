from tkinter import *
import time
import win32api

main = Tk()
main.overrideredirect(1)

class Window_R():
    def __init__(self, width=1360, height= 768, princippage=main, resizebarpage=main, sizebar=3, bgbar='white', bgcornerbar='gray99'):
        maskechelle1 = Frame(resizebarpage, bd=0, bg=bgbar, cursor="size_ns")
        maskechelle1.place(x=0, y=0, width=width, height=sizebar)
        while 1:
            mouseEvent = win32api.GetKeyState(0x01) #etat du clique gauche
            x = princippage.winfo_rootx() #x = sL
            y = princippage.winfo_rooty() #y = sH
            mouseX = princippage.winfo_pointerx()
            mouseY = princippage.winfo_pointery()
            print(str(x)+" "+str(y)+" "+str(mouseX)+" "+str(mouseY))
            time.sleep(0.01)
            if mouseY>=y and mouseY<=y+sizebar-1 and mouseX>=x and mouseX<=x+width:
                if mouseEvent == -128 or mouseEvent == -127:
                    depMouseX = princippage.winfo_pointerx()
                    while 1:
                        mouseX = princippage.winfo_pointerx()
                        mouseY = princippage.winfo_pointery()
                        newdim = str(width)+"x"+str(height)+"+"+str()+"+"+str(mouseY)
                        main.geometry(newdim)
                        main.update()
                        mouseEvent = win32api.GetKeyState(0x01)
                        if mouseEvent == -127 or mouseEvent == -128:
                            pass
                        else:
                            break
            else:
                pass
            princippage.update()


ss=1440
st=700
main.geometry(str(ss)+"x"+str(st)+"+"+str(100)+"+"+str(220))

Window_R(princippage=main,sizebar=10,height=st,width=ss, bgbar='cyan', bgcornerbar='blue')

main.mainloop()
