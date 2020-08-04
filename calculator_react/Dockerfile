FROM node:latest

WORKDIR /website

COPY package*.json ./

RUN npm install

COPY . .

CMD [ "npm", "start" ]