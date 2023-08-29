import pandas as pd

# Load the lottery data from a CSV file (replace 'data.csv' with the actual file path)
data = pd.read_csv('data.csv')

# Assuming the numbers are represented in separate columns (e.g., 'Number 1', 'Number 2', ... 'Number N')
# You can adjust the column names according to your dataset.
number_columns = ['Number 1', 'Number 2', 'Number 3', 'Number 4', 'Number 5']

# Create an empty dictionary to store the frequency of each number
number_frequency = {}

# Iterate through each row of the data and count the occurrences of each number
for column in number_columns:
    numbers = data[column].tolist()
    for number in numbers:
        if pd.notnull(number):
            number_frequency[number] = number_frequency.get(number, 0) + 1

# Sort the numbers by their frequency in descending order
sorted_frequency = sorted(number_frequency.items(), key=lambda x: x[1], reverse=True)

# Print the results
for number, frequency in sorted_frequency:
    print(f"Number {number}: {frequency} occurrences")