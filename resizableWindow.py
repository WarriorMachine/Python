from tkinter import *
import time
import os
import win32api

main = Tk()
main.overrideredirect(1)
main['bg']='crimson'

class Window_R():
    def __init__(self, width=1360, height= 768, princippage=main, resizebarpage=main, sizebar=3, bgbar='white', bgcornerbar='gray99'):
        maskechelle1 = Frame(resizebarpage, bd=0, bg=bgbar, cursor="size_ns")
        maskechelle1.place(x=0, y=0, width=width, height=sizebar)
        maskechelle2 = Frame(resizebarpage, bd=0, bg=bgbar, cursor="size_we")
        maskechelle2.place(x=0, y=0, width=sizebar, height=height)
        maskechelle3 = Frame(resizebarpage, bd=0, bg=bgbar, cursor="size_ns")
        maskechelle3.place(x=0, y=height-sizebar, width=width, height=sizebar)
        maskechelle4 = Frame(resizebarpage, bd=0, bg=bgbar, cursor="size_we")
        maskechelle4.place(x=width-sizebar, y=0, width=sizebar, height=height)
        maskechelle5 = Frame(resizebarpage, bd=0, bg=bgcornerbar, cursor="size_nw_se")
        maskechelle5.place(x=0, y=0, width=sizebar+1, height=sizebar+1)
        maskechelle6 = Frame(resizebarpage, bd=0, bg=bgcornerbar, cursor="size_ne_sw")
        maskechelle6.place(x=width-(sizebar+1), y=0, width=(sizebar+1), height=sizebar+1)
        maskechelle7 = Frame(resizebarpage, bd=0, bg=bgcornerbar, cursor="size_ne_sw")
        maskechelle7.place(x=0, y=height-(sizebar+1), width=(sizebar+1), height=sizebar+1)
        maskechelle8 = Frame(resizebarpage, bd=0, bg=bgcornerbar, cursor="size_nw_se")
        maskechelle8.place(x=width-(sizebar+1), y=height-(sizebar+1), width=sizebar+1, height=sizebar+1)
        while 1:
            mouseEvent = win32api.GetKeyState(0x01) #etat du clique gauche
            x = princippage.winfo_rootx() #x = sL
            y = princippage.winfo_rooty() #y = sH
            mouseX = princippage.winfo_pointerx()
            mouseY = princippage.winfo_pointery()
            time.sleep(0.01)
            if mouseX>=x and mouseX<=x+sizebar-1 and mouseY>=y and mouseY<=y+height or mouseX>=x+width-sizebar and mouseX<=x+width and mouseY>=y and mouseY<=y+height or mouseY>=y and mouseY<=y+sizebar-1 and mouseX>=x and mouseX<=x+width or mouseY>=y+height-sizebar and mouseY<=y+height and mouseX>=x and mouseX<=x+width:
                if mouseEvent == -128 or mouseEvent == -127:
                    mouseX = princippage.winfo_pointerx()
                    mouseY = princippage.winfo_pointery()
                    x = princippage.winfo_rootx() #x = sL
                    y = princippage.winfo_rooty() #y = sH
                    if mouseX>=x and mouseX<=x+sizebar-1 and mouseY>=y and mouseY<=y+height: #Gauche
                        while 1:
                            newmouseX = princippage.winfo_pointerx()
                            newval = newmouseX - mouseX
                            if width-newval <= 1:
                                break
                            newdim = str(width-newval)+"x"+str(height)+"+"+str(x+newval)+"+"+str(y)
                            princippage.geometry(newdim)
                            mouseEvent = win32api.GetKeyState(0x01)
                            maskechelle1.place_forget()
                            maskechelle2.place_forget()
                            maskechelle3.place_forget()
                            maskechelle4.place_forget()
                            maskechelle5.place_forget()
                            maskechelle6.place_forget()
                            maskechelle7.place_forget()
                            maskechelle8.place_forget()
                            newwidth = width-newval
                            maskechelle1 = Frame(resizebarpage, bd=0, bg=bgbar, cursor="size_ns")
                            maskechelle1.place(x=0, y=0, width=newwidth, height=sizebar)
                            maskechelle2 = Frame(resizebarpage, bd=0, bg=bgbar, cursor="size_we")
                            maskechelle2.place(x=0, y=0, width=sizebar, height=height)
                            maskechelle3 = Frame(resizebarpage, bd=0, bg=bgbar, cursor="size_ns")
                            maskechelle3.place(x=0, y=height-sizebar, width=newwidth, height=sizebar)
                            maskechelle4 = Frame(resizebarpage, bd=0, bg=bgbar, cursor="size_we")
                            maskechelle4.place(x=newwidth-sizebar, y=0, width=sizebar, height=height)
                            maskechelle5 = Frame(resizebarpage, bd=0, bg=bgcornerbar, cursor="size_nw_se")
                            maskechelle5.place(x=0, y=0, width=sizebar+1, height=sizebar+1)
                            maskechelle6 = Frame(resizebarpage, bd=0, bg=bgcornerbar, cursor="size_ne_sw")
                            maskechelle6.place(x=newwidth-(sizebar+1), y=0, width=(sizebar+1), height=sizebar+1)
                            maskechelle7 = Frame(resizebarpage, bd=0, bg=bgcornerbar, cursor="size_ne_sw")
                            maskechelle7.place(x=0, y=height-(sizebar+1), width=(sizebar+1), height=sizebar+1)
                            maskechelle8 = Frame(resizebarpage, bd=0, bg=bgcornerbar, cursor="size_nw_se")
                            maskechelle8.place(x=newwidth-(sizebar+1), y=height-(sizebar+1), width=sizebar+1, height=sizebar+1)

                            princippage.update()
                            if mouseEvent == -127 or mouseEvent == -128:
                                pass
                            else:
                                break
                    elif mouseX>=x+width-sizebar and mouseX<=x+width and mouseY>=y and mouseY<=y+height: #Droite
                        while 1:
                            newmouseX = princippage.winfo_pointerx()
                            newval = newmouseX - mouseX
                            if width-newval <= 1:
                                break
                            newdim = str(width+newval)+"x"+str(height)+"+"+str(x)+"+"+str(y)
                            princippage.geometry(newdim)
                            mouseEvent = win32api.GetKeyState(0x01)
                            maskechelle1.place_forget()
                            maskechelle2.place_forget()
                            maskechelle3.place_forget()
                            maskechelle4.place_forget()
                            maskechelle5.place_forget()
                            maskechelle6.place_forget()
                            maskechelle7.place_forget()
                            maskechelle8.place_forget()
                            newwidth = width+newval
                            maskechelle1 = Frame(resizebarpage, bd=0, bg=bgbar, cursor="size_ns")
                            maskechelle1.place(x=0, y=0, width=newwidth, height=sizebar)
                            maskechelle2 = Frame(resizebarpage, bd=0, bg=bgbar, cursor="size_we")
                            maskechelle2.place(x=0, y=0, width=sizebar, height=height)
                            maskechelle3 = Frame(resizebarpage, bd=0, bg=bgbar, cursor="size_ns")
                            maskechelle3.place(x=0, y=height-sizebar, width=newwidth, height=sizebar)
                            maskechelle4 = Frame(resizebarpage, bd=0, bg=bgbar, cursor="size_we")
                            maskechelle4.place(x=newwidth-sizebar, y=0, width=sizebar, height=height)
                            maskechelle5 = Frame(resizebarpage, bd=0, bg=bgcornerbar, cursor="size_nw_se")
                            maskechelle5.place(x=0, y=0, width=sizebar+1, height=sizebar+1)
                            maskechelle6 = Frame(resizebarpage, bd=0, bg=bgcornerbar, cursor="size_ne_sw")
                            maskechelle6.place(x=newwidth-(sizebar+1), y=0, width=(sizebar+1), height=sizebar+1)
                            maskechelle7 = Frame(resizebarpage, bd=0, bg=bgcornerbar, cursor="size_ne_sw")
                            maskechelle7.place(x=0, y=height-(sizebar+1), width=(sizebar+1), height=sizebar+1)
                            maskechelle8 = Frame(resizebarpage, bd=0, bg=bgcornerbar, cursor="size_nw_se")
                            maskechelle8.place(x=newwidth-(sizebar+1), y=height-(sizebar+1), width=sizebar+1, height=sizebar+1)
                            princippage.update()
                            if mouseEvent == -127 or mouseEvent == -128:
                                pass
                            else:
                                break
                    elif mouseY>=y and mouseY<=y+sizebar-1 and mouseX>=x and mouseX<=x+width: #Haut
                        while 1:
                            newmouseY = princippage.winfo_pointery()
                            newval = newmouseY - mouseY
                            if height-newval <= 1:
                                break
                            newdim = str(width)+"x"+str(height-newval)+"+"+str(x)+"+"+str(y+newval)
                            princippage.geometry(newdim)
                            mouseEvent = win32api.GetKeyState(0x01)
                            maskechelle1.place_forget()
                            maskechelle2.place_forget()
                            maskechelle3.place_forget()
                            maskechelle4.place_forget()
                            maskechelle5.place_forget()
                            maskechelle6.place_forget()
                            maskechelle7.place_forget()
                            maskechelle8.place_forget()
                            newheight = height-newval
                            maskechelle1 = Frame(resizebarpage, bd=0, bg=bgbar, cursor="size_ns")
                            maskechelle1.place(x=0, y=0, width=width, height=sizebar)
                            maskechelle2 = Frame(resizebarpage, bd=0, bg=bgbar, cursor="size_we")
                            maskechelle2.place(x=0, y=0, width=sizebar, height=newheight)
                            maskechelle3 = Frame(resizebarpage, bd=0, bg=bgbar, cursor="size_ns")
                            maskechelle3.place(x=0, y=newheight-sizebar, width=width, height=sizebar)
                            maskechelle4 = Frame(resizebarpage, bd=0, bg=bgbar, cursor="size_we")
                            maskechelle4.place(x=width-sizebar, y=0, width=sizebar, height=newheight)
                            maskechelle5 = Frame(resizebarpage, bd=0, bg=bgcornerbar, cursor="size_nw_se")
                            maskechelle5.place(x=0, y=0, width=sizebar+1, height=sizebar+1)
                            maskechelle6 = Frame(resizebarpage, bd=0, bg=bgcornerbar, cursor="size_ne_sw")
                            maskechelle6.place(x=width-(sizebar+1), y=0, width=(sizebar+1), height=sizebar+1)
                            maskechelle7 = Frame(resizebarpage, bd=0, bg=bgcornerbar, cursor="size_ne_sw")
                            maskechelle7.place(x=0, y=newheight-(sizebar+1), width=(sizebar+1), height=sizebar+1)
                            maskechelle8 = Frame(resizebarpage, bd=0, bg=bgcornerbar, cursor="size_nw_se")
                            maskechelle8.place(x=width-(sizebar+1), y=newheight-(sizebar+1), width=sizebar+1, height=sizebar+1)
                            princippage.update()
                            if mouseEvent == -127 or mouseEvent == -128:
                                pass
                            else:
                                break
                    elif mouseY>=y+height-sizebar and mouseY<=y+height and mouseX>=x and mouseX<=x+width: #Bas
                        while 1:
                            newmouseY = princippage.winfo_pointery()
                            newval = newmouseY - mouseY
                            if height-newval <= 1:
                                break
                            newdim = str(width)+"x"+str(height+newval)+"+"+str(x)+"+"+str(y)
                            princippage.geometry(newdim)
                            mouseEvent = win32api.GetKeyState(0x01)
                            maskechelle1.place_forget()
                            maskechelle2.place_forget()
                            maskechelle3.place_forget()
                            maskechelle4.place_forget()
                            maskechelle5.place_forget()
                            maskechelle6.place_forget()
                            maskechelle7.place_forget()
                            maskechelle8.place_forget()
                            newheight = height+newval
                            maskechelle1 = Frame(resizebarpage, bd=0, bg=bgbar, cursor="size_ns")
                            maskechelle1.place(x=0, y=0, width=width, height=sizebar)
                            maskechelle2 = Frame(resizebarpage, bd=0, bg=bgbar, cursor="size_we")
                            maskechelle2.place(x=0, y=0, width=sizebar, height=newheight)
                            maskechelle3 = Frame(resizebarpage, bd=0, bg=bgbar, cursor="size_ns")
                            maskechelle3.place(x=0, y=newheight-sizebar, width=width, height=sizebar)
                            maskechelle4 = Frame(resizebarpage, bd=0, bg=bgbar, cursor="size_we")
                            maskechelle4.place(x=width-sizebar, y=0, width=sizebar, height=newheight)
                            maskechelle5 = Frame(resizebarpage, bd=0, bg=bgcornerbar, cursor="size_nw_se")
                            maskechelle5.place(x=0, y=0, width=sizebar+1, height=sizebar+1)
                            maskechelle6 = Frame(resizebarpage, bd=0, bg=bgcornerbar, cursor="size_ne_sw")
                            maskechelle6.place(x=width-(sizebar+1), y=0, width=(sizebar+1), height=sizebar+1)
                            maskechelle7 = Frame(resizebarpage, bd=0, bg=bgcornerbar, cursor="size_ne_sw")
                            maskechelle7.place(x=0, y=newheight-(sizebar+1), width=(sizebar+1), height=sizebar+1)
                            maskechelle8 = Frame(resizebarpage, bd=0, bg=bgcornerbar, cursor="size_nw_se")
                            maskechelle8.place(x=width-(sizebar+1), y=newheight-(sizebar+1), width=sizebar+1, height=sizebar+1)
                            princippage.update()
                            if mouseEvent == -127 or mouseEvent == -128:
                                pass
                            else:
                                break
            else:
                pass
            princippage.update()

ss=1360
st=768
main.geometry(str(ss)+"x"+str(st)+"+"+str(100)+"+"+str(220))

Window_R(princippage=main,sizebar=20,height=st,width=ss, bgbar='green', bgcornerbar='blue')

main.mainloop()
