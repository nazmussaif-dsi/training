### Running Postgres with local volume

`sudo mkdir -p /data/postgres`

`sudo docker run --name postgres -p 5432:5432 -v ~/data/postgres:/var/lib/postgresql/data -e POSTGRES_PASSWORD=j1nkal0p0ngl@ -e POSTGRES_USER=postgres -e POSTGRES_DB=lechuck  postgres:10`

### Running MySQL with local volume

`sudo mkdir -p /data/mysql`

`sudo docker run --name mysql --publish 3306:3306 -v ~/data/mysql:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -d mysql:5.7.27`