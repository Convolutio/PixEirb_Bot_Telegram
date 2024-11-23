FROM alpine:latest

ARG PB_VERSION=0.22.27

RUN apk add --no-cache \
    unzip \
    ca-certificates

# download and unzip PocketBase
ADD https://github.com/pocketbase/pocketbase/releases/download/v${PB_VERSION}/pocketbase_${PB_VERSION}_linux_amd64.zip /tmp/pb.zip
# Copy PocketBase's binary in the build stage
RUN mkdir -p /app/pocketbase
RUN unzip /tmp/pb.zip -d /app/pocketbase/

# add tracked data tables' definitions in the containerized pb app
COPY ./pb_migrations /app/pocketbase/pb_migrations

# add tracked data hooks' definitions in the containerized pb app
COPY ./pb_hooks /app/pocketbase/pb_hooks

# add tracked static pages in the containerized pb app
COPY ./pb_public /app/pocketbase/pb_public

EXPOSE 8090

# Dossier de données pour la base de données SQLite et les fichiers
VOLUME ["/app/pocketbase/pb_data"]

CMD ["/app/pocketbase/pocketbase", "serve", "--http=0.0.0.0:8090"]
