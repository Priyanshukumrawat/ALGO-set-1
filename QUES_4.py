def reverse_array(arr):
  
    return arr[::-1]


arr = []
for i in range(7):
    num = int(input(f"Enter number {i+1}: "))
    arr.append(num)


reversed_arr = reverse_array(arr)


print("Reversed order of numbers:", reversed_arr)
