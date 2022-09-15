docker-compose-up:
	docker-compose up

run-test:
	docker-compose run --rm proyectofinalekchy sh -c "python manage.py test"

makemigrations:
	docker-compose run --rm proyectofinalekchy sh -c "python manage.py makemigrations"

migrate:
	docker-compose run --rm proyectofinalekchy sh -c "python manage.py makemigrations"

startproject:
	docker-compose run --rm proyectofinalekchy sh -c "django-admin startproject app ."

django-shell:
	docker-compose run --rm -it proyectofinalekchy sh -c "python manage.py shell"

docker-shell:
	docker-compose run --rm -it proyectofinalekchy sh


django-help:
	docker-compose run --rm -it proyectofinalekchy sh -c "python manage.py help"


django-graph:
	docker-compose run --rm -it proyectofinalekchy sh -c "python manage.py graph_models -a > proyectofinalekchy-schema.dot"
