import pandas as pd
import statistics
data = pd.read_csv("Admission_Predict.csv")
print(data.head(3))
print(statistics.mean(data['GRE Score']))

# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.distplot(data['GRE Score'])
# plt.show()

# print(statistics.mean(data['CGPA']))
# sns.distplot(data['CGPA'])
# plt.show()

#print(data.sample(5))

#print(data[100:103])