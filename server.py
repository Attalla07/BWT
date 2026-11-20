import socket
from bwt import bwt

INDIRIZZO= "127.0.0.1"
PORTA= 5000

#Per creare il serverr e meterlo in ascolto
server= socket.socket()
server.bind((INDIRIZZO,PORTA))
server.listen()
print("Server accesso e in aspetto di un cliente")
