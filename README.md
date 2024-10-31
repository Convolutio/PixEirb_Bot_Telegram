# PixiBot

Le pixibot est le bot qui va répondre n'importe quoi par télégram dès que
quelqu'un demande quand sort tel ou tel album.  

Il est sous le username `@Quand_sort_album_Pixeirb_bot`

## Comment que ca marche sous le capot?

Tout cela toune grâca à Pocketbase, un backend open source.

Ce pocketbase va faire plusieurs choses :

- Gérer une base de donnée sqlite
- Gérer l'authentification avec EirbConnect (OpenId Connect)
- Héberger un serveur http pour une interface admin
- Fournir une route `/get_random_response` qui renvoie une réponse au hasard de
la base de donnée (pas besoin d'être authentifié)

Il y a également un bot telegram écrit en python qui profitera de
`/get_random_response` pour répondre aux messages

## Comment Setup tout ca

Au niveau des variables d'environnement, il faut créer un fichier `.env` avec
les variables suivantes :

```sh
TELEGRAM_TOKEN="<your telegram bot token>"
POCKETBASE_URL="localhost:8090"
POCKETBASE_PORT=8090
```

Copiez le fichier `.env.example` et remplissez-le en tant que fichier `.env`
pour une configuration plus rapide.

## Configuration de Pocketbase

Le docker compose va utiliser un volume pour que les données restent si le docker n'est pas up. Il va créer un dossier `pb_data` dans lequel se trouveront les données.

Lors de la première instantiation, les données seront vides. Il faudra **créer
un administrateur** en allant sur la **page *admin*** (`/admin` ou bien `/_`).

Le docker pocketbase va être sur le port que vous aurez défini, on peut faire
une redirection de port en modifiant le docker compose.

### Configuration de l'authentification

Pour définir le client OpenId Connect relié à EirbConnect, aller dans ce lien

```sh
"http://${POCKETBASE_URL}/_/#/settings/auth-providers"
```

Ajouter le `Client Id` et le `Client secret` définis sur EirbConnect.
Les endpoints à fournir sont obtensibles sur `https://connect.eirb.fr/.well-known/openid-configuration`

Sur EirbConnect, définir pour le client le `Root URL` à la valeur de
`https://${POCKETBASE_URL}` ou `http://${POCKETBASE_URL}`
Aussi, activer le *Client authentication* et l'*Authorization*

L'autorisation aux administrateurs de Pixeirb uniquement est déléguée à
EirbConnect. Configurer donc les bonnes policies sur cette plateforme.
