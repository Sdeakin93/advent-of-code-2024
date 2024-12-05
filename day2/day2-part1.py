def calculate_diff_and_direction(a, b):
    diff = abs(a - b)
    direction = 'd' if a > b else 'i'  # 'd' for decreasing, 'i' for increasing
    return diff, direction

def count_safe_reports(input_str):
    total_safe_reports = 0

    for line in input_str.splitlines():
        levels = [int(n) for n in line.split()]
        is_safe = True
        prev_direction = None

        for i in range(len(levels) - 1):
            diff, direction = calculate_diff_and_direction(levels[i], levels[i+1])

            if (prev_direction is not None and direction != prev_direction) or not 0 < diff <= 3:
                is_safe = False
                break

            prev_direction = direction

        if is_safe:
            total_safe_reports += 1

    return total_safe_reports

with open("day2-input.txt", "r") as input_file:
    input_data = input_file.read()
    safe_reports_count = count_safe_reports(input_data)

print("Number of Safe Reports:", safe_reports_count)