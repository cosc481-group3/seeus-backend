# SEEUS App Backend

Backend for SEEUS Mobile App and Dispatcher Web App.

Built with Python and Flask.

## Development

### Set Up

1. [Install Docker](https://docs.docker.com/install/)
2. Clone repo `git clone git@github.com:seeus-dev/seeus-backend.git`
3. Run install script `./scripts/install`
4. Start up the flask app and postgres DB with `./scripts/start` (This just runs docker-compose)

The server will be running at http://localhost:5000

### Dependency Management

We're using Pipenv to manage dependencies. Pipenv manages both the virtualenv and ensures a specific version of python is being used. 

Since we're using Docker, you don't have to install Python, pip, or Pipenv. This is all managed automatically through Docker, and everything stays in the Docker web container.

Because of this, to install or update dependencies via pip/pipenv, you have to run `pipenv` command through the web container. We have a helper script to do this:

```
./scripts/pipenv
```

For example, to install `flask` dependency you would run:

```
./scripts/pipenv install flask
```
