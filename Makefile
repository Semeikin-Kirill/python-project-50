gendiff:
	poetry run gendiff -h

lint:
	poetry run flake8 gendiff

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

test:
	poetry run pytest

selfcheck:
	poetry check

check: selfcheck test lint

install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

.PHONY: install build publish package-install gendiff lint test selfcheck test-coverage
