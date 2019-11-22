export COVERAGE_PROCESS_START=.coveragerc
per_project -a getlino inv cov
coverage combine
coverage report -i
coverage html -i -d htmlcov
