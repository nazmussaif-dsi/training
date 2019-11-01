# For First guybrush_node : Nodejs Application

### Building first guybrush_node
`sudo docker build -t rincewind_spring rincewind_spring/`

### Running first guybrush_node on port 8080
`sudo docker run --name rincewind_spring -p 8080:8080 -d rincewind_spring`

### Testing first guybrush_node
`curl -i localhost:8080`

### Viewing first guybrush_node run details
`sudo docker ps`

### Viewing first guybrush_node log
`sudo docker logs rincewind_spring`

### Accessing the Running Instance
`sudo docker exec -it rincewind_spring /bin/bash`

### Login to docker
`sudo docker login`

### Tag the image
`sudo docker tag rincewind_spring dsinnovators/training:rincewind_spring`

### Push the image
`sudo docker push dsinnovators/training:rincewind_spring`

### Run from any machine
`sudo docker run --name rincewind_spring -p 8080:8080 -d dsinnovators/training:rincewind_spring`

### Stopping Docker Run
`sudo docker stop rincewind_spring`

### Removing Docker Container
`sudo docker rm rincewind_spring`