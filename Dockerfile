FROM python:3.11-alpine AS base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
# RUN apk update --no-cache \
#     && apk add --no-cache pkgconfig build-base linux-headers pcre-dev libpq curl python3-dev linux-headers pcre-dev just postgresql-dev --virtual .build-deps \
#     && pip install --no-cache-dir --upgrade pip \
#     && apk del .build-deps \
#     && apk add just

# RUN apk add python3-dev build-base linux-headers pcre-dev
# RUN apk update
# RUN apk add pkgconfig mysql-dev
# RUN apk add postgresql-dev
# RUN pip install gunicorn
# RUN apk add just
RUN apk update --no-cache \
    && apk add --no-cache pkgconfig build-base linux-headers pcre-dev libpq curl python3-dev postgresql-dev mysql-dev just --virtual .build-deps \
    && pip install --no-cache-dir --upgrade pip

# Verify the installation of `just`
RUN just --version
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN chmod +x justfile

FROM base AS worker


FROM base AS development
EXPOSE 8000
CMD ["just", "dev"]

FROM base AS production
EXPOSE 8000
CMD ["just", "prod"]
