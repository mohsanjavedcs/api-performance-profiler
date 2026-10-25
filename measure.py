import requests, time

url = "http://127.0.0.1:5000/fast"

times = []

for _ in range(30):
    
    start_time = time.perf_counter()
    response = requests.get(url)
    end_time = time.perf_counter()
    elapsed_time = (end_time - start_time) * 1000
    times.append(elapsed_time)

print(f"Number of observations: {len(times)}, Maximum: {max(times)}, Minimum: {min(times)}")