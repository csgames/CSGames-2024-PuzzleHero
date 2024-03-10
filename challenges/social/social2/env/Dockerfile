FROM nginx:alpine

COPY index.html /usr/share/nginx/html
COPY beautiful.css /usr/share/nginx/html
COPY crypto-js.js /usr/share/nginx/html
COPY jquery-3.7.1.min.js /usr/share/nginx/html
COPY secrets.js /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]