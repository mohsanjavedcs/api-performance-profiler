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
            
print(f"length of fast responses: {len(fast_responses)}")
for resp in fast_responses:
    print(resp)
print(f"length of delayed responses: {len(delayed_responses)}")
for resp in delayed_responses:
    print(resp)