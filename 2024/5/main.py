def check_order(order, pages):
    for before, afterL in order.items():
        if before in pages:
            before_position = pages.index(before)
            for after in afterL:
                if after in pages and pages.index(after) < before_position:
                    return False
    return True

def fix_order(order, pages):
    changed = True
    while changed:
        changed = False
        for before, afterL in order.items():
            if before in pages:
                before_position = pages.index(before)
                for after in afterL:
                    if after in pages and pages.index(after) < before_position:
                        pages.remove(after)
                        pages.insert(before_position, after)
                        changed = True
                        print(f"Moved {after} before {before}: {pages}")
    return pages

with open("input.txt") as input:
    lines = input.readlines()

    rules = []
    pagesL = []
    get_rules = True
    for line in lines:
        line = line.strip()
        if get_rules:
            if line != "":
                rules.append(line)
            else:
                get_rules = False
        else:
            pagesL.append(line)
    pagesL = [list(map(int, pages.split(','))) for pages in pagesL]

    order = {}
    for rule in rules:
        before, after = rule.split('|')
        before, after = int(before), int(after)
        if order.get(before):
            order[before].append(after)
        else:
            order[before] = [after]

    mid_sum = 0
    mid_sum_corrected = 0
    for pages in pagesL:
        if check_order(order, pages):
            print(f"{pages}: Correct Order")
            mid_page = pages[len(pages) // 2]
            mid_sum += mid_page
        else:
            print(f"{pages}: Wrong Order")
            corrected_pages = fix_order(order, pages)
            print(f"Corrected Order: {corrected_pages}")
            mid_page_corrected = corrected_pages[len(corrected_pages) // 2]
            mid_sum_corrected += mid_page_corrected

    print("Sum of Correct Mid Pages:", mid_sum)
    print("Sum of Corrected Mid Pages:", mid_sum_corrected)