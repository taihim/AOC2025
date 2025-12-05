# 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22

# invalid sequence -> some sequence of digits repeated twice. which can only happen for a number of even length so if len = 4, we compare 0,1 and 1,2
# 1111

if __name__ == "__main__":
    with open("./q2/input.txt", "r") as f:
        x = [line.split("-") for line in f.read().split(",")]
        total = 0
        for pair in x:            
            total_ids = int(pair[1]) - int(pair[0]) + 1
            for num in range(int(pair[0]), int(pair[1]) + 1):
                digits = len(str(num))
                if digits % 2 == 0:
                    mid = digits // 2
                    if str(num)[0:mid] == str(num)[mid:]:
                        print("Invalid ID:", num)
                        total += num

        print("Total: ", total)

