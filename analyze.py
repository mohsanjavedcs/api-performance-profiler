import csv, math, statistics

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

fast_mean = sum(fast_responses) / len(fast_responses)
delayed_mean = sum(delayed_responses) / len(delayed_responses)

# print(f"Fast Endpoints mean: {fast_mean}")
# print(f"Delayed Endpoints mean: {delayed_mean}")

sorted_fast_endpoints = sorted(fast_responses)
sorted_delayed_endpoints = sorted(delayed_responses)

# fast_median = round((sorted_fast_endpoints[14] + sorted_fast_endpoints[15]) / 2, 2)
# delayed_median = round((sorted_delayed_endpoints[14] + sorted_delayed_endpoints[15]) / 2, 2)

fast_median = statistics.median(sorted_fast_endpoints)
delayed_median = statistics.median(sorted_delayed_endpoints)

# print(f"Fast Endpoints median: {fast_median}")
# print(f"Delayed Endpoints median: {delayed_median}")

fast_min = round(min(fast_responses), 2)
fast_max = round(max(fast_responses), 2)
fast_range = round(fast_max - fast_min, 2)
delayed_min = round(min(delayed_responses), 2)
delayed_max = round(max(delayed_responses), 2)
delayed_range = round(delayed_max - delayed_min, 2)

# print(f"Fast Endpoints Min: {fast_min}")
# print(f"Fast Endpoints Max: {fast_max}")
# print(f"Fast Endpoints Range: {fast_range}")
# print(f"Delayed Endpoints Min: {delayed_min}")
# print(f"Delayed Endpoints Max: {delayed_max}")
# print(f"Delayed Endpoints Range: {delayed_range}")

fast_squared_difference = [(x - fast_mean) ** 2 for x in fast_responses]
delayed_squared_difference = [(x - delayed_mean) ** 2 for x in delayed_responses]

fast_variance = sum(fast_squared_difference) / (len(fast_responses) - 1)
delayed_variance = sum(delayed_squared_difference) / (len(delayed_responses) - 1)

# print(f"Fast Endpoints Variance: {fast_variance:.2f}")
# print(f"Delayed Endpoints Variance: {delayed_variance:.2f}")

fast_std = math.sqrt(fast_variance)
delayed_std = math.sqrt(delayed_variance)

# print(f"Fast Endpoints Standard Deviation: {fast_std:.2f}")
# print(f"Delayed Endpoints Standard Deviation: {delayed_std:.2f}")

# fast_mid_idx = len(fast_responses) // 2
# delayed_mid_idx = len(delayed_responses) // 2

# fast_first_half = sorted_fast_endpoints[:fast_mid_idx]
# fast_second_half = sorted_fast_endpoints[fast_mid_idx:]
# delayed_first_half = sorted_delayed_endpoints[:delayed_mid_idx]
# delayed_second_half = sorted_delayed_endpoints[delayed_mid_idx:]

# fast_q1 = fast_first_half[7]
# fast_q3 = fast_second_half[7]

fast_quartiles = statistics.quantiles(fast_responses, n=4, method='inclusive')
fast_q1 = fast_quartiles[0]
fast_q3 = fast_quartiles[2]

# delayed_q1 = delayed_first_half[7]
# delayed_q3 = delayed_second_half[7]

delayed_quartiles = statistics.quantiles(delayed_responses, n=4, method='inclusive')
delayed_q1 = delayed_quartiles[0]
delayed_q3 = delayed_quartiles[2]

fast_iqr = fast_q3 - fast_q1
delayed_iqr = delayed_q3 - delayed_q1

# print(f"Fast Endpoints Q1: {fast_q1:.2f}")
# print(f"Fast Endpoints Q3: {fast_q3:.2f}")
# print(f"Fast Endpoints IQR: {fast_iqr:.2f}")
# print(f"Delayed Endpoints Q1: {delayed_q1:.2f}")
# print(f"Delayed Endpoints Q3: {delayed_q3:.2f}")
# print(f"Delayed Endpoints IQR: {delayed_iqr:.2f}")

fast_lb = fast_q1 - (1.5 * fast_iqr)
delayed_lb = delayed_q1 - (1.5 * delayed_iqr)

fast_ub = fast_q3 + (1.5 * fast_iqr)
delayed_ub = delayed_q3 + (1.5 * delayed_iqr)

# print(f"Fast Endpoints Lower Boundary: {fast_lb:.2f}")
# print(f"Fast Endpoints Upper Boundary: {fast_ub:.2f}")
# print(f"Delayed Endpoints Lower Boundary: {delayed_lb:.2f}")
# print(f"Delayed Endpoints Upper Boundary: {delayed_ub:.2f}")

fast_outliers = [
    x for x in fast_responses
    if x < fast_lb or x > fast_ub
    ]
delayed_outliers = [
    x for x in delayed_responses
    if x < delayed_lb or x > delayed_ub
    ]

fast_qd = fast_iqr / 2
delayed_qd = delayed_iqr / 2

# print(f"Fast Endpoints Quartile Deviation: {fast_qd:.2f}ms")
# print(f"Delayed Endpoints Quartile Deviation: {delayed_qd:.2f}ms")

fast_skewness_sum = sum(
    ((x - fast_mean) / fast_std) ** 3
    for x in fast_responses
)

delayed_skewness_sum = sum(
    ((x - delayed_mean) / delayed_std) ** 3
    for x in delayed_responses
)

fast_n = len(fast_responses)
delayed_n = len(delayed_responses)

fast_skewness = (fast_n / ((fast_n - 1) * (fast_n - 2))) * fast_skewness_sum
delayed_skewness = (delayed_n / ((delayed_n - 1) * (delayed_n - 2))) * delayed_skewness_sum

# print(f"Fast Endpoints Skewness: {fast_skewness:.2f}")
# print(f"Delayed Endpoints Skewness: {delayed_skewness:.2f}")

fast_ub_outliers = [
    x for x in fast_responses
    if x > fast_ub
    ]
delayed_ub_outliers = [
    x for x in delayed_responses
    if x > delayed_ub
    ]

std_threshold = (fast_std + delayed_std) / 2
outlier_threshold = math.ceil((len(fast_ub_outliers) + len(delayed_ub_outliers)) / 2)

fast_status = (
    "Unstable"
    if fast_std > std_threshold or len(fast_ub_outliers) > outlier_threshold
    else "Stable"
)

delayed_status = (
    "Unstable"
    if delayed_std > std_threshold or len(delayed_ub_outliers) > outlier_threshold
    else "Stable"
)

# print(f"Fast Endpoint Status: {fast_status}")
# print(f"Delayed Endpoint Status: {delayed_status}")

fast_outlier_percentage = (len(fast_outliers) / len(fast_responses)) * 100
delayed_outlier_percentage = (len(delayed_outliers) / len(delayed_responses)) * 100

# print(f"Fast Outlier Percentage: {fast_outlier_percentage:.2f}%")
# print(f"Delayed Outlier Percentage: {delayed_outlier_percentage:.2f}%")

