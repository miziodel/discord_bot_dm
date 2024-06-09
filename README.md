# Esempi per usare invio messaggi diretti 

## setup in discord

- creare application e bot nel server impostati come serve, con gli intent e i permessi adeguati a permettere al bot di lavorare con gli utenti e di inviare messaggi

## secret.py

creare un file secret.py e infilarci dentro:

  token_bot = <token del bot>

## discord_bot

offre il codice base per creare il bot, mandando lo script in esecuzione.

aprendo un canale diretto col bot, e usando il comando 

  !send_dm <username> <messaggio>

il messaggio <messaggio> verrà inviato dal bot all'utente direttamente identificato da <username> nel server

se il bot riceve un messaggio, questo viene loggato nella shell

## send_dm.py

offre il codice per lanciare da shall il comando che prende lo username di un utente e se esiste nel server gli invia un messaggio privato.

  > send_dm <username> "<messaggio>"