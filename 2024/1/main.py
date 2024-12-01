with open("input.txt") as input:
    lines = input.readlines()
    locations_by_group1 = [int(line.split()[0]) for line in lines]
    locations_by_group2 = [int(line.split()[1]) for line in lines]

    locations_by_group1.sort()
    locations_by_group2.sort()

    distance = 0
    for location_1, location_2 in zip(locations_by_group1, locations_by_group2):
        distance += abs(location_1 - location_2) 

    print(distance)

    location_2_repeats = {}
    for location in locations_by_group2:
        if location_2_repeats.get(location):
            location_2_repeats[location] += 1
        else:
            location_2_repeats[location] = 1
    
    similarity = 0

    for location in locations_by_group1:
        repeats = location_2_repeats.get(location)
        if repeats:
            similarity += location * repeats
    
    print(similarity)