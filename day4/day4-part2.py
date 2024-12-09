from collections import Counter

def solve(input_str: str):
    xmas_count = 0
    s = input_str.splitlines()

    for y in range(1, len(s) - 1):
        for x in range(1, len(s[0]) - 1):
            if s[y][x] == 'A':
                neighbors = s[y-1][x-1] + s[y-1][x+1] + s[y+1][x+1] + s[y+1][x-1]
                if Counter(neighbors)['S'] == 2 and Counter(neighbors)['M'] == 2 and s[y-1][x-1] != s[y+1][x+1]:
                    xmas_count += 1

    return xmas_count

with open('day4-input.txt', 'r') as file:
    input_text = file.read()
    print("Number of X-MAS occurrences:", solve(input_text))