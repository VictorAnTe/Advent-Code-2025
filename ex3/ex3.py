from typing import List

def sumOfMaximus2(batteries: List[int]) -> int:
    total = 0

    for bank in batteries:
        digits = list(map(int, bank))
        best = 0

        # Compute the best 2-digit value
        for i in range(len(digits)):
            first = digits[i]
            second = max(digits[i+1:], default=-1)
            if second >= 0:
                value = first * 10 + second
                best = max(best, value)

        total += best

    return total


def sumOfMaximus12(batteries: List[int]) -> int:
    total = 0

    K = 12

    for bank in batteries:
        digits = list(map(int, bank))
        to_remove = len(digits) - K
        stack = []

        for d in digits:
            while stack and to_remove > 0 and stack[-1] < d:
                stack.pop()
                to_remove -= 1
            stack.append(d)

        # Take first K digits
        chosen = stack[:K]

        # Convert list of digits to integer
        value = int("".join(map(str, chosen)))
        total += value

    return total



def main():
    with open("input.txt") as f:
        batteries = [line.strip() for line in f if line.strip()]
    
    # Result = 17346
    result = sumOfMaximus2(batteries)
    print("Part A: " + str(result))

    # Result = 5941
    result = sumOfMaximus12(batteries)
    print("Part B: " + str(result))


if __name__ == "__main__":
    main()