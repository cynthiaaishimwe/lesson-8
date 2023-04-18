# Given two lists, write a function to find the common elements between them 
# and return them in a new list.

def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = find_common_elements(list1, list2)
print(common_elements)

# Given a list of integers, write a function that returns the smallest element in the list.
def elements(nums):
  nums.sort()
  newnumber = nums[0]
  return newnumber

print(elements(nums= [20,30,80,12,9,3,89]))

# Given a list of integers, write a function that returns the second largest element in the list.

def integers(num):
   num.sort()
   newlist = num[-2]
   return newlist
print(integers(num=[50,20,97,23,45]))

# Given a list of integers, write a function that returns the  largest element in the list.
def list(ages):
   ages.sort()
   newage = ages[-1]
   return newage
print(list(ages=[100,90,56,34,22]))