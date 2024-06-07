FROM python:3.11-alpine
WORKDIR /app
COPY ./scripts/entrypoint.sh /scripts/entrypoint.sh
RUN apk update --no-cache \
    && apk add build-base postgresql-dev libpq --no-cache --virtual .build-deps \
    && pip install --no-cache-dir --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN apk del .build-deps
COPY . .
EXPOSE 8000
EXPOSE 7777
RUN chmod +x /scripts/entrypoint.sh
CMD ["sh", "/scripts/entrypoint.sh"]
