### Create a new local volume
`sudo docker volume create lechuck_volume`
### View the volumes
`sudo docker volume ls`
### VIew the local volume in detail
`sudo docker volume inspect lechuck_volume`
### Start a swarm if not already started
`sudo docker swarm init --advertise-addr=10.0.0.110`
### Create a service mounting to the guybrush_node
`sudo docker service create --name guybrush_node --publish target=8080,published=8080 --replicas=3 --mount source=lechuck_volume,target=/usr/src/app/data/ dsinnovators/training:guybrush_node`
### VIew the services
`sudo docker service ps guybrush_node`
### Test the services
`curl -i http://10.0.0.110:8080`
### Stop the service
`sudo docker service rm guybrush_node`
### Remove the volume 
`sudo docker volume rm lechuck_volume`

