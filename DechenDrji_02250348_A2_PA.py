# List of student IDs (already sorted)
student_ids = [
    101, 103, 108, 115, 120,
    125, 130, 135, 140, 145,
    150, 155, 160, 165, 170,
    175, 180, 185, 190, 195
]

# List of scores (already sorted for binary search)
scores = [
    45, 50, 52, 55, 58,
    60, 62, 65, 68, 70,
    72, 75, 78, 80, 82,
    85, 88, 90, 92, 95
]

# LINEAR SEARCH

def linear_search(values, target):
    """
    Search for 'target' in the list using Linear Search.
    Returns the 1-indexed position if found, otherwise -1.
    """
    for index in range(len(values)):
        if values[index] == target:
            return index + 1  # Convert to human-friendly position
    return -1  # Not found


# BINARY SEARCH

def binary_search(values, target):
    """
    Search for 'target' in the list using Binary Search.
    Returns the 1-indexed position if found, otherwise -1.
    """
    left = 0
    right = len(values) - 1

    while left <= right:
        middle = (left + right) // 2

        if values[middle] == target:
            return middle + 1  # Convert to human-friendly position
        elif values[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1  # Not found


def main():
    print("    SEARCH PROGRAM    ")
    print("1. Linear Search (Student IDs)")
    print("2. Binary Search (Scores)")

    choice = int(input("Choose an option (1 or 2): "))

    # --- Linear Search ---
    if choice == 1:
        print("\nStudent ID List:")
        print(student_ids)

        target = int(input("\nEnter the Student ID to find: "))
        result = linear_search(student_ids, target)

        if result != -1:
            print(f"\n✔ Student ID found at position {result}.")
        else:
            print("\n✘ Student ID not found in the list.")

    # --- Binary Search ---
    elif choice == 2:
        print("\nScore List:")
        print(scores)

        target = int(input("\nEnter the score to find: "))
        result = binary_search(scores, target)

        if result != -1:
            print(f"\n✔ Score found at position {result}.")
        else:
            print("\n✘ Score not found in the list.")

    else:
        print("\nInvalid choice! Please restart the program.")


# Run the program
if __name__ == "__main__":
    main()
