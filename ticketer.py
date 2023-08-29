#!/usr/bin/env python
# coding: utf-8
import itertools
import csv
import random

def generate_combinations(source_set, num_combinations, combination_size):
    combinations = set()
    while len(combinations) < num_combinations:
        combination = tuple(sorted(random.sample(list(source_set), combination_size)))
        combinations.add(combination)
    return combinations

if __name__ == "__main__":
    try:
        file_path = "top14.csv"
        with open(file_path, "rt") as file:
            reader = csv.reader(file)
            input_numbers = next(reader)
            
            if len(input_numbers) != 14:
                raise ValueError("The CSV file should contain exactly 14 numbers.")

            source_set = set(map(int, input_numbers))
            
            num_combinations = 40
            combination_size = 5

            combinations = generate_combinations(source_set, num_combinations, combination_size)

            print("40 combinations of 5 numbers from the randomly selected set:")
            for idx, combination in enumerate(combinations, start=1):
                print(f"{idx}. {combination}")

    except FileNotFoundError:
        print("Error: File not found.")
    except ValueError as e:
        print(f"Error: {e}")
