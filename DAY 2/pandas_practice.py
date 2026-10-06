import pandas as pd

# Load the dataset
df = pd.read_csv("dataset_folder/pandas_student_practice_100.csv")

print("First 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nInformation:")
df.info()

print("\nSelected first 3 columns:")
print(df.iloc[:, :3])

print("\nMissing values:")
print(df.isnull().sum())

print("\nNumber of rows:")
print(len(df))

print("\nRandom 5 rows:")
print(df.sample(5))

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nTop 5 students by Marks:")
print(df.nlargest(5, "Marks")[["Student_ID", "Name", "Marks"]])

print("\nBottom 5 students by Marks:")
print(df.nsmallest(5, "Marks")[["Student_ID", "Name", "Marks"]])