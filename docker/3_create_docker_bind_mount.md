# Create Bind mount with name and use it
### Create the data directory
`mkdir /tmp/data`
### Create the bind mount volume
`sudo docker volume create --driver local --opt o=bind --opt type=none --opt device=/tmp/data/ twoflower_bindmount`
### View the volumes
`sudo docker volume ls`
### View the bind mount volume in details
`sudo docker volume inspect twoflower_bindmount`
### Start the swarm if not already started
`sudo docker swarm init --advertise-addr=10.0.0.110`
### Run the services using the bind mount volume
`sudo docker service create --name guybrush_node --publish target=8080,published=8080 --replicas=3 --mount source=twoflower_bindmount,target=/usr/src/app/data/ dsinnovators/training:guybrush_node`
### View the services
`sudo docker service ps guybrush_node`
### Test the services
`curl -i http://10.0.0.110:8080`
### View the change in data directory
`ls /tmp/data/`

# Create bind mount on the fly 
### Run the node image with bind mount volume mounted
`sudo docker run --name guybrush_node --publish target=8080,published=8080 --mount type=bind,source=/tmp/data/,target=/usr/src/app/data/ dsinnovators/training:guybrush_node`
### Test the services
`curl -i http://10.0.0.110:8080`
### View the change in data directory
`ls /tmp/data/`