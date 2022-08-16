# flasklate
A dockerized flask template (`flasklate`) to be used as a bootstrap starting point for future projects.

***
## ✨ Dev
[http://localhost:8000/](http://localhost:8000/)
```shell 
docker-compose down -v && \
    docker system prune -af && \
    docker-compose up --build
```
```shell
# debug
docker-compose logs -f
```
```shell
#cleanup
docker-compose down -v && \
    docker system prune -af
```