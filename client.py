#!/usr/bin/env python3

import socket
import sys

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224

#!La funzione crea una socket una socket (s) per la connessione con il server e la passa alla funzione invia_comandi(s)
def connessione_server(address, port):
    sock_service = socket.socket()
    sock_service.connect((SERVER_ADDRESS, SERVER_PORT))
    print("Connesso a " + str((SERVER_ADDRESS, SERVER_PORT)))
    invia_comandi(sock_service)
    sock_service.close()

#!La funzione riceve la socket connessa al server a la utilizza per richiedere il servizio
def invia_comandi(socket):
    while True:
        try:
            dati = input("Inserisci i dati da inviare [OPERAZIONE;NUMERO;NUMERO] (0 per uscire): ")
        except EOFError:
            print("\nOkay buffone. Exit")
            break
        if not dati:
            print("Non puoi inviare una stringa vuota Tizio Tosto!")
            continue
        if dati == '0':
            print("Chiudo la connessione con il server!")
            break
        
        dati = dati.encode()#trasforma dati in byte

        socket.send(dati)

        dati = socket.recv(2048)

        if not dati:
            print("Server non abbastanza tosto da risponderti. Exit")
            break
        
        dati = dati.decode()

        print("Ricevuto dal server:")
        print("Risultato operazione: "+dati + '\n')

    
# if __name__ == "__main__": consente al nostro codice di capire se stia venendo eseguito come script a se stante,
# o se è invece stato richiamato come modulo da un qualche programma per usare una o più delle sue varie
# funzioni e classi
if __name__ == "__main__":
    connessione_server(SERVER_ADDRESS, SERVER_PORT)