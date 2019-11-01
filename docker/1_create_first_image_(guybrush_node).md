# For First guybrush_node : Nodejs Application

### Building first guybrush_node
`sudo docker build -t guybrush_node guybrush_node/`

### Running first guybrush_node on port 8080
`sudo docker run --name guybrush_node -p 8080:8080 -d guybrush_node`

### Testing first guybrush_node
`curl -i localhost:8080`

### Viewing first guybrush_node run details
`sudo docker ps`

### Viewing first guybrush_node log
`sudo docker logs guybrush_node`

### Accessing the Running Instance
`docker exec -it guybrush_node /bin/bash`

### Login to docker
`sudo docker login`

### Tag the image
`sudo docker tag guybrush_node dsinnovators/training:guybrush_node`

### Push the image
`sudo docker push dsinnovators/training:guybrush_node`

### Run from any machine
`sudo docker run --name guybrush_node -p 8080:8080 dsinnovators/training:guybrush_node`

### Stopping Docker Run
`sudo docker stop guybrush_node`

### Removing Docker Container
`sudo docker rm guybrush_node`