def radixsort_lsb(input):  # O(n*k) -> k = maximum number of bits
    """A multiple pass distribution sort algorithm that distributes each item
    to a bucket according to part of the item's key beginning with the least
    significant part of the key.

    Use:
        - When longest integer smaller than n, otherwise n^2 (n * k -> k=n)

    Stable sorting.

    Args:
        input ([List[int]]): List of positive integers.
    
    Returns:
        List[int]: Sorted list.
    """
    k = len(str(max(input)))  # maximum bit size

    # Initialize buckets for all digits 0...9
    buckets = [[] for _ in range(10)]

    # Place input into first bucket
    buckets[0].extend(input)

    for bit in range(k):  # O(k)
        for bucket in buckets:
            for _ in range(len(bucket)):  # O(n)
                # Remove x from bucket to prevent duplicates
                x = bucket.pop(0)
                # Compute bucket ID of current bit
                bucket_id = x % (10 ** (bit + 1)) // (10 ** bit)
                buckets[bucket_id].append(x)

    return [x for b in buckets for x in b]


if __name__ == "__main__":
    print("Radixsort(LSB):", radixsort_lsb([170, 45, 75, 90, 2, 802, 2, 66]))
