FROM python:3.7-alpine

WORKDIR /app
COPY . .

RUN ["pip3", "install", "pipenv"]
RUN ["pipenv", "install"]

EXPOSE 5000
CMD pipenv run python app.py