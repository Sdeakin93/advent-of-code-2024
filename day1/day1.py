# part 1
with open('day1-input.txt', 'r') as file:
    lines = file.readlines()

list_a = []
list_b = []

for line in lines:
    numbers = line.split()
    list_a.append(int(numbers[0]))
    list_b.append(int(numbers[1]))

# sort them into lowest to highest order
list_a.sort()
list_b.sort()

# calculate the difference between list_a and list_b
difference = [abs(a - b) for a, b in zip(list_a, list_b)]

# calculate the sum of the difference
total_difference = sum(difference)

print("Total Difference:", total_difference)
# Total Difference: 1651298

# part 2
# Calculate the similarity score
total_similarity_score = 0

for number in list_a:
    total_appearances = list_b.count(number)
    individual_similarity_score = number * total_appearances
    total_similarity_score += individual_similarity_score

print("Total Similarity Score:", total_similarity_score)
# Total Similarity Score: 21306195