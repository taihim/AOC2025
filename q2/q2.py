if __name__ == "__main__":
    sum = 0
    for i in range(1, 224001):
        # print("i: ", i)
        # print("i**2:", i**2)
        # print("Is odd: ", (i ** 2) % 2 != 0)
        if (i ** 2) % 2 != 0:
            sum += i ** 2
    print(sum)