# FROM node:latest
# WORKDIR /code
# COPY package.json package.json
# RUN npm install
# COPY . .

FROM tiangolo/node-frontend:10 as build-stage
WORKDIR /app
COPY package.json /app/
COPY package-lock.json /app/
RUN npm install
COPY ./ /app/
