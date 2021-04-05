
try:
  import time
  from statistics import mean
except ImportError as e:
  print("Testing Might not be available due to Import Error")
  print(e)
#my algorithm to sort a list in python
#faster than bubble and insertion (only tested with these two)
def pop_sort(list1):
  list2 =[]
  while list1 != []:
    list2.append(list1.pop(list1.index(min(list1))))
  return list2
      
def test(list_=[7,5,3,5,8,2,4,3],cycles=100000): #mean time taken to sort for this algorithm code for hundred thousand iteration
  time_list = []
  given_list = list_.copy()
  for i in range(cycles):
      start = time.time()
      list1,list2 = list_,[]
      while list1 != []:
        list2.append(list1.pop(list1.index(min(list1))))
      end = time.time()
      time_list.append((end-start))
  print()
  print("Mean time taken to cycle through",cycles,"iterations for",given_list," is ",mean(time_list))
  print("Total time taken to cycle through:",sum(time_list))
  print()
test()
