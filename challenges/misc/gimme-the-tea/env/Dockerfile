FROM rust:alpine AS build
LABEL author="Mehdi Benouhoud"

COPY src /app/src
COPY Cargo.* /app/

WORKDIR /app

RUN apk update && apk add --no-cache libressl-dev pkgconfig musl-dev

RUN cargo build --release

FROM alpine:latest AS prod

RUN apk update && apk add --no-cache socat bash
COPY --from=build /app/target/release/gimmetea /app/gimmetea
COPY run.sh /app/run.sh
RUN chmod +x /app/run.sh && chmod +x /app/gimmetea

EXPOSE 1337

CMD ["/app/run.sh"]

