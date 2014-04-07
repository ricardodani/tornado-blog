run:
	@cd blog/ && python -vvv server.py

setup:
	@pip install -r requirements.txt

migration:
	@cd blog/ && alembic upgrade head

migration-test:
	@cd blog/ && alembic -c alembic_tests.ini upgrade head

test: migration-test
	@cd blog/ && python -m tornado.testing tests

recreate-dbs:
	@echo 'Droping (if exists) and creating `tornado_blog` db.'
	@mysql -u root -e "DROP DATABASE IF EXISTS tornado_blog; CREATE DATABASE IF NOT EXISTS tornado_blog"
	@echo 'Droping (if exists) and creating `test_tornado_blog` db.'
	@mysql -u root -e "DROP DATABASE IF EXISTS test_tornado_blog; CREATE DATABASE IF NOT EXISTS test_tornado_blog"
