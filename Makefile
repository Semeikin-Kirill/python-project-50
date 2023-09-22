gendiff:
	poetry run gendiff -h

install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

.PHONY: install build publish package-install gendiff
