tests:
	python -m pytest src -v -s

run:
	python -m src 

check-lint:
	python -m black src
	python -m isort src

run-prod:
	python -m gunicorn src.__main__:server -b :80

docker-build:
	docker build --pull --rm -f "dockerfile" -t kamasdashboard:latest "." --platform linux/amd64 -t ghcr.io/clementraoulastek/kamasdashboard:latest

docker-push:
	docker push ghcr.io/clementraoulastek/kamasdashboard:latest