run:
	python -m src 

run-prod:
	python -m gunicorn src.__main__:server -b :80

docker-build:
	docker build --pull --rm -f "dockerfile" -t kamasdashboard:latest "."

docker-tag:
	docker tag kamasdashboard:latest clementraoul/dockerhub:kamasdashboard