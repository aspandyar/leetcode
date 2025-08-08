def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

def generate_list(n):
    return list(range(n))

if __name__ == "__main__":
    n = 1000
    item = 234
    list = generate_list(n)

    print(binary_search(list, item))

for i in len(list):
    print(i)
