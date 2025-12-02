from typing import List, Tuple

def sumDuplicate(intervals: List[Tuple[int, int]]) -> int:
    result = 0
    for start, end in intervals:
        for position in range(start, end + 1):
            s = str(position)
            if len(s) % 2 == 0:
                half = len(s) // 2
                if s[:half] == s[half:]:
                    result += position
    return result


def sumRepeated(intervals: List[Tuple[int, int]]) -> int:
    result = 0
    for start, end in intervals:
        for position in range(start, end + 1):
            s = str(position)
            L = len(s)

            # Prueba todos los posibles tamaños de subcadena
            for i in range(1, L):
                if L % i == 0:                     # tiene que dividirse de forma exacta
                    repeats = L // i
                    if repeats >= 2:               # al menos 2 repeticiones
                        if s == s[:i] * repeats:   # repetir la misma subcadena "repeats" veces da el número original
                            result += position
                            break
    return result


def main():
    with open("input.txt") as f:
        line = f.read().strip()

    # Parse "a-b,c-d,e-f"
    intervals = []
    for part in line.split(","):
        a, b = part.split("-")
        intervals.append((int(a), int(b)))

    result = sumDuplicate(intervals)
    print("Part A:", result)

    result = sumRepeated(intervals)
    print("Part B:", result)


if __name__ == "__main__":
    main()
