import csv

fast_responses = []
delayed_responses = []

with open("measurements.csv", newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["endpoint"] == "/delayed":
            delayed_responses.append(float(row["response_time_ms"]))
        elif row["endpoint"] == "/fast":
            fast_responses.append(float(row["response_time_ms"]))
            
# print(f"length of fast responses: {len(fast_responses)}")
# for resp in fast_responses:
#     print(resp)
# print(f"length of delayed responses: {len(delayed_responses)}")
# for resp in delayed_responses:
#     print(resp)

fast_mean = round(sum(fast_responses) / len(fast_responses), 2)
delayed_mean = round(sum(delayed_responses) / len(delayed_responses), 2)

# print(f"Fast Endpoints mean: {fast_mean}")
# print(f"Delayed Endpoints mean: {delayed_mean}")

sorted_fast_endpoints = sorted(fast_responses)
sorted_delayed_endpoints = sorted(delayed_responses)

fast_median = round((sorted_fast_endpoints[14] + sorted_fast_endpoints[15]) / 2, 2)
delayed_median = round((sorted_delayed_endpoints[14] + sorted_delayed_endpoints[15]) / 2, 2)

# print(f"Fast Endpoints median: {fast_median}")
# print(f"Delayed Endpoints median: {delayed_median}")

fast_min = round(min(fast_responses), 2)
fast_max = round(max(fast_responses), 2)
fast_range = round(fast_max - fast_min, 2)
delayed_min = round(min(delayed_responses), 2)
delayed_max = round(max(delayed_responses), 2)
delayed_range = round(delayed_max - delayed_min, 2)

print(f"Fast Endpoints Min: {fast_min}")
print(f"Fast Endpoints Max: {fast_max}")
print(f"Fast Endpoints Range: {fast_range}")
print(f"Delayed Endpoints Min: {delayed_min}")
print(f"Delayed Endpoints Max: {delayed_max}")
print(f"Delayed Endpoints Range: {delayed_range}")