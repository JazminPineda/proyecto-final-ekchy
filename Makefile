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



