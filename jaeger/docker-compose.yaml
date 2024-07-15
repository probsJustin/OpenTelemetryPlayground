version: '3'
services:
  jaeger:
    image: jaegertracing/all-in-one:latest
    container_name: jaeger
    ports:
      - "6831:6831/udp"  # For UDP Jaeger Thrift agents
      - "5778:5778"      # For managing sampling strategies
      - "16686:16686"    # For the Jaeger UI
      - "14268:14268"    # For HTTP collector
      - "14250:14250"    # For gRPC collector
    environment:
      COLLECTOR_ZIPKIN_HOST_PORT: ":9411"
    restart: on-failure
