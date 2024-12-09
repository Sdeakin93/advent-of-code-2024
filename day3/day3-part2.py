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

def calculate_sum(input_str):
    mul_enabled = True
    sum_mul = 0
    
    for match in re.findall(r"do\(\)|don't\(\)|mul\(\d+,\s*\d+\)", input_str):
        if "mul(" in match:
            if mul_enabled:
                sum_mul += split_and_multiply(match)
        elif "do()" in match:
            mul_enabled = True
        elif "don't()" in match:
            mul_enabled = False
    
    return sum_mul

with open("day3-input.txt", "r") as input_file:
    input_data = input_file.read()
    
    mul_count = count_mul(input_data)
    
    sum_mul_enabled = calculate_sum(input_data)
    
    print("Sum of enabled multiplications:", sum_mul_enabled)