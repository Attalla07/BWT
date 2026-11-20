import socket
from bwt import bwt

INDIRIZZO= "127.0.0.1"
PORTA= 5000

#Per creare il serverr e meterlo in ascolto
server= socket.socket()
server.bind((INDIRIZZO,PORTA))
server.listen()
print("Server accesso e in aspetto di un cliente")

#while True serve per restare acceso e servire piu client uno dopo l'altro
while True:
    client, indirizzo_client= server.accept()
    print("Client collegato")
#per trrasformare la parola recivota in byte in testo
    parola= client.recv(4096).decode()
    print("messaggio ricevuto: ", parola)

