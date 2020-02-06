from tkinter import *
import time
import os
import win32api

main = Tk()
main.overrideredirect(1)
main['bg']='crimson'

class Window_MR():
    def __init__(self, width=1360, height= 768, princippage=main, resizebarpage=main, sizebar=4, sizemovebar=15, bgbar='white', bgmovebar='gray30', bgcornerbar='gray99'):
        data_size = dict()
        data_size["width"] = width
        data_size["height"] = height
        maskechelle0 = Frame(resizebarpage, bd=0, bg=bgmovebar, cursor="hand2")
        maskechelle0.place(x=sizebar, y=sizebar, width=width-sizebar*2, height=sizemovebar)
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
            princippage.update()
            mouseEvent = win32api.GetKeyState(0x01) #etat du clique gauche
            x = princippage.winfo_rootx() #x = sL
            y = princippage.winfo_rooty() #y = sH
            mouseX = princippage.winfo_pointerx()
            mouseY = princippage.winfo_pointery()
            time.sleep(0.01)
            if mouseY>=y+sizebar and mouseY<=y+sizemovebar-1 and mouseX>=x+sizebar and mouseX<=x+data_size["width"]-sizebar*2:
                if mouseEvent == -128 or mouseEvent == -127:
                    while 1:
                        mouseX = princippage.winfo_pointerx()
                        mouseY = princippage.winfo_pointery()
                        newdim = str(data_size['width'])+"x"+str(data_size['height'])+"+"+str(mouseX-round(data_size['width']/2))+"+"+str(mouseY-sizebar)
                        princippage.geometry(newdim)
                        mouseEvent = win32api.GetKeyState(0x01)
                        princippage.update()
                        if mouseEvent == -127 or mouseEvent == -128:
                            pass
                        else:
                            break
            else:
                pass
            if mouseX>=x and mouseX<=x+sizebar-1 and mouseY>=y and mouseY<=y+data_size['height'] or mouseX>=x+data_size['width']-sizebar and mouseX<=x+data_size['width'] and mouseY>=y and mouseY<=y+data_size['height'] or mouseY>=y and mouseY<=y+sizebar-1 and mouseX>=x and mouseX<=x+data_size['width'] or mouseY>=y+data_size['height']-sizebar and mouseY<=y+data_size['height'] and mouseX>=x and mouseX<=x+data_size['width']:
                if mouseEvent == -128 or mouseEvent == -127:
                    mouseX = princippage.winfo_pointerx()
                    mouseY = princippage.winfo_pointery()
                    x = princippage.winfo_rootx() #x = sL
                    y = princippage.winfo_rooty() #y = sH
                    if mouseX>=x and mouseX<=x+sizebar-1 and mouseY>=y and mouseY<=y+data_size['height']: #Gauche
                        while 1:
                            newmouseX = princippage.winfo_pointerx()
                            newval = newmouseX - mouseX
                            if width-newval <= 1:
                                break
                            newwidth = width-newval
                            data_size['width'] = newwidth
                            newdim = str(data_size['width'])+"x"+str(data_size['height'])+"+"+str(x+newval)+"+"+str(y)
                            princippage.geometry(newdim)
                            mouseEvent = win32api.GetKeyState(0x01)
                            maskechelle0.place_forget()
                            maskechelle1.place_forget()
                            maskechelle2.place_forget()
                            maskechelle3.place_forget()
                            maskechelle4.place_forget()
                            maskechelle5.place_forget()
                            maskechelle6.place_forget()
                            maskechelle7.place_forget()
                            maskechelle8.place_forget()
                            maskechelle0 = Frame(resizebarpage, bd=0, bg=bgmovebar, cursor="hand2")
                            maskechelle0.place(x=sizebar, y=sizebar, width=newwidth, height=sizemovebar)
                            maskechelle1 = Frame(resizebarpage, bd=0, bg=bgbar, cursor="size_ns")
                            maskechelle1.place(x=0, y=0, width=newwidth, height=sizebar)
                            maskechelle2 = Frame(resizebarpage, bd=0, bg=bgbar, cursor="size_we")
                            maskechelle2.place(x=0, y=0, width=sizebar, height=data_size['height'])
                            maskechelle3 = Frame(resizebarpage, bd=0, bg=bgbar, cursor="size_ns")
                            maskechelle3.place(x=0, y=data_size['height']-sizebar, width=newwidth, height=sizebar)
                            maskechelle4 = Frame(resizebarpage, bd=0, bg=bgbar, cursor="size_we")
                            maskechelle4.place(x=newwidth-sizebar, y=0, width=sizebar, height=data_size['height'])
                            maskechelle5 = Frame(resizebarpage, bd=0, bg=bgcornerbar, cursor="size_nw_se")
                            maskechelle5.place(x=0, y=0, width=sizebar+1, height=sizebar+1)
                            maskechelle6 = Frame(resizebarpage, bd=0, bg=bgcornerbar, cursor="size_ne_sw")
                            maskechelle6.place(x=newwidth-(sizebar+1), y=0, width=(sizebar+1), height=sizebar+1)
                            maskechelle7 = Frame(resizebarpage, bd=0, bg=bgcornerbar, cursor="size_ne_sw")
                            maskechelle7.place(x=0, y=data_size['height']-(sizebar+1), width=(sizebar+1), height=sizebar+1)
                            maskechelle8 = Frame(resizebarpage, bd=0, bg=bgcornerbar, cursor="size_nw_se")
                            maskechelle8.place(x=newwidth-(sizebar+1), y=data_size['height']-(sizebar+1), width=sizebar+1, height=sizebar+1)

                            princippage.update()
                            if mouseEvent == -127 or mouseEvent == -128:
                                pass
                            else:
                                break
                    elif mouseX>=x+data_size['width']-sizebar and mouseX<=x+data_size['width'] and mouseY>=y and mouseY<=y+data_size['height']: #Droite
                        while 1:
                            newmouseX = princippage.winfo_pointerx()
                            newval = newmouseX - mouseX
                            if width-newval <= 1:
                                break
                            newwidth = width+newval
                            data_size['width'] = newwidth
                            newdim = str(data_size['width'])+"x"+str(data_size['height'])+"+"+str(x)+"+"+str(y)
                            princippage.geometry(newdim)
                            mouseEvent = win32api.GetKeyState(0x01)
                            maskechelle0.place_forget()
                            maskechelle1.place_forget()
                            maskechelle2.place_forget()
                            maskechelle3.place_forget()
                            maskechelle4.place_forget()
                            maskechelle5.place_forget()
                            maskechelle6.place_forget()
                            maskechelle7.place_forget()
                            maskechelle8.place_forget()
                            maskechelle0 = Frame(resizebarpage, bd=0, bg=bgmovebar, cursor="hand2")
                            maskechelle0.place(x=sizebar, y=sizebar, width=newwidth, height=sizemovebar)
                            maskechelle1 = Frame(resizebarpage, bd=0, bg=bgbar, cursor="size_ns")
                            maskechelle1.place(x=0, y=0, width=newwidth, height=sizebar)
                            maskechelle2 = Frame(resizebarpage, bd=0, bg=bgbar, cursor="size_we")
                            maskechelle2.place(x=0, y=0, width=sizebar, height=data_size['height'])
                            maskechelle3 = Frame(resizebarpage, bd=0, bg=bgbar, cursor="size_ns")
                            maskechelle3.place(x=0, y=data_size['height']-sizebar, width=newwidth, height=sizebar)
                            maskechelle4 = Frame(resizebarpage, bd=0, bg=bgbar, cursor="size_we")
                            maskechelle4.place(x=newwidth-sizebar, y=0, width=sizebar, height=data_size['height'])
                            maskechelle5 = Frame(resizebarpage, bd=0, bg=bgcornerbar, cursor="size_nw_se")
                            maskechelle5.place(x=0, y=0, width=sizebar+1, height=sizebar+1)
                            maskechelle6 = Frame(resizebarpage, bd=0, bg=bgcornerbar, cursor="size_ne_sw")
                            maskechelle6.place(x=newwidth-(sizebar+1), y=0, width=(sizebar+1), height=sizebar+1)
                            maskechelle7 = Frame(resizebarpage, bd=0, bg=bgcornerbar, cursor="size_ne_sw")
                            maskechelle7.place(x=0, y=data_size['height']-(sizebar+1), width=(sizebar+1), height=sizebar+1)
                            maskechelle8 = Frame(resizebarpage, bd=0, bg=bgcornerbar, cursor="size_nw_se")
                            maskechelle8.place(x=newwidth-(sizebar+1), y=data_size['height']-(sizebar+1), width=sizebar+1, height=sizebar+1)
                            princippage.update()
                            if mouseEvent == -127 or mouseEvent == -128:
                                pass
                            else:
                                break
                    elif mouseY>=y and mouseY<=y+sizebar-1 and mouseX>=x and mouseX<=x+data_size['width']: #Haut
                        while 1:
                            newmouseY = princippage.winfo_pointery()
                            newval = newmouseY - mouseY
                            if height-newval <= 1:
                                break
                            newheight = height-newval
                            data_size['height'] = newheight
                            newdim = str(data_size['width'])+"x"+str(height-newval)+"+"+str(x)+"+"+str(y+newval)
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
                            maskechelle1 = Frame(resizebarpage, bd=0, bg=bgbar, cursor="size_ns")
                            maskechelle1.place(x=0, y=0, width=data_size['width'], height=sizebar)
                            maskechelle2 = Frame(resizebarpage, bd=0, bg=bgbar, cursor="size_we")
                            maskechelle2.place(x=0, y=0, width=sizebar, height=newheight)
                            maskechelle3 = Frame(resizebarpage, bd=0, bg=bgbar, cursor="size_ns")
                            maskechelle3.place(x=0, y=newheight-sizebar, width=data_size['width'], height=sizebar)
                            maskechelle4 = Frame(resizebarpage, bd=0, bg=bgbar, cursor="size_we")
                            maskechelle4.place(x=data_size['width']-sizebar, y=0, width=sizebar, height=newheight)
                            maskechelle5 = Frame(resizebarpage, bd=0, bg=bgcornerbar, cursor="size_nw_se")
                            maskechelle5.place(x=0, y=0, width=sizebar+1, height=sizebar+1)
                            maskechelle6 = Frame(resizebarpage, bd=0, bg=bgcornerbar, cursor="size_ne_sw")
                            maskechelle6.place(x=data_size['width']-(sizebar+1), y=0, width=(sizebar+1), height=sizebar+1)
                            maskechelle7 = Frame(resizebarpage, bd=0, bg=bgcornerbar, cursor="size_ne_sw")
                            maskechelle7.place(x=0, y=newheight-(sizebar+1), width=(sizebar+1), height=sizebar+1)
                            maskechelle8 = Frame(resizebarpage, bd=0, bg=bgcornerbar, cursor="size_nw_se")
                            maskechelle8.place(x=data_size['width']-(sizebar+1), y=newheight-(sizebar+1), width=sizebar+1, height=sizebar+1)
                            princippage.update()
                            if mouseEvent == -127 or mouseEvent == -128:
                                pass
                            else:
                                break
                    elif mouseY>=y+data_size['height']-sizebar and mouseY<=y+data_size['height'] and mouseX>=x and mouseX<=x+data_size['width']: #Bas
                        while 1:
                            newmouseY = princippage.winfo_pointery()
                            newval = newmouseY - mouseY
                            if height-newval <= 1:
                                break
                            newheight = height+newval
                            data_size['height'] = newheight
                            newdim = str(data_size['width'])+"x"+str(data_size['height'])+"+"+str(x)+"+"+str(y)
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
                            maskechelle1 = Frame(resizebarpage, bd=0, bg=bgbar, cursor="size_ns")
                            maskechelle1.place(x=0, y=0, width=data_size['width'], height=sizebar)
                            maskechelle2 = Frame(resizebarpage, bd=0, bg=bgbar, cursor="size_we")
                            maskechelle2.place(x=0, y=0, width=sizebar, height=newheight)
                            maskechelle3 = Frame(resizebarpage, bd=0, bg=bgbar, cursor="size_ns")
                            maskechelle3.place(x=0, y=newheight-sizebar, width=data_size['width'], height=sizebar)
                            maskechelle4 = Frame(resizebarpage, bd=0, bg=bgbar, cursor="size_we")
                            maskechelle4.place(x=data_size['width']-sizebar, y=0, width=sizebar, height=newheight)
                            maskechelle5 = Frame(resizebarpage, bd=0, bg=bgcornerbar, cursor="size_nw_se")
                            maskechelle5.place(x=0, y=0, width=sizebar+1, height=sizebar+1)
                            maskechelle6 = Frame(resizebarpage, bd=0, bg=bgcornerbar, cursor="size_ne_sw")
                            maskechelle6.place(x=data_size['width']-(sizebar+1), y=0, width=(sizebar+1), height=sizebar+1)
                            maskechelle7 = Frame(resizebarpage, bd=0, bg=bgcornerbar, cursor="size_ne_sw")
                            maskechelle7.place(x=0, y=newheight-(sizebar+1), width=(sizebar+1), height=sizebar+1)
                            maskechelle8 = Frame(resizebarpage, bd=0, bg=bgcornerbar, cursor="size_nw_se")
                            maskechelle8.place(x=data_size['width']-(sizebar+1), y=newheight-(sizebar+1), width=sizebar+1, height=sizebar+1)
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

Window_MR(princippage=main,height=st,width=ss, bgbar='green', bgcornerbar='blue')

main.update()
