run:
	python -m src 

docker-build:
	docker build --pull --rm -f "dockerfile" -t kamasdashboard:latest "." 