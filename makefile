tests:
	python -m pytest src -v -s

run:
	python -m src 

lint:
	python -m isort . --profile black
	python -m black .

run-prod:
	python -m gunicorn src.__main__:server -b :80 --log-level=debug

docker-build:
	docker build . --tag ghcr.io/clementraoulastek/kamasdashboard:latest --platform linux/amd64

docker-push:
	docker push ghcr.io/clementraoulastek/kamasdashboard:latest