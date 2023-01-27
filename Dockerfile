FROM python:3.10-alpine
LABEL creator="gmoroz"

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

COPY . .
RUN python3 -m pip install -r requirements.txt

ENTRYPOINT ["sh", "entrypoint.sh"]