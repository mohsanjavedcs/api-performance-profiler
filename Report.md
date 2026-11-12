# Backend API Latency and Performance Profiling

## 1. Introduction

The purpose of this project is to analyze the response-time performance of backend API endpoints using statistical methods.

An API (Application Programming Interface) allows different software applications to communicate with each other. When a client sends a request to an API, the time taken by the server to respond is called response time or latency.

In this project, two local Flask API endpoints were created: a fast endpoint and a delayed endpoint. Their response times were measured and analyzed using statistical techniques to understand their performance, consistency, variability, and unusual response-time observations.

## 2. Objectives

The main objectives of this project are:

- To create local API endpoints using Flask.
- To measure the response times of 1,000 requests for each endpoint.
- To store the measurements in a CSV file.
- To calculate statistical measures such as mean, median, variance, standard deviation, quartiles, IQR, quartile deviation, and skewness.
- To identify unusual response times using the IQR method.
- To classify endpoints as stable or unstable based on statistical thresholds.
- To visualize response-time distributions and behavior.
- To demonstrate the effect of an extreme observation on mean and median.

## 3. Tools and Technologies

The following tools and libraries were used:

- **Python:** Main programming language.
- **Flask:** Used to create the local API endpoints.
- **Requests:** Used to send HTTP requests and measure response times.
- **CSV:** Used to store collected measurements.
- **Statistics and Math:** Used for statistical calculations.
- **Matplotlib:** Used to create graphs.
- **Seaborn:** Used for statistical visualizations.

## 4. Methodology

### 4.1 Creating API Endpoints

Two Flask endpoints were created.

**Fast Endpoint (/fast):**

This endpoint returns a response without introducing any intentional delay.

**Delayed Endpoint (/delayed):**

This endpoint introduces a random delay in approximately 50% of requests. The delay duration ranges from 0.01 to 0.3 seconds.

This allows us to compare an endpoint without intentional delays against one with deliberately introduced variability.

### 4.2 Collecting Response-Time Measurements

A Python measurement script was created using the Requests library.

It sends 1,000 requests to each endpoint and measures the time taken for each HTTP response.

The collected measurements include:

- Request number
- Endpoint name
- Response time in milliseconds
- HTTP status code

A total of 2,000 measurements were collected and stored in `measurements.csv`.

### 4.3 Statistical Analysis

The collected measurements were divided into two datasets, one for each endpoint.

The following statistical measures were calculated:

- Mean and median
- Minimum, maximum, and range
- Variance and standard deviation
- First and third quartiles
- Interquartile range (IQR)
- Quartile deviation
- Skewness
- Outlier boundaries and outlier percentages

## 5. Statistical Results

The following table summarizes the calculated results.

| Statistical Measure | Fast | Delayed |
|---|---:|---:|
| Mean (ms) | 8.65 | 80.14 |
| Median (ms) | 6.74 | 21.79 |
| Minimum (ms) | 5.27 | 5.38 |
| Maximum (ms) | 220.29 | 342.25 |
| Range (ms) | 215.02 | 336.87 |
| Variance (ms²) | 109.97 | 9,127.09 |
| Standard deviation (ms) | 10.49 | 95.54 |
| Q1 (ms) | 6.16 | 7.04 |
| Q3 (ms) | 7.95 | 145.40 |
| IQR (ms) | 1.79 | 138.36 |
| Quartile deviation (ms) | 0.89 | 69.18 |
| Skewness | 13.12 | 1.04 |
| Outlier percentage | 9.40% | 0.00% |

### 5.1 Mean and Median Analysis

The fast endpoint has a mean response time of 8.65 ms and a median of 6.74 ms. The delayed endpoint has a mean of 80.14 ms and a median of 21.79 ms.

The delayed endpoint has a considerably higher average response time because its intentionally introduced delays increase the response times of many requests.

In both datasets, the mean is greater than the median. This indicates that higher response-time observations are pulling the averages upward.

### 5.2 Variance and Standard Deviation Analysis

The fast endpoint has a standard deviation of 10.49 ms, whereas the delayed endpoint has a standard deviation of 95.54 ms.

This indicates that the delayed endpoint has substantially greater variability.

The result is consistent with the endpoint's implementation, which introduces random sleep delays into approximately half of its requests.

The fast endpoint generally has more concentrated response times, although it also experiences occasional unusually slow requests.

### 5.3 Quartile and IQR Analysis

The fast endpoint has an IQR of 1.79 ms, compared with 138.36 ms for the delayed endpoint.

The small IQR indicates that the middle 50% of fast endpoint measurements are concentrated within a narrow range.

The much larger IQR of the delayed endpoint indicates that its middle 50% of observations are spread across a considerably wider interval.

This confirms the difference in consistency between the two endpoints.

### 5.4 Skewness Analysis

The fast endpoint has a skewness of 13.12, indicating extremely strong positive skewness. Most observations are concentrated around relatively low response times, while a smaller number of unusually high measurements create a long right tail.

The delayed endpoint has a skewness of 1.04, indicating positive skewness as well, but to a lesser degree.

These results demonstrate that both distributions are positively skewed, with the fast endpoint showing much greater asymmetry.

### 5.5 Outlier Analysis

Outliers were identified using the 1.5 × IQR method.

The fast endpoint has an upper boundary of 10.63 ms and a lower boundary of 3.48 ms. Its outlier percentage is 9.40%, meaning that 94 out of 1,000 measurements were classified as outliers.

The delayed endpoint has an upper boundary of 352.94 ms and a lower boundary of -200.50 ms. Its maximum observation is 342.25 ms, which is below the upper boundary. Therefore, no observations were classified as outliers.

Although the delayed endpoint has no IQR-based outliers, it still has considerably greater variability. This is because its IQR is already very large, resulting in wider outlier boundaries.

## 6. Endpoint Stability Classification

The endpoints were classified as stable or unstable using two dataset-relative thresholds:

1. Whether the standard deviation exceeds the calculated standard deviation threshold.
2. Whether the number of upper-bound outliers exceeds the calculated outlier threshold.

The calculated standard deviation threshold was 53.015 ms, and the upper-outlier count threshold was 47.

**Fast Endpoint: Unstable**

Its standard deviation is below the threshold, but its 94 upper-bound outliers exceed the outlier threshold.

**Delayed Endpoint: Unstable**

Its standard deviation exceeds the threshold, even though it has no upper-bound outliers.

Therefore, both endpoints were classified as unstable under the project's chosen classification rule, but for different statistical reasons.

## 7. Graphical Representations

Three types of visualizations were created to understand the response-time behavior.

### 7.1 Histogram with KDE

A histogram with a Kernel Density Estimation (KDE) curve was created for each endpoint.

The histogram displays the frequency of response times within different intervals, while the KDE curve provides a smooth representation of the distribution.

Vertical lines represent the mean and median.

The visualizations show that the fast endpoint has most of its observations concentrated near lower response times, with a long right tail. The delayed endpoint has a much wider distribution due to the intentionally introduced delays.

### 7.2 Box Plot

Box plots were created to compare the distributions of both endpoints.

They display the median, first quartile, third quartile, interquartile range, whiskers, and outliers.

The fast endpoint has a narrow box and several upper outliers. The delayed endpoint has a much larger box, demonstrating its greater variability.

Separate subplots were used so that each endpoint could be examined with its own vertical axis scale.

### 7.3 Time-Series Chart

Time-series line charts were created to show how response times change across the 1,000 requests.

The charts include:

- A line representing individual response times.
- A horizontal line representing the mean.
- Shaded regions representing mean ± 1 standard deviation.
- Shaded regions representing mean ± 2 standard deviations.

The fast endpoint generally shows low response times with occasional spikes. The delayed endpoint shows frequent fluctuations because of its random delays.

The charts help identify changes and unusual spikes across the sequence of requests.

## 8. Extreme Value Experiment: 5-Second Spike

An additional experiment was performed to demonstrate the effect of an extreme observation on the mean and median.

The original fast endpoint dataset was copied, and an artificial response time of 5,000 ms (5 seconds) was added.

The results were:

| Statistic | Before | After |
|---|---:|---:|
| Mean (ms) | 8.65 | 13.64 |
| Median (ms) | 6.74 | 6.74 |

The mean increased by approximately 57.7% after adding only one extreme observation.

However, the median remained unchanged.

This demonstrates that the mean is sensitive to extreme values, while the median is relatively resistant to them.

The experiment also highlights why both measures are useful when analyzing API response times.

## 9. Conclusion

The project successfully demonstrated how statistical methods can be used to analyze backend API performance.

The fast endpoint generally produced lower response times and had a much smaller interquartile range and standard deviation. However, it experienced occasional extreme slowdowns, resulting in high positive skewness and a 9.40% outlier percentage.

The delayed endpoint had a much higher average response time and substantially greater variability due to the intentionally introduced random delays. Although it had no observations classified as IQR-based outliers, its large standard deviation demonstrated that its response times were widely spread.

Both endpoints were classified as unstable according to the project's chosen statistical thresholds.

The three visualizations provided different perspectives on response-time behavior, while the 5-second spike experiment demonstrated the sensitivity of the mean to extreme observations.

Overall, the project shows that API performance cannot be understood through average response time alone. Measures of variability, distribution, skewness, and outliers are also important for evaluating performance and consistency.