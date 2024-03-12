FROM node:21-alpine

WORKDIR /app

COPY app .

RUN npm install

EXPOSE 8000

CMD ["node", "app.js"]
