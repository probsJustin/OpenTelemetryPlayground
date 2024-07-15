# Use the official OpenTelemetry Collector image
FROM otel/opentelemetry-collector:latest

# Copy your custom configuration file into the container
COPY otel-config.yaml /etc/otel/config.yaml

# Set the config file environment variable to tell the collector which config to use
ENV OTEL_CONFIG_FILE=/etc/otel/config.yaml

# Expose ports used by the collector
EXPOSE 4317 55680 55681 4318 8888 9411

# Command to start the OpenTelemetry Collector
CMD ["/otelcol", "--config=${OTEL_CONFIG_FILE}"]
