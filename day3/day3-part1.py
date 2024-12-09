import re

def count_mul(input_str):
    pattern = r"mul\(\d+,\s*\d+\)"  # Pattern to match "mul(int, int)"
    matches = re.findall(pattern, input_str)
    
    print("Matches:")
    for match in matches:
        print(match)
    
    return len(matches)

def split_and_multiply(match):
    # Extract the integers from the match
    numbers = re.findall(r'\d+', match)
    
    # Convert the extracted strings to integers
    num1 = int(numbers[0])
    num2 = int(numbers[1])
    
    # Multiply the two numbers
    result = num1 * num2
    
    return result

with open("day3-input.txt", "r") as input_file:
    input_data = input_file.read()
    
    mul_count = count_mul(input_data)
    
    sum_mul = sum(split_and_multiply(match) for match in re.findall(r"mul\(\d+,\s*\d+\)", input_data))
    
    print("Sum of all results:", sum_mul)