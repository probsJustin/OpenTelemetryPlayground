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
