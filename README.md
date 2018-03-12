# Learning Graphql

Using Django (via docker) as a backend.

## Running

Make sure you have docker for Mac/PC/Linux installed...

```
docker-compose run web python manage.py migrate

docker-compose run web python manage.py createsuperuser
```
then...
```
docker-compose up
```
and browse to http://localhost:8000/admin

add some Students and Courses

then browse to http://localhost:8000/graphiql

and play with Graphql
