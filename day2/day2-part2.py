def calculate_diff_and_direction(a, b):
    diff = abs(a - b)
    orientation = 'd' if a > b else 'i'
    return diff, orientation

def is_safe(levels):
    prev_orientation = None
    
    for i in range(len(levels) - 1):
        diff, orientation = calculate_diff_and_direction(levels[i], levels[i+1])

        if (prev_orientation is not None and orientation != prev_orientation) or not 0 < diff <= 3:
            return False

        prev_orientation = orientation

    return True

def solve(input_str):
    total_safe_reports = 0

    for line in input_str.splitlines():
        levels = [int(n) for n in line.split()]

        if is_safe(levels):
            total_safe_reports += 1
        else:
            for i in range(len(levels)):
                if is_safe(levels[:i] + levels[i+1:]):
                    total_safe_reports += 1
                    break

    return total_safe_reports

with open("day2-input.txt", "r") as input_file:
    input_data = input_file.read()
    safe_reports_count = solve(input_data)

print("Number of Safe Reports with Problem Dampener:", safe_reports_count)