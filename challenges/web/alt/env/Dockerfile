FROM python:3.10 as builder

WORKDIR /app

COPY . .


RUN chmod +x build.sh
RUN ./build.sh

FROM nginx:alpine

COPY --from=builder /app/public/ /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]