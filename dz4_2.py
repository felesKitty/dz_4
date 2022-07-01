num_list = [222, 22, 11, 7, 20, 33, 35, 34, 50, 230, 17, 6, 8, 1]
more_previous = [num_list[num] for num in range(1, len(num_list))
             if num_list[num] > num_list[num - 1]]
print(more_previous)
