# Hardcoded list of 20 student IDs
student_ids = [
    101, 103, 108, 115, 120,
    125, 130, 135, 140, 145,
    150, 155, 160, 165, 170,
    175, 180, 185, 190, 195
]

def linear_search(ids, target):
    for i in range(len(ids)):
        if ids[i] == target:
            return i + 1  # Return position (1-indexed)
    return -1


def main():
    print("=== Linear Search: Find a Student ID ===")
    print("Student IDs:", student_ids)

    target = int(input("Enter the Student ID to search for: "))

    result = linear_search(student_ids, target)

    if result != -1:
        print(f"Student ID found at position {result}.")
    else:
        print("Student ID not found.")


if __name__ == "__main__":
    main()

# Hardcoded sorted list of 20 test scores
scores = [
    45, 50, 52, 55, 58,
    60, 62, 65, 68, 70,
    72, 75, 78, 80, 82,
    85, 88, 90, 92, 95
]

def binary_search(lst, target):
    left, right = 0, len(lst) - 1

    while left <= right:
        mid = (left + right) // 2

        if lst[mid] == target:
            return mid + 1  # Return 1-indexed position
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def main():
    print("=== Binary Search: Find a Score ===")
    print("Scores:", scores)

    target = int(input("Enter the score to search for: "))

    result = binary_search(scores, target)

    if result != -1:
        print(f"Score found at position {result}.")
    else:
        print("Score not found.")


if __name__ == "__main__":
    main()
