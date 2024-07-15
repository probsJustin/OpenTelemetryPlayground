# OpenTelemetryPlayground

### Flask Application: 

To Build: 
````
docker build -t catfact-app . 
docker run -p 5000:5000 catfact-app
````

### Jaeger Information: 
Port Information
````
6831: Accepts Thrift over UDP, used by Jaeger agents.
5778: Provides an endpoint for fetching sampling strategies.
16686: Serves the Jaeger UI.
14268: For the HTTP collector.
14250: For the gRPC collector.
````

To Run: 
````
docker-compose up
````
To Access: 
````
http://localhost:16686
````


### Grafana: 

Ports: Exposes Grafana on port 3000, so you can access it at http://localhost:3000.
Environment: Sets up an admin password (change "yourpassword" to something secure) and disables sign-ups.
Volumes: Maps a volume for Grafana data to ensure data persists across container restarts.
Restart: Configures the container to restart unless manually stopped.

To Run: 
````
docker-compose up
````

To Access: 
```
Once the container is running, you can access Grafana by visiting http://localhost:3000 on your web browser.
The default username is admin, and the password will be what you set for GF_SECURITY_ADMIN_PASSWORD in the docker-compose file.```
```
### OpenTelemetry Collector: 

To Build and Run: 
```
docker build -t my-otel-collector .
docker run -p 4317:4317 -p 4318:4318 -p 55681:55681 my-otel-collector
```


