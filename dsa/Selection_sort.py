def index_of_min(values):
    min_index = 0
    for i in range(1, len(values)):
        if values[i] < values[min_index]:
            min_index = i
    return min_index


def selection_sort(values):
    ls = []
    for i in range(0, len(values)):
        index_to_move = index_of_min(values)
        ls.append(values.pop(index_to_move))
    return ls


def main():
    import random
    with open(r"numbers/5.txt") as f:
        data = [int(x) for x in f.readlines()]
    random.shuffle(data)
    sorted_list = selection_sort(data.copy())
    print(f"Data before sorting : {data}")
    print(f"Data after sorting : {sorted_list}")


if __name__ == '__main__':
    main()
