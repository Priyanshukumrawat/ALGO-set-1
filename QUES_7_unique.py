def print_unique_numbers(arr):

    counts = {}
   

    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
   

    print("Unique numbers in the array are:")
    for num, count in counts.items():
        if count == 1:
            print(num)

arr = [4, 5, 6, 7, 4, 8, 9, 6]
print_unique_numbers(arr)