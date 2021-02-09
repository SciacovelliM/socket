#!/usr/bin/env python3
import socket



SERVER_ADDRESS = '127.0.0.1'

SERVER_PORT = 22224

sock_listen = socket.socket()

sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock_listen.bind((SERVER_ADDRESS, SERVER_PORT))

sock_listen.listen(5)

print("Server in ascolto su %s." % str((SERVER_ADDRESS, SERVER_PORT)))


while True:
    sock_service, addr_client = sock_listen.accept()
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

        dati = dati.split(";")
        print(dati)
        ris=0
        if dati[0]=="più":
            ris=double(dati[1])+double(dati[2])
        elif dati[0]=="meno":
            ris=double(dati[1])-double(dati[2])
        elif dati[0]=="per":
            ris=double(dati[1])*double(dati[2])
        elif dati[0]=="diviso":
            ris=double(dati[1])/double(dati[2])
        dati=str(ris)
        
        dati = dati.encode()#trasforma i dati in byte

        


        sock_service.send(dati)#invia i dati

    sock_service.close()#chiude la trasmissione