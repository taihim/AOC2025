def rotate(current_val, direction, amount):
    if direction == "R":
        return (current_val + amount) % 100
    else:
        return (current_val - amount) % 100

def main():
    with open("./q1/input.txt", "r") as input_file:
        lines = "".join(input_file.readlines()).split("\n")

        start = 50
        count = 0
        for line in lines:
            print("Start value: ", start)
            print("Rotating:", line)
            
            start = rotate(start, line[0], int(line[1:]))    
            print("New value: ", start)
           

            if start == 0:
                count += 1

            print("Count: ", count)
            print("______________________________")

    print("First advent of code puzzle", count)


if __name__ == "__main__":
    main()