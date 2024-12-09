def parse_input(input_str):
    rules = []
    updates = []
    is_rules_section = True

    for line in input_str.splitlines():
        if not line:
            is_rules_section = False
            continue

        if is_rules_section:
            rules.append(line)
        else:
            updates.append(list(map(int, line.split(','))))

    return rules, updates

def check_order(page, rules, update):
    for rule in rules:
        x, y = map(int, rule.split('|'))
        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False
    return True

def find_middle_page(update):
    return update[len(update) // 2]

def find_sum_of_middle_pages(input_str):
    rules, updates = parse_input(input_str)
    correct_updates = []

    for update in updates:
        if check_order(1, rules, update):
            correct_updates.append(update)

    middle_pages = [find_middle_page(update) for update in correct_updates]
    return sum(middle_pages)

with open('day5-input.txt', 'r') as file:
    input_text = file.read()
    print("Sum of middle pages from correctly-ordered updates:", find_sum_of_middle_pages(input_text))