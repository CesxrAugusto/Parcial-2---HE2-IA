import pandas as pd

training_data = pd.read_csv(r"adult\adult.data", header = None)
testing_data = pd.read_csv(r"adult\adult.test", header = None, skiprows = 1)

print(training_data)
print(testing_data)