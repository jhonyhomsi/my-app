# Use a secure, small base with glibc and apt
FROM python:3.12-slim

# Install ping (iputils-ping) and keep the image lean
RUN apt-get update \
 && apt-get install -y --no-install-recommends iputils-ping \
 && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy application files
# If you have requirements.txt, copy and install before copying the rest
# (keeps layers cacheable). Since your current script has no deps, we skip.
COPY . /app

# Optional: run as non-root (comment out if you prefer root)
# USER 65532:65532

# Environment defaults (can be overridden at runtime)
# ENV GATEWAY=8.8.8.8

# Health check (will report unhealthy if the script would fail)
# Adjust timeout/interval as needed; this only verifies the binary exists.
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD command -v ping >/dev/null || exit 1

# Run your script
ENTRYPOINT ["python", "/app/ping_gateway.py"]
