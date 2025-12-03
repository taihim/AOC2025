import math


def rotate(current_val, direction, amount):
    if direction == "R":
        zero_hit = (current_val + amount) // 100 - ((current_val + 1 - 1) // 100)
        return (current_val + amount) % 100, zero_hit
    else:
        # using formula for multiples in a range
        # for a range [a, b] we can check how many multiples of N exist in the range (a and b inclusive) with the formula:
        # floor(b / N) - floor(a - 1 / N)
        # we do a - 1 so that a is included if its a multiple
        # in python, a // b is the same as floor division
        # for left rotations, we go from 0 -> 99, 98, 97, 96, 95 etc.
        # e.g. if we have L5 and start at 0, we go to 95
        # [99, 98, 97, 96, 95] -> [-1, -2, -3, -4, -5]
        # more generally, when we start at x and rotate by amount A:
            # we visit [x-1, x-2, x-3, x-4,... x-A]
            # when do we "hit" 0? whenever the position visited is divisible by 100 i.e. when x % 100 is 0 (i.e. 0, -100, -200, -300...)
            # so we just need to count how many multiples of 100 are in the range [x-A, x-1]
            # we choose [x-A, x-1] instead of [x-1, x-A] just because of convention
            # i.e. going from smaller to larger values
            # this also means the result is positive so its a win win
            # if we used the range [x-1, x-A] instead, we would have to use abs() to turn the answer positive
            
        zero_hit = (current_val - 1) // 100 - (current_val - amount - 1) // 100
        return (current_val - amount) % 100, zero_hit


def main():
    with open("./q1/input.txt", "r") as input_file:
        lines = "".join(input_file.readlines()).split("\n")

        start = 50
        count = 0

        # print(rotate(start, "R", 3))

        for line in lines:
            print("Start value: ", start)
            print("Rotating:", line)
            
            start, add_count = rotate(start, line[0], int(line[1:]))
            print("New value: ", start)

            print("Add Count: ", add_count)
            count += add_count    

            # if start == 0:
            #     print("Dial ended at 0, increasing count")
            #     count += 1


            print("Count: ", count)
            print("______________________________")

    print("First advent of code puzzle", count)


if __name__ == "__main__":
    main()