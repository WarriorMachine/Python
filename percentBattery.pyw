from tkinter import *
import psutil, time

ll, hh = 50, 28 #lenght & height window size
main = Tk()
main.focus_set()
main.overrideredirect(1)
main.wm_attributes("-topmost", 1)
large, haut = main.winfo_screenwidth(), main.winfo_screenheight()
perct, connect, timer = StringVar(), StringVar(), StringVar()
main.geometry("%dx%d+%d+%d" % (ll, hh, large/1.25-ll/2, 0))
main['bg'] = '#1a1a1a'

def maj():
    battery, plugged = psutil.sensors_battery(), battery.power_plugged
    plug = "🔒" if plugged else "🔓"
    plugtext.configure(fg="mediumseagreen") if plugged else plugtext.configure(fg="gold")
    if battery.percent >= 50: percenttext.configure(fg="springgreen")
    elif battery.percent > 25: percenttext.configure(fg="mediumseagreen")
    elif battery.percent > 15 : percenttext.configure(fg="orange")
    else: percenttext.configure(fg="crimson")
    connect.set(plug)
    perct.set(str(battery.percent)+"%")
    timer.set(time.strftime('%H:%M:%S'))
    main.after(5000, maj)

def moreLess(val):
    main.geometry("%dx%d+%d+%d" % (ll, hh, large/1.25-ll/2, 0)) if val else main.geometry("%dx%d+%d+%d" % (ll, hh/2+2, large/1.25-ll/2, 0))

percenttext = Button(main, textvariable=perct, bg='#1a1a1a', fg='gray60', border=0, activebackground="#1a1a1a", activeforeground="#1a1a1a", command= lambda:moreLess(True)).place(x=0, y=2, width= ll/1.5, height= 12)
plugtext = Button(main, textvariable=connect, bg='#1a1a1a', fg='gray60', border=0, activebackground="#1a1a1a", activeforeground="#1a1a1a", command= lambda:moreLess(True)).place(x=ll/1.5, y=0, width= ll-ll/1.5, height= 12)
timetext = Button(main, textvariable=timer, bg='#1a1a1a', fg='gray60', border=0, activebackground="#1a1a1a", activeforeground="#1a1a1a", command= lambda:moreLess(False)).place(x=0, y=15, width= ll, height= 10)
quitbutton = Button(main, text="❌", bg='#1a1a1a', fg='#1a1a1a', activebackground='crimson', border=0, command=quit).place(x=ll-7, y=0, width= 7, height= 7)

maj()

main.mainloop()
