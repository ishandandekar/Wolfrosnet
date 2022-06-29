def shell_sort(arr):
    size = len(arr)
    gap = size//2

    while gap > 0:
        for i in range(gap, size):
            anchor = arr[i]
            j = i
            while j >= gap and arr[j-gap] > anchor:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = anchor
        gap = gap//2


def main():
    import random
    with open(r"numbers/8.txt") as f:
        data = [int(x) for x in f.readlines()]
    random.shuffle(data)
    sorted_list = shell_sort(data.copy())
    print(f"Data before sorting : {data}")
    print(f"Data after sorting : {sorted_list}")


if __name__ == '__main__':
    main()
