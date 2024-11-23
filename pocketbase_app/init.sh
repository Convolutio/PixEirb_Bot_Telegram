#!/bin/sh
# This script can only be run in a docker container built as expected

# Initialize the database with the administrator credentials, if empty
if [ -z "$(ls -A /pb_data)" ]; then
    echo "-- Initializing PocketBase database... --"
    /usr/local/bin/pocketbase migrate up --migrationsDir=/pb_migrations \
      --dir=/pb_data --encryptionEnv=${PB_ENCRYPTION_KEY}

    echo "-- Adding admin account... --"
    /usr/local/bin/pocketbase admin create ${ADMIN_EMAIL} ${ADMIN_PASSWORD} \
      --dir=/pb_data --encryptionEnv=${PB_ENCRYPTION_KEY}
else
    echo "-- PocketBase data directory is already initialized. --"
fi

echo "-- Starting PocketBase instance... --"
exec /usr/local/bin/pocketbase serve --http=0.0.0.0:8090 \
  --publicDir=/pb_public --hooksDir=/pb_hooks --migrationsDir=/pb_migrations \
  --dir=/pb_data --encryptionEnv=${PB_ENCRYPTION_KEY}
