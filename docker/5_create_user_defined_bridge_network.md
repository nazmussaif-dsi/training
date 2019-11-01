### Create a user defined bridge network
`sudo docker network create --driver bridge threepwood_bridge`
### View newly created bridge network
`sudo docker network inspect threepwood_bridge`
### Run a container attaching to the bridge network
`sudo docker run --network threepwood_bridge  -dit --name guybrush_node guybrush_node`
### Run a container then attach to the bridge network
`sudo docker run -dit --name rincewind_spring rincewind_spring`

`sudo docker network connect threepwood_bridge spring`
### Log into spring container and ping guybrush_node
`sudo docker exec -it rincewind_spring /bin/bash`

`curl -i http://localhost:8080/`

`ping guybrush_node`

`exit`
### Log into guybrush_node container and ping spring
`sudo docker exec -it guybrush_node /bin/bash`

`curl -i http://localhost:8080/`

`ping rincewind_spring`

`exit`
### Detach the containers from the network
`sudo docker network disconnect threepwood_bridge guybrush_node`

`sudo docker network disconnect threepwood_bridge rincewind_spring`
