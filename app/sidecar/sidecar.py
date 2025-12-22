import time
import requests

while True:
    try:
        r = requests.get("http://localhost:8000/info", timeout=2)
        print(f"[SIDECAR] backend responded: {r.status_code} {r.text}")
    except Exception as e:
        print(f"[SIDECAR] error talking to backend: {e}")

    time.sleep(5)
