import re

with open('input.txt') as input:
    memory = input.read()
    pattern1 = r"mul\((-?\d+),(-?\d+)\)"
    matches = re.findall(pattern1, memory)
    result = sum(int(match[0])*int(match[1]) for match in matches)
    print(result)

    pattern2 = r"(mul\((-?\d+),(-?\d+)\)|do\(\)|don['’]t\(\))"
    matches = re.findall(pattern2, memory)
    do = True
    result = 0
    for match in matches:
        match match[0]:
            case value if "mul" in value:
                if do:
                    result += int(match[1]) * int(match[2])
            case value if "don't" in value:
                do = False
            case value if "do" in value:
                do = True
            case _:
                print("You shouldn't be here")
    print(result)