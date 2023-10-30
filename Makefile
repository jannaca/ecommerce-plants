runserver:
	python manage.py runserver --settings=settings.local

makemigrations:
	python manage.py makemigrations --settings=settings.local

migrate:
	python manage.py migrate --settings=settings.local

superuser:
	python manage.py createsuperuser --settings=settings.local

loaddata:
	python manage.py loaddata category.json --settings=settings.local
	python manage.py loaddata products.json	--settings=settings.local

test:
	python manage.py test --settings=settings.local