# Hardcoded list of 15 student names
student_names = [
    "Karma", "Sonam", "Dechen", "Pema", "Jigme",
    "Tashi", "Ugyen", "Sangay", "Passang", "Chimi",
    "Dorji", "Tshering", "Kinley", "Thinley", "Namgay"
]

def bubble_sort(names):
    arr = names.copy()
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j].lower() > arr[j + 1].lower():   # Compare alphabetically
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def main():
    print("=== Bubble Sort: Student Names ===")
    print("Original List:")
    print(student_names)

    sorted_names = bubble_sort(student_names)

    print("\nSorted List (Alphabetically):")
    print(sorted_names)


if __name__ == "__main__":
    main()

# Hardcoded unsorted list of 20 test scores
scores = [72, 55, 88, 91, 60, 45, 78, 85, 69, 95,
          53, 82, 90, 74, 67, 58, 80, 99, 62, 50]

def selection_sort(lst):
    arr = lst.copy()
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


def main():
    print("=== Sorting Test Scores ===")

    print("\nOriginal Unsorted List:")
    print(scores)

    sorted_scores = selection_sort(scores)

    print("\nSorted List (Ascending Order):")
    print(sorted_scores)

    top_5 = sorted_scores[-5:]      # Last 5 elements = highest
    top_5.reverse()                 # Display in descending order (highest first)

    print("\nTop 5 Scores:")
    print(top_5)


if __name__ == "__main__":
    main()

# Hardcoded unsorted list of 15 book prices
book_prices = [499, 150, 320, 899, 120, 250, 450, 799, 600, 330,
               275, 520, 410, 680, 150]

# Global counter for recursive calls
recursive_calls = 0

def quick_sort(lst):
    global recursive_calls
    recursive_calls += 1

    if len(lst) <= 1:
        return lst

    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


def main():
    global recursive_calls
    print("=== Quick Sort: Book Prices ===")

    print("\nOriginal Unsorted List:")
    print(book_prices)

    recursive_calls = 0  # Reset counter before sorting
    sorted_prices = quick_sort(book_prices)

    print("\nSorted List (Ascending Order):")
    print(sorted_prices)

    print(f"\nNumber of Recursive Calls: {recursive_calls}")


if __name__ == "__main__":
    main()
