# PixiBot

Le pixibot est le bot qui va répondre n'importe quoi par télégram dès que quelqu'un demande quand sort tel ou tel album.  

Il est sous le username @Quand_sort_album_Pixeirb_bot

## Comment que ca marche sous le capot?

Tout cela toune grâca à Pocketbase, un backend open source.

Ce pocketbase va faire plusieurs choses : 
- Gérer une base de donnée sqlite
- Gérer l'authentification avec EirbConnect
- Hoster un serveur http pour une interface admin
- Fournir une route /get_random_response qui renvoie une réponse au hasard de la base de donnée (pas besoin d'être authentifié)

Il y a également un bot telegram écrit en python qui profitera de /get_random_response pour répondre aux messages

## Comment Setup tout ca

Au niveau des variables d'environnement, il faut créer un fichier ".env" avec les variables suivantes :
```
TELEGRAM_TOKEN=...
POCKETBASE_URL=...
```
