def is_valid(list):  
    def is_sorted_ascending(list):
        return all(list[i] <= list[i+1] for i in range(len(list) - 1))

    def is_sorted_descending(list):
        return all(list[i] >= list[i+1] for i in range(len(list) - 1))
        
    def is_difference_valid(list):
        return all(1 <= abs(list[i] - list[i+1]) <= 3 for i in range(len(list) - 1))

    if (is_sorted_ascending(list) or is_sorted_descending(list)) and is_difference_valid(list):
        return True

    #find if sorted and difference is valid after removal of each item in the list
    for i in range(len(list)):        
        new_list = list[:i] + list[i+1:]
        if (is_sorted_ascending(new_list) or is_sorted_descending(new_list)) and is_difference_valid(new_list):
            return True
    return False

with open("input.txt") as input:
    lines = input.readlines()
    reports = [list(map(int, line.split())) for line in lines]
    safe = 0
    for report in reports:
        if is_valid(report):
            safe += 1
    print(safe)
    