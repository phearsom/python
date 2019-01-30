import statistics
# Check out docs at:
#    https://docs.python.org/3/library/statistics.html

data = [31975, 219, 7, 789, 7, 3, 57, 4, 92, 0, 5, 47, 645, 518, 26, 711, 1212, 662, 4, 26, 10, 13, 15, 21, 17, 123, 643, 1, 95, 20, 256, 2048, 1116, 5, 6, 1, 52, 6, 931, 83, 7, 9, 80, 99, 136, 18, 24, 14, 123, 5]
print("Mean", statistics.mean(data))
print("Median", statistics.median(data))
try:
	print("Mode", statistics.mode(data))
except statistics.StatisticsError:
	print("No unique mode.") 
print("Standard deviation:", statistics.stdev(data))
print("Variance:", statistics.variance(data))

odd_data = [4, 7, 3, 9, 12]
even_data = [4, 7, 3, 9, 12, 2]
print(odd_data)
print(even_data)
print("Median odd data", statistics.median(odd_data))
print("Median even data", statistics.median(even_data))
print("Median low of even data", statistics.median_low(even_data))
print("Median high of even data", statistics.median_high(even_data))
print("Standard deviation:", statistics.stdev(odd_data))
print("Variance:", statistics.variance(odd_data))

# Simple plot to look for outliers
import seaborn as sns
import matplotlib.pyplot as plt
sns.boxplot(x=even_data)
plt.show()
sns.boxplot(x=data)
plt.show()

