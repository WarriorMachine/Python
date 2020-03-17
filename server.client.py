from tkinter import *
from tkinter import messagebox
import socket
import os
import time

os.popen("title WarN version Alpha 1.0 : SERVER.server")

cePC = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

Hote = socket.gethostbyname(socket.gethostname())

print("Adresse a échanger :",Hote)
Hote_de_reponse = input('Adresse du correspondant : ') #adresse de l'autre pc
Port = 80
Portreponse = 234
username = str(os.getlogin())

cePC.bind((Hote,Port))
cePC.listen(1)

client, adresse = cePC.accept()
print("En attente du message de",adresse)

autrePC = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
autrePC.connect((Hote_de_reponse,Portreponse ))

while 1:
    Message = str(client.recv(1024),'mac_roman')
    if not Message:
        break
    print("\nClient User :",Message,"\a")
    reponseAuMessage = input("\n(Vous) "+username+" : ")
    val = bytes(str(username+" : "+reponseAuMessage), 'mac_roman')
    autrePC.send(val)

client.close()
