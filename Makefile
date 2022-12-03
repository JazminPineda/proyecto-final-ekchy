docker-compose-up:
	docker-compose up

run-test:
	docker-compose run --rm app sh -c "python manage.py test"

makemigrations:
	docker-compose run --rm app sh -c "python manage.py makemigrations"

migrate:
	docker-compose run --rm app sh -c "python manage.py makemigrations"

startproject:
	docker-compose run --rm app sh -c "django-admin startproject app ."

django-shell:
	docker-compose run --rm -it app sh -c "python manage.py shell"

docker-shell:
	docker-compose run --rm -it app sh


django-help:
	docker-compose run --rm -it app sh -c "python manage.py help"


django-graph:
	docker-compose run --rm -it app sh -c "python manage.py graph_models -a > app-schema.dot"
