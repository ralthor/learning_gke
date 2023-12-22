.PHONY: build run stop rm restart

build: 
	docker-compose build

run-docker:
	docker run -d -p 5000:80 --name flask_app my_flask_app

up:
	docker-compose up -d

up-build:
	docker-compose up -d --build

up-log:
	docker-compose up

stop-docker:
	docker stop flask_app

down:
	docker-compose down

rm-docker:
	docker rm flask_app

restart-docker: stop-docker rm-docker run-docker

restart: down up-build

status: 
	docker ps -a | grep flask_app; docker-compose ps