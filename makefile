tests: # Run all the tests
tests:
	python -m pytest src -v -s

lint: # Run all the linters
lint:
	python -m header_context
	python -m isort . --profile black
	python -m black .
	python -m pylint src

# Run the server in development mode
run:
	python -m src 

run-prod: # Run the server in production mode
run-prod:
	python -m gunicorn src.__main__:server -b :80 --log-level=debug


docker-build: # Build the docker image for an amd64 architecture, and tag it for github container registry
docker-build:
	docker build . --tag ghcr.io/clementraoulastek/kamasdashboard:latest --platform linux/amd64


docker-push: # Push the docker image to github container registry
docker-push:
	docker push ghcr.io/clementraoulastek/kamasdashboard:latest

docs: # Create the documentation in html with sphinx
docs:
	@cd doc && echo "I'm in doc folder" && \
	make html