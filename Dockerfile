FROM node:22-alpine AS nodebuilder

WORKDIR /frontend/

COPY src ./src
COPY public ./public
COPY .npmrc ./.npmrc
COPY index.html ./index.html
COPY package.json ./package.json
COPY package-lock.json ./package-lock.json
COPY package.json ./package.json
COPY postcss.config.js ./postcss.config.js
COPY quasar.config.ts ./quasar.config.ts
COPY tsconfig.json ./tsconfig.json
COPY eslint.config.js ./eslint.config.js

RUN node -v
RUN npm -v
RUN npm i
RUN npm run build

RUN pwd && ls -la
RUN ls -la /frontend/dist/spa

#######################################################

FROM rust:1.85-alpine AS rustbuilder
RUN apk add musl-dev

WORKDIR /backend/

# RUN cargo install --path .
RUN rustup target add x86_64-unknown-linux-musl

COPY timeproject25_service ./timeproject25_service
COPY Cargo.toml ./Cargo.toml
COPY Cargo.lock ./Cargo.lock

# ENV RUSTFLAGS="-C target-feature=+crt-static"
RUN cargo build --target x86_64-unknown-linux-musl --release

RUN pwd && ls -la
RUN find . -type f -name "timeproject25_service"

#######################################################

# FROM scratch
FROM alpine

WORKDIR /app

COPY --from=nodebuilder /frontend/dist/spa /app/dist/spa
COPY --from=rustbuilder /backend/target/x86_64-unknown-linux-musl/release/timeproject25_service /app/timeproject25_service

RUN pwd && find ./ -type d

EXPOSE 8080/tcp
CMD ["/app/timeproject25_service"]
