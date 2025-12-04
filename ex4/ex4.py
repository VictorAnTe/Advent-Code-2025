from typing import List

def countAccessibleRolls(grid: List[str]) -> int:
    total = 0

    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '@':
                continue

            adjacent = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue

                    rr = r + dr
                    cc = c + dc

                    if 0 <= rr < rows and 0 <= cc < cols:
                        if grid[rr][cc] == '@':
                            adjacent += 1

            if adjacent < 4:
                total += 1

    return total



def countTotalRemovable(grid: List[str]) -> int:
    # Convert to mutable list of lists
    g = [list(row) for row in grid]

    rows = len(g)
    cols = len(g[0])

    total_removed = 0

    while True:
        to_remove = []

        # Identify all removable rolls
        for r in range(rows):
            for c in range(cols):
                if g[r][c] != '@':
                    continue

                adjacent = 0
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue

                        rr = r + dr
                        cc = c + dc

                        if 0 <= rr < rows and 0 <= cc < cols:
                            if g[rr][cc] == '@':
                                adjacent += 1

                if adjacent < 4:
                    to_remove.append((r, c))

        # No more accessible rolls
        if not to_remove:
            break

        # Remove all marked rolls at once
        for r, c in to_remove:
            g[r][c] = '.'

        total_removed += len(to_remove)

    return total_removed



def main():
    with open("input.txt") as f:
        grid = [line.strip() for line in f if line.strip()]

    # result = 1553
    partA = countAccessibleRolls(grid)
    print("Part A: " + str(partA))

    # result = 8442
    partB = countTotalRemovable(grid)
    print("Part B: " + str(partB))



if __name__ == "__main__":
    main()
