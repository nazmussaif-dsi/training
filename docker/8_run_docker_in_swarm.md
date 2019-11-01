# To run the docker swarm in a network of machines

### Create first virtual machine 
`docker-machine create --driver virtualbox firstmachine`

### Create second virtual machine
`docker-machine create --driver virtualbox secondmachine`

### View the machines
`docker-machine ls`

### View first machine info
`docker-machine env firstmachine`

### Use first machine
`eval $(docker-machine env firstmachine)`

### Start docker swarm and make this machine the manager
`docker swarm init --advertise-addr=192.168.99.100`

### Use second machine
`eval $(docker-machine env secondmachine)`

### Join the docker swarm with token as a worker
`docker swarm join --token <SWARM TOKEN> 192.168.99.100:2377`

### Deploy the stack
`docker stack deploy -c docker-compose.yml threepwood`

### View the stack status
`docker stack ps threepwood`