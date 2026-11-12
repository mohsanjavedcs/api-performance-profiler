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

delayed_mean = statistics.mean(delayed_responses)
delayed_median = statistics.median(sorted(delayed_responses))

fig, axes = plt.subplots(1, 2, figsize=(13, 5))

sns.histplot(fast_responses, bins=30, kde=True, ax=axes[0])
axes[0].axvline(fast_mean, color='red', linestyle='--', linewidth=2, label=f'Mean:{fast_mean:.2f} ms')
axes[0].axvline(fast_median, color='green', linestyle='--', linewidth=2, label=f'Median:{fast_mean:.2f} ms')
axes[0].set_title("Fast Endpoint")
axes[0].set_xlabel("Response Time (ms)")
axes[0].set_ylabel("Frequency")
axes[0].legend()

sns.histplot(delayed_responses, bins=30, kde=True, ax=axes[1])
axes[1].axvline(delayed_mean, color="red", linestyle="--", label=f"Mean: {delayed_mean:.2f} ms")
axes[1].axvline(delayed_median, color="green", linestyle="--", label=f"Median: {delayed_median:.2f} ms")
axes[1].set_title("Delayed Endpoint")
axes[1].set_xlabel("Response Time (ms)")
axes[1].set_ylabel("Frequency")
axes[1].legend()

plt.tight_layout()
plt.savefig("histogram.png", dpi=300)
plt.show()