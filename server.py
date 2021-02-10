#!/usr/bin/env python3
import socket

SERVER_ADDRESS = '127.0.0.1'

#Numero di porta deve essere maggiore di 1024 perché le altre sono riservate
SERVER_PORT = 22224

#Crea un endpoint di ascolto (sock_listen) dal quale accettare connessioni in entrata
#la socket di ascolto viene passata alla funzione ricevi_comandi la quale accettarichieste di connessione
#e per ognuna crea una socket per i dati (socket service) da cui ricevere le richieste e inviare le risposte
def avvia_server(address, port):
    sock_listen = socket.socket()
    sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock_listen.bind((address, port))
    sock_listen.listen(5)
    print("Server in ascolto su %s." % str((address, port)))
    ricevi_comandi(sock_listen)

def ricevi_comandi(socket):
    while True:
        sock_service, addr_client = socket.accept()
        print("\nConnessione ricevuta da tizio tosto " + str(addr_client))
        print("\nAspetto di ricevere i dati da tizio tosto")
        contConn=0
        while True:
            dati = sock_service.recv(2048) #ricevo dati
            contConn+=1
            
            if not dati:
                print("Fine dati dal client. Fine della storia. Reset")
                break
            

            dati = dati.decode()
            print("Ricevuto: '%s'" % dati)
            if dati=='0':
                print("Chiudo la connessione con tizio tosto" + str(addr_client))
                break
            dati = "Risposta a tizio tosto : " + str(addr_client) + ". Il valore del contatore è : " + str(contConn)

            dati = dati.split(";")#separa i caratteri che hanno nel mezzo ";" e trasforma la stringa in una lista
            print(dati)
            ris=int()
            #controlla la cella 0 contenente l'operazione da svolgere per poi assegnarla alle celle 1 e 2 ed applicare l'operazione
            if dati[0]=="più":
                ris= dati[1] + dati[2]
            elif dati[0]=="meno":
                ris= dati[1] - dati[2]
            elif dati[0]=="per":
                ris= dati[1] * dati[2]
            elif dati[0]=="diviso":
                ris= dati[1] / dati[2]
            dati=str(ris)
            dati = dati.encode()#trasforma i dati in byte
            sock_service.send(dati)#invia i dati
        sock_service.close()#chiude la trasmissione

# if __name__ == "__main__": consente al nostro codice di capire se stia venendo eseguito come script a se stante,
# o se è invece stato richiamato come modulo da un qualche programma per usare una o più delle sue varie
# funzioni e classi
if __name__ == "__main__":
    avvia_server(SERVER_ADDRESS, SERVER_PORT)