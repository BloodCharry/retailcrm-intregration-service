FROM node:20-alpine

WORKDIR /app

COPY docs-site/package*.json ./

RUN npm install

COPY docs-site ./

EXPOSE 3001

RUN npm run build
CMD ["npm", "run", "serve"]

