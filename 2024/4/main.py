import re

def diagonals(matrix):
    h, w = len(matrix), len(matrix[0])
    return [[matrix[h - p + q - 1][q]
            for q in range(max(p-h+1, 0), min(p+1, w))]
            for p in range(h + w - 1)]


def antidiagonals(matrix):
    h, w = len(matrix), len(matrix[0])
    return [[matrix[p - q][q]
            for q in range(max(p-h+1,0), min(p+1, w))]
            for p in range(h + w - 1)]

def subgrids(matrix, size=3):
    rows = len(matrix)
    cols = len(matrix[0])
    subgrids = []

    for i in range(rows - size + 1):
        for j in range(cols - size + 1):
            subgrid = [row[j:j+size] for row in matrix[i:i+size]]
            subgrids.append(subgrid)
    
    return subgrids

def count_pattern(pattern, puzzle):
    return sum(len(re.findall(pattern, line)) for line in puzzle) + sum(len(re.findall(pattern, line[::-1])) for line in puzzle)

with open("input.txt") as input:
    lines = input.readlines()
    
    puzzle = [list(item[:-1]) if item[-1] == '\n' else list(item) for item in lines]
    puzzle_T = [list(row) for row in zip(*puzzle)]
    puzzle_diagonals = diagonals(puzzle)
    puzzle_antidiagonals = antidiagonals(puzzle)

    straight = ["".join(line) for line in puzzle]
    transposed = ["".join(line) for line in puzzle_T]
    diagonals = ["".join(line) for line in puzzle_diagonals]
    antidiagonals = ["".join(line) for line in puzzle_antidiagonals]

    pattern = "XMAS"
    match = 0

    ways = [straight, transposed, diagonals, antidiagonals]
    for way in ways:
        match += count_pattern(pattern, way)
    
    print(match)

    match = 0
    grids = subgrids(puzzle, size=3)
    for grid in grids:
        diagonal = grid[0][0] + grid[1][1] + grid[2][2]
        antidiagonal = grid[2][0] + grid[1][1] + grid[0][2]
        x1, x2 = 0, 0
        if diagonal == 'MAS' or diagonal == 'SAM':
            x1 = True
        if antidiagonal == 'MAS' or antidiagonal == 'SAM':
            x2 = True
        if x1 and x2:
            match += 1
    
    print(match)