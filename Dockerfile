FROM node:20 AS frontend_builder

WORKDIR /app

COPY ./frontend/package.json ./frontend/package-lock.json ./
RUN npm ci

COPY ./frontend .

RUN npm run build

FROM python:3.12 

WORKDIR /app

COPY ./backend/requirements.txt ./
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

COPY ./backend .
COPY --from=frontend_builder /app/dist ./static

CMD ["python3", "main.py"]
