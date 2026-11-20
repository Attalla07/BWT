import socket

INDIRIZZO= "127.0.0.1"
PORTA= 5000

parola= input("Scrivi una stringa: ")

client= socket.socket()
client.connect((INDIRIZZO,PORTA))

client.send(parola.encode())

#aspetto la ris. e la trasforrma da byte a testo e poi chiudo
risposta= client.recv(4096).decode()
print("Risposta del server: ", risposta)
client.close()
