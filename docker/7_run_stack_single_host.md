# To run the docker swarm in the single host machine

### Login to docker hub
`sudo docker login`

### Init the swarm
`sudo docker swarm init`

### Deploy the stack
`sudo docker stack deploy -c docker-compose.yml threepwood`

### View stack status
`sudo docker service ls`

### View detailed stack status
`sudo docker service ps threepwood_guybrush_node --no-trunc`
`sudo docker service ps threepwood_rincewind_spring --no-trunc`

### Tear Down stack

`sudo docker stack rm threepwood`

### Leave the swarm
`sudo docker swarm leave --force`
