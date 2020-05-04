def countingsort(input, key=lambda x: x):  # O(n+k) -> k = non-negative value range
    """A 2-pass sort algorithm that is efficient when the number of distinct
    keys is small compared to the number of items.

    Stable sorting.

    Args:
        input ([List[int]]): List of positive integers.
        key (Callable[[int], int]): Key function that takes an element of input
            and outputs a key.
    
    Returns:
        List[int]: Sorted list.
    """
    # Value range
    k = max(input) + 1

    # Count occurrence of each value
    count = [0 for _ in range(k)]
    for x in input:  # O(k)
        count[key(x)] += 1

    # Determine position of value
    # position = current_position + number of occurrences
    total = 0
    for i in range(k):  # O(k)
        count[i], total = total, count[i] + total

    # Build output
    output = [0 for _ in range(len(input))]
    for x in input:  # O(n)
        output[count[key(x)]] = x
        count[key(x)] += 1  # Shift next position of same value by 1 to the right

    return output


if __name__ == "__main__":
    print("Countingsort:", countingsort([1, 2, 3, 4, 0, 0, 1, 2, 3, 4, 10, 8, 7]))
