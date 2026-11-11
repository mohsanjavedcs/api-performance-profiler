import requests, time, csv
from urllib.parse import urlparse

fast = "http://127.0.0.1:5000/fast"
delayed = "http://127.0.0.1:5000/delayed"

measurements = []

def store_measurements(url):
    for i in range(1000):
    
        start_time = time.perf_counter()
        response = requests.get(url, timeout=5)
        end_time = time.perf_counter()
        elapsed_time = (end_time - start_time) * 1000
        parsed_url = urlparse(url)
        measurement = {
            "request_number": i + 1,
            "endpoint": f"{parsed_url.path}",
            "response_time_ms": elapsed_time,
            "status_code": response.status_code
        }
        measurements.append(measurement)

store_measurements(fast)
store_measurements(delayed)

with open("measurements.csv", 'w', newline='') as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["request_number", "endpoint", "response_time_ms", "status_code"]
    )

    writer.writeheader()
    writer.writerows(measurements)