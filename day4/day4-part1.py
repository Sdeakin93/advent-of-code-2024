def solve(input_str: str):
    xmas_count = 0
    string_list = input_str.splitlines()

    height_of_puzzle = len(string_list)
    width_of_puzzle = len(string_list[0])

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

    for y in range(height_of_puzzle):
        for x in range(width_of_puzzle):
            for yy, xx in directions:
                if 0 <= y + 3 * yy < height_of_puzzle and 0 <= x + 3 * xx < width_of_puzzle:
                    current_word = ''.join([string_list[y + i * yy][x + i * xx] for i in range(4)])
                    xmas_count += current_word == 'XMAS'

    return xmas_count

with open('day4-input.txt', 'r') as file:
    print("Number of xmas occurences:", solve(file.read()))
