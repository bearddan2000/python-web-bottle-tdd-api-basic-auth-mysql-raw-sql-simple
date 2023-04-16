# python-web-bottle-tdd-api-basic-auth-mysql-raw-sql-simple

## Description
Simple web app that serves an api for a bottle project using basic auth.
Requires basic authentication for endpoints.

| username | password |
| -------- | -------- |
| *user* | *pass* |

Uses and replicate over 4 databases on the same server:
- animal, the prod
- test_api, for remotely testing api by *testify*
- test_chained, tests strategy chained sql functions by *pytest*
- test_raw, tests strategy raw sql by *pytest*
*Note: test data should not be on same server as prod; only brevity made it necessary.*

Pytests are aggregated to a single folder, reports, and viewable with an allure server.

Uses sqlalchemy query a table `dog` using raw sql.

## Tech stack
- python
  - bottle
  - sqlalchemy
  - pytest
  - allure-pytest
  - testify
  - response
- mysql

## Docker stack
- python:latest
- mariadb

## To run
`sudo ./install.sh -u`
- Get all dogs: http://localhost/dog
  - Schema id, breed, and color
- CRUD opperations
  - Create: curl -i -X PUT localhost/dog/<id> -u 'user:pass'
  - Read: http://localhost/dog/<id> -u 'user:pass'
  - Update: curl -i -X POST localhost/dog/<id>/<breed>/<color> -u 'user:pass'
  - Delete: curl -i -X DELETE localhost/dog/<id> -u 'user:pass'

## To stop
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`

## Credit
[Bottle sqlalchemy setup](https://github.com/iurisilvio/bottle-sqlalchemy/blob/master/examples/basic.py)
