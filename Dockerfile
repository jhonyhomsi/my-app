FROM python:3.12-slim

# Install ping
RUN apt-get update \
 && apt-get install -y --no-install-recommends iputils-ping \
 && rm -rf /var/lib/apt/lists/*

# App
WORKDIR /app
COPY . /app

# Run your script (adjust filename if different)
ENTRYPOINT ["python", "/app/ping_gateway.py"]
