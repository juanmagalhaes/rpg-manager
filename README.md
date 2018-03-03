# RPG Manager - Made for Dungeon Masters [![CircleCI Build Status](https://circleci.com/gh/juanmagalhaes/rpg-manager.svg?style=svg)](https://circleci.com/gh/juanmagalhaes/rpg-manager) ![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)

Manage your Role Playing Game Campaign as you never done before.

Built with Python 3, Django, Django Rest Framework and Postgresql.
It has endpoints for the Cerebral selection process challenge.


## set up

```
  # install pipenv (or pip and virtualenv if you prefer)
  $ pipenv shell
  $ pipenv install
```

** OBS: ** It needs a postgres server runing in order to work properly
so you should install postgres locally or run it with docker.

** OBS 2: ** It needs a database called olist_challenge created so you can
manually do this or rely on the docker image `juanmagalhaes/rpg_manager_db`

with db set up you can:

```
  # run migrations
  $ python manage.py migrate
```

and then:

```
  # run server
  $ python manage.py runserver
```

and thats it. Up and running!

## To run tests, do:

```
  # run tests
  $ python manage.py test
```

## Instructions to run on docker container


```
  # On the root of the project
  $ docker-compose up
```

It will do everything for you.

Production link to the api running on heroku free servers:

[production rpg-manager](https://rpg-manager.herokuapp.com/api/character/)

Hope you enjoy!!! =D

