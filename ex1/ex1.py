import sys
from typing import List

def howMany0Stops(rotations: List[str]) -> int:
    count = 0
    pos = 50
    for rotation in rotations:
        side = rotation[0]
        number = rotation[1:]
        amount = int(number)

        # Update position
        if side == 'L':
            pos = (pos - amount) % 100
        elif side == 'R':
            pos = (pos + amount) % 100

        # Check if we are at position 0
        if pos == 0:
            count += 1
    return count

def howMany0Cross(rotations: List[str]) -> int:
    count = 0
    pos = 50
    for rotation in rotations:
        side = rotation[0]
        number = rotation[1:]
        amount = int(number)

        # Determine how many times we cross 0 in this rotation
        if side == 'R':
            amountFor0 = (100 - pos) % 100
        else:
            amountFor0 = pos % 100

        # If we are already at 0, we need to adjust from 0 to 100 rotations
        if amountFor0 == 0:
            amountFor0 = 100
        
        if amount >= amountFor0:
            count += 1 + (amount - amountFor0) // 100

        # Update position
        if side == 'L':
            pos = (pos - amount) % 100
        else:
            pos = (pos + amount) % 100

    return count

def main():
    with open("input.txt") as f:
        rotations = [line.strip() for line in f if line.strip()]
    
    # Result = 989
    result = howMany0Stops(rotations)
    print("Part A: " + str(result))

    # Result = 5941
    result = howMany0Cross(rotations)
    print("Part B: " + str(result))

if __name__ == "__main__":
    main()