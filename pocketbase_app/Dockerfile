FROM alpine:latest AS downloader

ARG TARGETOS
ARG TARGETARCH
ARG TARGETVARIANT
ARG VERSION

ENV BUILDX_ARCH="${TARGETOS:-linux}_${TARGETARCH:-amd64}${TARGETVARIANT}"


# Security environment variables
ENV ADMIN_EMAIL="test@example.org"
ENV ADMIN_PASSWORD="1234567890"
ENV PB_ENCRYPTION_KEY="NOT_SAFE_SECRET_KEY"


RUN wget https://github.com/pocketbase/pocketbase/releases/download/v${VERSION}/pocketbase_${VERSION}_${BUILDX_ARCH}.zip \
    && unzip pocketbase_${VERSION}_${BUILDX_ARCH}.zip \
    && chmod +x /pocketbase

FROM alpine:latest
RUN apk update && apk add ca-certificates && rm -rf /var/cache/apk/*

EXPOSE 8090

COPY --from=downloader /pocketbase /usr/local/bin/pocketbase


# Add tracked data definitions of the pocketbase instance
COPY ./pb_migrations /pb_migrations
COPY ./pb_hooks /pb_hooks
COPY ./pb_public /pb_public

# Setup the starting script
COPY ./init.sh /usr/local/bin/init.sh
RUN chmod +x /usr/local/bin/init.sh
ENTRYPOINT ["/usr/local/bin/init.sh"]
