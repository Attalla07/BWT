import socket

INDIRIZZO= "127.0.0.1"
PORTA= 5000

parola= input("Scrivi una stringa: ")

client= socket.socket()
client.connect((INDIRIZZO,PORTA))

client.send(parola.encode())