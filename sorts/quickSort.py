from random import randrange

def quicksort(lst, start, end):
  if start >= end:
    return
  pivot_idx = randrange(start, end + 1)
  pivot_element = lst[pivot_idx]
  lst[end], lst[pivot_idx] = lst[pivot_idx], lst[end]

  less_than_pointer = start
  
  for i in range(start, end):
    if lst[i] < pivot_element:
      lst[i], lst[less_than_pointer] = lst[less_than_pointer], lst[i]
      less_than_pointer += 1
  lst[end], lst[less_than_pointer] = lst[less_than_pointer], lst[end]
  quicksort(lst, start, less_than_pointer - 1)
  quicksort(lst, less_than_pointer + 1, end)


    
  
lst = [5,3,1,7,4,6,2,8]
quicksort(lst, 0, len(lst) -1)
print(lst)
