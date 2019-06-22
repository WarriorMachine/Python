class scaleOptions:
    def __init__(self, activebackground=None, bd=0, bg=None, bordercolor=None, cursor=None, command=None, digits=None, font=None, fg=None, from_=0, height=250, highlightbackground=None, 
    highlightcolor=None, label=None,orient=VERTICAL, page=main, relief=FLAT, repeatdelay=None, resolution=1 ,showvalue=1, sliderlength=30, state=None, takefocus=None, tickinterval=10, to=100, troughcolor=None,
    variable=None, width=75, sliderwidth=15, x=0, y=0):
        backFrameScaleOptions = Frame(page, bg=bg)
        backFrameScaleOptions.place(x=x, y=y, width=width, height=height)
        echelle = Scale(backFrameScaleOptions, activebackground=activebackground, bd=bd, bg=bg, cursor=cursor, command=command, digits=digits, font=font, fg=fg, from_=from_, 
        highlightbackground=highlightbackground, highlightcolor=highlightcolor, label=label, orient=orient, relief=relief, repeatdelay=repeatdelay, resolution=resolution, showvalue=showvalue, 
        sliderlength=sliderlength, state=state, takefocus=takefocus, tickinterval=tickinterval, to=to, troughcolor=troughcolor, variable=variable, width=sliderwidth)
        echelle.place(x=0, y=0, width=width, height=height)
        if bordercolor == None or bordercolor == 0:
            bordercolor = bg
        maskechelle1 = Frame(backFrameScaleOptions, bd=0, bg=bordercolor)
        maskechelle1.place(x=0, y=0, width=width, height=2)
        maskechelle2 = Frame(backFrameScaleOptions, bd=0, bg=bordercolor)
        maskechelle2.place(x=0, y=height-2, width=width, height=2)
        maskechelle3 = Frame(backFrameScaleOptions, bd=0, bg=bordercolor)
        maskechelle3.place(x=0, y=0, width=2, height=height)
        maskechelle4 = Frame(backFrameScaleOptions, bd=0, bg=bordercolor)
        maskechelle4.place(x=width-2, y=0, width=2, height=height)
