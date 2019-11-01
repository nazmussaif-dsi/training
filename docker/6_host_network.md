### Run a container attaching to the host network
`sudo docker run --network host  -dit --name guybrush_node guybrush_node`

### Test it
`curl http://localhost:8080/`