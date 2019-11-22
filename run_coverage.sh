export COVERAGE_PROCESS_START=.coveragerc
per_project -a getlino inv cov
coverage combine
coverage report
coverage html -d htmlcov
