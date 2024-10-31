FROM alpine:latest

ARG PB_VERSION=0.22.21

RUN  apk add --no-cache \
    unzip \
    git\
    ca-certificates

# download and unzip PocketBase
WORKDIR /app
ADD https://github.com/pocketbase/pocketbase/releases/download/v${PB_VERSION}/pocketbase_${PB_VERSION}_linux_amd64.zip /tmp/pb.zip
RUN unzip /tmp/pb.zip -d /app/pocketbase

# Copier le binaire PocketBase depuis la phase de build
COPY ./pb_migrations /app/pocketbase/pb_migrations

# uncomment to copy the local pb_hooks dir into the image
COPY ./pb_hooks /app/pocketbase/pb_hooks

COPY ./pb_public /app/pocketbase/pb_public

EXPOSE "${POCKETBASE_PORT}"

RUN echo "{\"pocketbaseUrl\": \"${POCKETBASE_URL}\"}" > /app/pocketbase/pb_public/config.json

# Dossier de données pour la base de données SQLite et les fichiers
VOLUME ["/app/pocketbase/pb_data"]

ENTRYPOINT ["/app/pocketbase/pocketbase", "serve", "--http", "${POCKETBASE_URL}"]
