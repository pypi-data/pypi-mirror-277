../../.tox/lint/bin/black --config ../../pyproject.toml . --diff --check
../../.tox/lint/bin/isort --settings-path ../../.isort.cfg . --diff --check-only
../../.tox/lint/bin/flake8 --config ../../.flake8 .
../../.tox/lint/bin/pylint src/oteltest
