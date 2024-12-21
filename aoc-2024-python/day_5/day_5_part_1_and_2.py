with open("input", "r") as file:
    lines = file.readlines()

empty_line_idx = 0
for line in lines:
    if line == "\n":
        empty_line_idx = lines.index(line)

pages_ordering_rules_str = lines[:empty_line_idx]
updates_str = lines[empty_line_idx + 1 :]


pages_ordering_rules_list = []
for rule in pages_ordering_rules_str:
    rule = rule.strip().split("|")
    pages_ordering_rules_list.append((int(rule[0]), int(rule[1])))

# print(pages_ordering_rules_dict)
updates_list = []
for update_str in updates_str:
    update = [int(x) for x in update_str.strip().split(",")]
    updates_list.append(update)

# print(updates_list)


def pages_that_should_be_before(page: int) -> set:
    pages = set()
    for rule in pages_ordering_rules_list:
        if rule[1] == page:
            pages.add(rule[0])
    return pages


def pages_that_should_be_after(page: int) -> set:
    pages = set()
    for rule in pages_ordering_rules_list:
        if rule[0] == page:
            pages.add(rule[1])
    return pages


def middle_number(pages: list) -> int:
    middle_idx = len(pages) // 2
    return pages[middle_idx]


sum = 0
inccorect_updates = []

def get_wrong_pages(update, i, page):
    update_set = set(update)
    pages_that_should_be_before_set = pages_that_should_be_before(page) & update_set

    pages_before = set(update[:i])

    wrong_pages = pages_that_should_be_before_set - pages_before
    return wrong_pages



for update in updates_list:

    is_good = True
    for i, page in enumerate(update):

        wrong_pages = get_wrong_pages(update, i, page)
        
        if len(wrong_pages) > 0:
            is_good = False
            inccorect_updates.append(update)
            break

    if is_good:

        sum += middle_number(update)

print(f"part 1, {sum}")

def fix_order(update, i, wrong_pages) -> list:
    for wrong_page in wrong_pages:
        idx_wrong = update.index(wrong_page)
        idx_current = i
            # print(f" index of wrong page: {idx_wrong}")
            # print(f" index of current page: {idx_current}")
        update.pop(idx_wrong)
        update.insert(idx_current, wrong_page)

    return update

sum = 0
for update in inccorect_updates:
    update_set = set(update)
    is_good = False
    while not is_good:
        for i, page in enumerate(update):
            # print("")
            # print(f"page: {page}")
            is_good = True
            wrong_pages = get_wrong_pages(update, i, page)
            # print(f"Wrong pages: {wrong_pages}")
            if len(wrong_pages) > 0:
                update = fix_order(update, i, wrong_pages)
                is_good = False
                break
    
    sum +=middle_number(update)

print(f"part 2, {sum}")
