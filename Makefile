setup:
	@pip install -r requirements.txt

migration:
	@cd blog/ && alembic upgrade head

migration-test:
	@cd blog/ && alembic -c alembic_tests.ini upgrade head

test: migration-test
	@cd blog/ && python -m tornado.testing tests
