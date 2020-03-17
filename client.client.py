from tkinter import *
from tkinter import messagebox
import socket
import os
import time

os.popen("title WarN version Alpha 1.0 : CLIENT.client")

cePC = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

Hote = socket.gethostbyname(socket.gethostname())

print("Adresse a échanger :",Hote)
Hote_de_reponse = input('Adresse du correspondant : ') #adresse de l'autre pc
Port = 80
Port_de_reponse = 234
username = str(os.getlogin())

cePC.connect((Hote_de_reponse,Port))

autrePC = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
autrePC.bind((Hote,Port_de_reponse))
autrePC.listen(1)

client, adresse = autrePC.accept()

while 1:
    Message = input("\n(Vous) "+username+" : ")
    val = bytes(str(username+" : "+Message), 'mac_roman')
    cePC.send(val)
    reponseAuMessage = str(client.recv(1024),'mac_roman')
    if not reponseAuMessage:
            break
    print("\n Server User :",reponseAuMessage,"\a")
		
client.close()
