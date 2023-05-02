FROM node:13.12.0-alpine as build

WORKDIR /app
COPY package*.json ./
RUN npm install

COPY . ./

RUN npm run build


FROM alpine

COPY --from=build /app/build /app/build