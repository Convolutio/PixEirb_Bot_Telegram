# PixiBot

Le pixibot est le bot qui va répondre n'importe quoi par télégram dès que
quelqu'un demande quand sort tel ou tel album.  

Il est sous le username `@Quand_sort_album_Pixeirb_bot`

## Comment que ca marche sous le capot?

Tout cela tourne grâca à Pocketbase, un backend open source.

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
PB_ENCRYPTION_KEY="<your secret db encryption key"
ADMIN_EMAIL="test@example.org"
ADMIN_PASSWORD="1234567890"
```

Les 3 dernières variables permettent de définir le compte administrateur au
démarrage du serveur et de crypter la base de données qui contient des données
sensibles de configuration, notamment la clé secrète pour se connecter à
EirbConnect.

Copiez le fichier `.env.example` et remplissez-le en tant que fichier `.env`
pour une configuration plus rapide.

## Configuration de Pocketbase

Le docker compose va utiliser un volume pour que les données restent si le
docker n'est pas up. Il va créer un dossier `pb_data` dans lequel se trouveront
les données.

Lors de la première instantiation, les données seront vides. Il faudra **créer
un administrateur** en allant sur la **page *admin*** (`/admin` ou bien `/_`).

Il est possible sinon de placer un dossier `pb_data` que vous avez à
disposition afin d'initier le container avec des configurations du serveur et
des données déjà présentes.

Le docker pocketbase va être sur le port que vous aurez défini, on peut faire
une redirection de port en modifiant le docker compose.

### Configuration de l'authentification

Pour définir le client OpenId Connect relié à EirbConnect, aller dans ce lien

```sh
"http://${POCKETBASE_URL}/_/#/settings/auth-providers"
```

Ajouter le `Client Id` et le `Client secret` définis côté EirbConnect.
Les endpoints à fournir sont obtensibles sur `https://connect.eirb.fr/.well-known/openid-configuration`

#### Côté EirbConnect

*Normalement, la bonne configuration est déjà faite 😊*

Sur EirbConnect, définir pour le client le `Root URL` à la valeur de
`https://${POCKETBASE_URL}` ou `http://${POCKETBASE_URL}`
Aussi, activer le *Client authentication* et l'*Authorization*

L'autorisation aux administrateurs de Pixeirb uniquement est déléguée à
EirbConnect. Configurer donc les bonnes policies sur cette plateforme et
ajouter les bonnes personnes dans le groupe des admins Pixibot.
