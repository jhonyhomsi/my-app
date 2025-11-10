# Use Python 3.12 slim image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy Python script
COPY ping_gateway.py .

# Run script by default
CMD ["python", "ping_gateway.py"]
