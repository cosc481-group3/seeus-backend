# SEEUS App Backend

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/ec0375095ced4b55b5c14921e2e565bc)](https://app.codacy.com/gh/seeus-dev/seeus-backend?utm_source=github.com&utm_medium=referral&utm_content=seeus-dev/seeus-backend&utm_campaign=Badge_Grade_Dashboard)

Backend for SEEUS Mobile App and Dispatcher Web App.

Built with Python and Flask.

## Development

### Installation

1.  [Install Docker](https://docs.docker.com/install/)
2.  Clone repo `git clone git@github.com:seeus-dev/seeus-backend.git`
3.  Run setup script `./scripts/setup`
4.  Start up the flask app and postgres DB with `docker-compose up -d` or `./scripts/start`

The server will be running at http://localhost:5000

Now setup your IDE ([instructions]() for IntelliJ/PyCharm) to point to the python interpreter in the docker-compose `web` service container.

In IntelliJ: 

1. Project Structure > SDKs > `+` > Python SDK > Docker Compose > Select web service
2. Project Structure > Project > Select SDK created in (1): "Remote Python .. Docker Compose web"

### Dependency Management

Install [pipflow](https://github.com/iMerica/pipflow) with `pip3 install pipflow` locally on your machine. This automatically updates requirements.txt and rebuilds the docker image in one command.

You can add packages with `pipflow add [package]`. See docs for more commands.

### Local OAuth Set Up
OAuth requires the environmental variables OAUTH_CLIENT_ID and OAUTH_CLIENT_SECRET to be set in .env file.

-  SEEUS dev team: get the credentials from project documentation or directly from the Google API Console.

-  External/open source contributors: [create oauth credentials under your own project in Google API Console](https://support.google.com/googleapi/answer/6158862?hl=en) to obtain a client ID and secret.

To access a local instance of the backend running on your computer from a physical phone:
1. Sign up for and install [ngrok](https://ngrok.com/). Start a tunnel.
2. Set API_BASE_URL to your ngrok tunnel's subdomain (`[yourcode].ngrok.io`) in the .env file in both backend and app.
3. Add the callback URL with your ngrok tunnel (`https://[yourcode].ngrok.io/app/auth/callback`) in [Google API Console](https://console.developers.google.com/apis/credentials) (Project: seeus-appliction) > Credentials > SEEUS Backend > Authorized redirect URIs

### PostgreSQL

Run psql within the Postgres container with `./scripts/psql`.
 
[Postgres CLI Commands Cheat Sheet](https://gist.github.com/Kartones/dd3ff5ec5ea238d4c546)
