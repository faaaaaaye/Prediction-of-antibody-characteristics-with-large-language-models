import json
import re


with open('answer.txt', 'r', encoding='utf-8') as file:
    answer_lines = file.readlines()
    answer_column = [line.split()[2] for line in answer_lines]  # Extract the third column

# Read the first column of result.txt (excluding the last line)
with open('results.txt', 'r', encoding='utf-8') as file:
    result_lines = file.readlines()
    result_column = [line.split()[0] for line in result_lines]  # Extract the first column

# Calculate the percentage of identical values
total_comparisons = min(len(answer_column), len(result_column))
same_count = sum(1 for a, r in zip(answer_column, result_column) if a == r)

percentage = (same_count / total_comparisons) * 100 if total_comparisons > 0 else 0

with open('results.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()  # Read all lines
    last_line = lines[-1].strip() if lines else None  # Get the last line and remove line breaks

# Write the content into the compare.txt file.
with open('compare.txt', 'a', encoding='utf-8') as file:
    file.write(f"correct percentage: {percentage:.2f}%\n")
    file.write(last_line + '\n')

print("Task completed. Data has been written to the appropriate file.")
