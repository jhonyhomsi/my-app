import os
import subprocess
import socket
from datetime import datetime

def get_default_gateway():
    """Return the default gateway IP"""
    route = subprocess.run("ip route | grep default", shell=True, capture_output=True, text=True)
    if route.returncode != 0 or not route.stdout.strip():
        return None
    return route.stdout.strip().split()[2]

def ping(host):
    """Ping the host once and return True if reachable"""
    result = subprocess.run(f"ping -c 1 -W 1 {host}", shell=True)
    return result.returncode == 0

def main():
    gateway = get_default_gateway()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if not gateway:
        print(f"[{timestamp}] No default gateway found")
        return

    if ping(gateway):
        print(f"[{timestamp}] Default gateway {gateway} is reachable ✅")
    else:
        print(f"[{timestamp}] Default gateway {gateway} is DOWN ❌")

if __name__ == "__main__":
    main()
