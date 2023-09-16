# syntax=docker/dockerfile:1


FROM node:16-alpine as frontend
RUN npm install -g pnpm
WORKDIR /app
COPY frontend/package.json frontend/pnpm-lock.yaml ./
RUN pnpm install --frozen-lockfile
COPY ./frontend .
CMD ["pnpm", "run", "dev", "--host"]

FROM python:3.8-slim-buster as backend
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python3", "app.py"]
