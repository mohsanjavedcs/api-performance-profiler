import csv, statistics
import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore

fast_responses = []
delayed_responses = []

with open("measurements.csv", newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["endpoint"] == "/delayed":
            delayed_responses.append(float(row["response_time_ms"]))
        elif row["endpoint"] == "/fast":
            fast_responses.append(float(row["response_time_ms"]))

fast_mean = statistics.mean(fast_responses)
fast_median = statistics.median(sorted(fast_responses))
fast_std = statistics.stdev(fast_responses)
fast_requests = range(1, len(fast_responses) + 1)

delayed_mean = statistics.mean(delayed_responses)
delayed_median = statistics.median(sorted(delayed_responses))
delayed_std = statistics.stdev(delayed_responses)
delayed_requests = range(1, len(delayed_responses) + 1)


# Histplot

# fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# sns.histplot(fast_responses, bins=30, kde=True, ax=axes[0])
# axes[0].axvline(fast_mean, color='red', linestyle='--', linewidth=2, label=f'Mean:{fast_mean:.2f} ms')
# axes[0].axvline(fast_median, color='green', linestyle='--', linewidth=2, label=f'Median:{fast_mean:.2f} ms')
# axes[0].set_title("Fast Endpoint")
# axes[0].set_xlabel("Response Time (ms)")
# axes[0].set_ylabel("Frequency")
# axes[0].legend()

# sns.histplot(delayed_responses, bins=30, kde=True, ax=axes[1])
# axes[1].axvline(delayed_mean, color="red", linestyle="--", label=f"Mean: {delayed_mean:.2f} ms")
# axes[1].axvline(delayed_median, color="green", linestyle="--", label=f"Median: {delayed_median:.2f} ms")
# axes[1].set_title("Delayed Endpoint")
# axes[1].set_xlabel("Response Time (ms)")
# axes[1].set_ylabel("Frequency")
# axes[1].legend()

# plt.tight_layout()
# # plt.savefig("histogram.png", dpi=300)
# plt.show()

# Box Plot

# fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# # Fast Endpoints

# sns.boxplot(
#     y = fast_responses,
#     ax=axes[0],
#     width=0.4
# )

# axes[0].set_title("Fast Endpoint")
# axes[0].set_ylabel("Response Time (ms)")

# # Delayed Endpoints

# sns.boxplot(
#     y = delayed_responses,
#     ax=axes[1],
#     width=0.4
# )

# axes[1].set_title("Delayed Endpoint")
# axes[1].set_ylabel("Response Time (ms)")

# plt.suptitle("API Response Time Comparison")
# plt.tight_layout()
# # plt.savefig("boxplot.png", dpi=300)
# plt.show()

# Time Series Chart

# fig, axes = plt.subplots(2, 1, figsize=(13, 9))

# # Fast Endpoint

# axes[0].axhspan(
#     fast_mean - 2 * fast_std,
#     fast_mean + 2 * fast_std,
#     color="orange",
#     alpha=0.15,
#     label="Mean ± 2σ"
# )

# axes[0].axhspan(
#     fast_mean - fast_std,
#     fast_mean + fast_std,
#     color="green",
#     alpha=0.25,
#     label="Mean ± 1σ"
# )

# axes[0].plot(
#     fast_requests,
#     fast_responses,
#     label="Response Time"
# )

# axes[0].axhline(
#     fast_mean,
#     color="red",
#     linestyle="--",
#     label="Mean"
# )

# axes[0].set_title("Fast Endpoint")
# axes[0].set_xlabel("Request Number")
# axes[0].set_ylabel("Response Time (ms)")
# axes[0].legend()

# # Delayed Endpoint

# axes[1].axhspan(
#     delayed_mean - 2 * delayed_std,
#     delayed_mean + 2 * delayed_std,
#     color="orange",
#     alpha=0.15,
#     label="Mean ± 2σ"
# )

# axes[1].axhspan(
#     delayed_mean - delayed_std,
#     delayed_mean + delayed_std,
#     color="green",
#     alpha=0.25,
#     label="Mean ± 1σ"
# )

# axes[1].plot(
#     delayed_requests,
#     delayed_responses,
#     label="Response Time"
# )

# axes[1].axhline(
#     delayed_mean,
#     color="red",
#     linestyle="--",
#     label="Mean"
# )

# axes[1].set_title("Delayed Endpoint")
# axes[1].set_xlabel("Request Number")
# axes[1].set_ylabel("Response Time (ms)")
# axes[1].legend()

# plt.suptitle("API Response Time Over Requests")
# plt.tight_layout()
# # plt.savefig("timeseries.png", dpi=300)
# plt.show()

# The 5 Seconds Spike Experiment

spiked_fast_responses = fast_responses.copy()

spiked_fast_responses.append(5000)

spiked_mean = statistics.mean(spiked_fast_responses)
spiked_median = statistics.median(spiked_fast_responses)

print(f"Original Mean: {fast_mean:.2f}")
print(f"New Mean: {spiked_mean:.2f}")

print(f"Original Median: {fast_median:.2f}")
print(f"New Median: {spiked_median:.2f}")

