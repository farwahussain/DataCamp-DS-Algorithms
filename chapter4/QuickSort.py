#Implement a quick sort algorithm

def partition(my_list, first_index, last_index):
  pivot = my_list[first_index]
  left_pointer = first_index + 1
  right_pointer = last_index
 
  while True:
    # Iterate until the value pointed by left_pointer is greater than pivot or left_pointer is greater than last_index
    while pivot < left_pointer and last_index < left_pointer:
      left_pointer += 1
    
    while my_list[right_pointer] > pivot and right_pointer >= first_index:
      right_pointer -= 1 
    if left_pointer >= right_pointer:
        break
    # Swap the values for the elements located at the left_pointer and right_pointer
    my_list[left_pointer], my_list[right_pointer] = my_list[right_pointer], my_list[left_pointer]
   
  my_list[first_index], my_list[right_pointer] = my_list[right_pointer], my_list[first_index]
  return right_pointer

