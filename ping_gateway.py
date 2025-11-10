import os
import subprocess
from datetime import datetime

def timestamp():
    return datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

# Use the GATEWAY environment variable
gateway = os.getenv("GATEWAY")

if not gateway:
    print(f"{timestamp()} No gateway provided. Please set the GATEWAY environment variable.")
    exit(1)

# Ping the gateway
result = subprocess.run(
    ["ping", "-c", "1", gateway],
    capture_output=True,
    text=True
)

if result.returncode == 0:
    print(f"{timestamp()} {gateway} is reachable ✅")
else:
    print(f"{timestamp()} {gateway} is not reachable ❌")
