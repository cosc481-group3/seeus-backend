# SEEUS App Backend

Backend for SEEUS Mobile App and Dispatcher Web App.

Built with Python and Flask.

## Development

### Set Up

1.  [Install Docker](https://docs.docker.com/install/)
2.  Clone repo `git clone git@github.com:seeus-dev/seeus-backend.git`
3.  Run setup script `./scripts/setup`
4.  Start up the flask app and postgres DB with `docker-compose up -d` or `./scripts/start`

The server will be running at http://localhost:5000

Now setup your IDE ([instructions]() for IntelliJ/PyCharm) to point to the python interpreter in the docker-compose `web` service container.

In IntelliJ: 

1. Project Structure > SDKs > `+` > Python SDK > Docker Compose > Select web service
2. Project Structure > Project > Select SDK created in (1): "Remote Python .. Docker Compose web"

### Dependencies

Install [pipflow](https://github.com/iMerica/pipflow) with `pip3 install pipflow`

You can add packages with `pipflow add [package]`. This updates requirements.txt and rebuilds the docker image.

## PostgreSQL

Run psql within the Postgres container with `./scripts/psql`.
 
[Postgres CLI Commands Cheat Sheet](https://gist.github.com/Kartones/dd3ff5ec5ea238d4c546)