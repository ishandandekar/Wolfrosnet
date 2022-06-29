def bubble_sort(elements):
    size = len(elements)

    for k in range(size-1):
        for i in range(size-1):
            if elements[i] > elements[i+1]:
                elements[i], elements[i+1] = elements[i+1], elements[i]
    return elements


def main():
    import random
    with open(r"numbers/8.txt") as f:
        data = [int(x) for x in f.readlines()]
    random.shuffle(data)
    sorted_list = bubble_sort(data.copy())
    print(f"Data before sorting : {data}")
    print(f"Data after sorting : {sorted_list}")


if __name__ == '__main__':
    main()
