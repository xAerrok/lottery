#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the lottery data from a CSV file (replace 'megamillions.csv' with the actual file path)
# Use 'date_format' instead of 'date_parser'
data = pd.read_csv('megamillions.csv', parse_dates=['date'], date_format='%m-%d-%y')

# Assuming the numbers are represented in separate columns (e.g., 'Number 1', 'Number 2', ... 'Number N')
# You can adjust the column names according to your dataset.
number_columns = ['a', 'b', 'c', 'd', 'e']

# Determine the maximum number present in the dataset
max_number = data[number_columns].max().max()

# Create a dictionary to store the frequency of each number
number_frequency = {number: 0 for number in range(1, max_number + 1)}

# Create a list to store the cumulative frequency for each number
cumulative_frequency = {number: [] for number in range(1, max_number + 1)}

# Calculate the start date for the previous 1 year
one_year_ago = data['date'].max() - pd.DateOffset(years=1)

# Iterate through each row of the data and calculate the weekly and cumulative frequencies
for _, row in data.iterrows():
    date = row['date']
    
    # Calculate the weekly frequency
    for column in number_columns:
        number = row[column]
        if pd.notnull(number):
            number = int(number)
            if 1 <= number <= max_number:  # Check if the number is within the valid range
                number_frequency[number] = number_frequency.get(number, 0) + 1

    # Calculate the cumulative frequency by month, quarter, and year
    for column in number_columns:
        number = row[column]
        if pd.notnull(number):
            number = int(number)
            if 1 <= number <= max_number:  # Check if the number is within the valid range
                cumulative_frequency[number].append((date, number_frequency[number]))

# Calculate the total number of draws in the previous 1 year
total_draws_1_year = data[data['date'] >= one_year_ago]['date'].count()

# Calculate the probability of each number occurring in the previous 1 year
number_probabilities = {number: freq / total_draws_1_year for number, freq in number_frequency.items()}

# Sort the numbers by their probability in descending order
sorted_probabilities = sorted(number_probabilities.items(), key=lambda x: x[1], reverse=True)

# Display the probabilities of each number occurring in the previous 1 year
for number, probability in sorted_probabilities:
    print(f"Number {number}: Probability = {probability:.6f}")

# ...

# ...

# Rest of the code (visualization, saving plots, etc.)
# ...

# Sort the numbers by their probability in descending order
sorted_probabilities = sorted(number_probabilities.items(), key=lambda x: x[1], reverse=True)

# Display the probabilities of each number occurring in the previous 1 year
for number, probability in sorted_probabilities:
    print(f"Number {number}: Probability = {probability:.6f}")

# Generate a bar chart for the probability of each number and save it to a file
number_values, probabilities = zip(*sorted_probabilities)
plt.figure(figsize=(12, 6))
plt.bar(number_values, probabilities, tick_label=number_values)
plt.xlabel('Number')
plt.ylabel('Probability')
plt.title('Probability of Each Number Occurring in the Previous 1 Year')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('number_probabilities.png')
plt.show()

# Save the most frequent numbers by week, month, quarter, and year to a file
with open('most_frequent_numbers.txt', 'w') as f:
    for freq_period in ['W', 'M', 'Q', 'Y']:
        f.write(f"Most frequent numbers by {freq_period}:\n")
        most_frequent_numbers_by_period = []

        for number in range(1, max_number + 1):
            date_freq = pd.DataFrame(cumulative_frequency[number], columns=['Date', 'Frequency'])
            date_freq.set_index('Date', inplace=True)
            date_freq.index = pd.to_datetime(date_freq.index)  # Convert the index to a datetime-like index

            if not date_freq.empty:
                date_freq = date_freq.sort_index(ascending=False)
                most_frequent_numbers = date_freq.resample(freq_period)['Frequency'].sum().nlargest(5)
                most_frequent_numbers_by_period.extend(list(zip([number] * len(most_frequent_numbers), most_frequent_numbers)))

        # Sort the numbers by frequency in descending order
        most_frequent_numbers_by_period.sort(key=lambda x: x[1], reverse=True)

        for i, (number, freq) in enumerate(most_frequent_numbers_by_period[:5]):
            f.write(f"{i+1}. Number {number}: {freq} occurrences\n")
        f.write('\n')

        # Create a data frame for each time period
        df = pd.DataFrame(most_frequent_numbers_by_period, columns=['Number', 'Frequency'])
        df.set_index('Number', inplace=True)

        # Plot the most frequent numbers for each time period in time series order
        plt.figure(figsize=(10, 4))
        plt.plot(df['Frequency'], marker='o')
        plt.xlabel('Number')
        plt.ylabel('Frequency')
        plt.title(f"Most frequent numbers by {freq_period}")
        plt.xticks(range(1, len(df.index) + 1), df.index, rotation=45)
        plt.tight_layout()

        # Save the plot to a file
        filename = f'most_frequent_numbers_by_{freq_period}.png'
        plt.savefig(filename)
        plt.close()

# ...

# ...

# Generate and save the cumulative frequency for each number by week, month, and year
for number in range(1, max_number + 1):
    date_freq = pd.DataFrame(cumulative_frequency[number], columns=['Date', 'Frequency'])
    date_freq.set_index('Date', inplace=True)
    date_freq.index = pd.to_datetime(date_freq.index)  # Convert the index to a datetime-like index

    plt.figure(figsize=(10, 4))
    plt.plot(date_freq.resample('W').sum(), label='Weekly')
    plt.plot(date_freq.resample('M').sum(), label='Monthly')
    plt.plot(date_freq.resample('Q').sum(), label='Quarterly')
    plt.plot(date_freq.resample('Y').sum(), label='Yearly')

    plt.title(f"Cumulative Frequency - Number {number}")
    plt.xlabel('Date')
    plt.ylabel('Frequency')
    plt.legend()
    plt.tight_layout()

    # Save the plot to a file
    filename = f'number_{number}_frequencies.png'
    plt.savefig(filename)
    plt.close()

# ...

