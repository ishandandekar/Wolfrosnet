import random


def is_sorted(values):
    for idx in range(len(values)-1):
        if values[idx] > values[idx+1]:
            return False
    return True


def bogo_sort(values):
    iters = 0
    while not is_sorted(values):
        iters += 1
        random.shuffle(values)
    return values, iters


def main():
    with open(r"numbers/5.txt") as f:
        data = [int(x) for x in f.readlines()]
    random.shuffle(data)
    sorted_data, iters = bogo_sort(data)
    print(f"Data before sorting : {data}")
    print(f"Data after sorting : {sorted_data}")
    print(f"iterations of shuffling : {iters}")


if __name__ == '__main__':
    main()
