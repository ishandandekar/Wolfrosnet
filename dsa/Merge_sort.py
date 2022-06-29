def merge_sort(elements):
    if len(elements) <= 1:
        return elements
    mid = len(elements)//2
    left = elements[:mid]
    right = elements[mid:]
    merge_sort(left)
    merge_sort(right)
    return merge_two_sorted_lists(left, right, elements)


def merge_two_sorted_lists(a, b, arr):
    len_a, len_b = len(a), len(b)
    i = j = k = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
    k += 1
    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1
    return arr


def main():
    import random
    with open(r"numbers/8.txt") as f:
        data = [int(x) for x in f.readlines()]
    random.shuffle(data)
    sorted_list = merge_sort(data.copy())
    print(f"Data before sorting : {data}")
    print(f"Data after sorting : {sorted_list}")


if __name__ == '__main__':
    main()
