# 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22

# invalid sequence -> some sequence of digits repeated twice. which can only happen for a number of even length so if len = 4, we compare 0,1 and 1,2
# 1111

# if __name__ == "__main__":
#     with open("./q2/input.txt", "r") as f:
#         x = [line.split("-") for line in f.read().split(",")]
#         total = 0
#         for pair in x:            
#             total_ids = int(pair[1]) - int(pair[0]) + 1
#             for num in range(int(pair[0]), int(pair[1]) + 1):
#                 digits = len(str(num))
#                 if digits % 2 == 0:
#                     mid = digits // 2
#                     if str(num)[0:mid] == str(num)[mid:]:
#                         # print("Invalid ID:", num)
#                         total += num

#         print("Total: ", total)



# math based approach
# any twice repeated sequence of digits can be expressed as a multiplication. e.g. 11 -> 1 * 11, 123123 -> 123 * 1001, 45674567 -> 4567 * 10001
# more generally, the repeated sequence is n * (10 ^ k + 1), where n is a k digit number. we just need to find which values of n produce numbers in our range [a, b]
# so we need to also find the minimum and max values for n based on the range
# before that, lets see how we can get the min and max val of n for a specific k
# e.g. if we assume n is a 1 digit number then k -> 1, and the sequence will be of length 2*k -> 2
# 1 digit -> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# sequences -> 00, 11, 22, 33, 44, 55, 66, 77, 88, 99
# problem told us to ignore zero so 0 and 00 dont count.
# so we have 1, 2, 3, 4, 5, 6, 7, 8, 9
# the minimum number is 1 i.e. 10 ^ 0
# max val of n is 9 i.e. 10 ^ 1 - 1
# since k -> 1, we can write n_min -> 10 ^ (k-1) and n_max -> 10 ^ k - 1
# lets validate for k = 2
# 10, 11, 12, 13, ... 97, 98, 99
# n_min -> 10 ^ (2 - 1) -> 10
# n_max -> 10 ^ 2 -1 -> 99

# so we know we can get the min with 10 ^ (k-1) and max with 10 ^ k - 1
# but now we also have a range provided by the problem.
# we need to choose which min and max values should be used

# e.g. if we get the range [11, 22] 
# so we are checking sequences of 2 digit numbers i.e. k = 1
# therefore n_min will be the higher one out of 10 ^ (k-1) or the value ceil(11 // 10 ^ k + 1)
# in this case they are equal so we can use whatever
# but if they are not equal, we use the larger value since we need numbers that fall in the range only
# n_max will be the lower value between floor(22 // 10 ^ k + 1) and 10 ^ k - 1 for the same reason

# what happens for odd num digits? 
# k = 3 / 2 - > 1.5
# n_min -> 10 ^ (1.5 - 1) -> 3.6
# n_max -> 10 ^ 1.5 -1 -> 31.6
# the math breaks down. odd digit numbers cannot have a twice repeating pattern in them

# therefore:
# the minimum value of n will be whichever is higher between ceil(a/10^k + 1) and 10 ^ (k-1)  
# the max value of n will be whichever is lower between floor(b/10^k + 1) and (10 ^ k) - 1

# after we have n_min and n_max, multiplying n by them will give us the min and max repeating number in the range
# e.g. n_min = 1 and n_max = 9 (k = 1)
# 10 ^ 1 + 1 = 11
# so our repeated numbers will be:# 1 * 11, 2 * 11, 3 * 11, 4 * 11, 9 * 11
# i.e. 11, 22, 33, 44, 55, 66, 77, 88, 99
# we want to sum them which is (11 + 22 + 33 + 44 + 55...)
# if we just factor out the multiplier 11 * (1 + 2 + 3 + 4 + 5...)
# so we can write the sum of all repeated sequences as (10 ^ k + 1) * (sum(n))
import math
if __name__ == "__main__":
    with open("./q2/input.txt", "r") as f:
        x = [line.split("-") for line in f.read().split(",")]
        total = 0
        for pair in x:   
            a = int(pair[0])
            b = int(pair[1])         
            
            digits = len(pair[1]) # 2*k. k = digits / 2, use the second value to get max number of digits
            
            k = digits // 2
            
            multiplier = (10 ** k) + 1

            n_min = max(math.ceil(a / ((10**k)+1)), 10**(k-1))
            n_max = min(math.floor(b / ((10**k)+1)), (10**k) - 1)

            # print(k)
            # print(a, b)
            # print(n_min, n_max)
            # print("_____________")

            if n_min <= n_max: # if n_min is greater, that means there is no number in this range that is a repeating sequence
                counts = n_max - n_min + 1 # how many values of n do we have
                bases_sum = counts * ((n_min + n_max) / 2) # arithmetic series to get sum of all n's in the range
                sum_invalid = multiplier * bases_sum
                total += sum_invalid
            # break
        print("Total: ", int(total))
