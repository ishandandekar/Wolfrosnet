def quick_sort(values):
    if len(values) <= 1:
        return values
    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]
    for value in values[1:]:
        if value > pivot:
            greater_than_pivot.append(value)
        else:
            less_than_pivot.append(value)
    return quick_sort(less_than_pivot)+[pivot]+quick_sort(greater_than_pivot)


def main():
    import random
    with open(r"numbers/8.txt") as f:
        data = [int(x) for x in f.readlines()]
    random.shuffle(data)
    sorted_list = quick_sort(data.copy())
    print(f"Data before sorting : {data}")
    print(f"Data after sorting : {sorted_list}")


if __name__ == '__main__':
    main()
