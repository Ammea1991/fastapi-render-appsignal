
compose_local = docker-compose -f ./docker-compose.yml


start:
	${compose_local} up -d
	
stop:
	${compose_local} stop

down:
	${compose_local} down

start_rebuild:
	${compose_local} up -d --build
