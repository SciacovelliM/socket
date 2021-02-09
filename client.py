#!/usr/bin/env python3


input_string = 'Hello'
print(type(input_string))
input_bytes_encoded = input_string.encode()
print(type(input_bytes_encoded))
print(input_bytes_encoded)
output_string=input_bytes_encoded.decode()
print(type(output_string))
print(output_string)

import socket

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224

sock_service = socket.socket()

sock_service.connect((SERVER_ADDRESS, SERVER_PORT))

print("Connesso a " + str((SERVER_ADDRESS, SERVER_PORT)))
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

    sock_service.send(dati)

    dati = sock_service.recv(2048)

    if not dati:
        print("Server non abbastanza tosto da risponderti. Exit")
        break
    
    dati = dati.decode()

    print("Ricevuto dal server:")
    print("Risultato operazione: "+dati + '\n')

sock_service.close()