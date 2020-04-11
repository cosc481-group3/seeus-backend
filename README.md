# SEEUS App Backend

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/ec0375095ced4b55b5c14921e2e565bc)](https://app.codacy.com/gh/seeus-dev/seeus-backend?utm_source=github.com&utm_medium=referral&utm_content=seeus-dev/seeus-backend&utm_campaign=Badge_Grade_Dashboard)

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

### OAuth
OAuth requires the environmental variables OAUTH_CLIENT_ID and OAUTH_CLIENT_SECRET to be set in .env file.

-  SEEUS dev team: get the credentials from Nathan, the project documentation, or from the Google Developer Console.

-  External/open source contributors: you'll need to [create oauth credentials under your own Google project](https://support.google.com/googleapi/answer/6158862?hl=en) to obtain a client ID and secret.

### Dependency Management

Install [pipflow](https://github.com/iMerica/pipflow) with `pip3 install pipflow` locally on your machine. This automatically updates requirements.txt and rebuilds the docker image in one command.

You can add packages with `pipflow add [package]`. See docs for more commands.

## PostgreSQL

Run psql within the Postgres container with `./scripts/psql`.
 
[Postgres CLI Commands Cheat Sheet](https://gist.github.com/Kartones/dd3ff5ec5ea238d4c546)
