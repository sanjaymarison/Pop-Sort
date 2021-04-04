#my algorithm to sort a list in python
#faster than bubble and insertion (only tested with these two)
def pop_sort(list1):
  list2 =[]
      while list1 != []:
          list2.append(list1.pop(list1.index(min(list1))))
   return list2
      
#mean time taken to sort for this algorithm code for hundred thousand iterations
import time
from statistics import mean
time_list = []
for i in range(100000):
    start = time.time()
    list1,list2 = [7,5,3,5,8,2,4,3],[]
    while list1 != []:
        list2.append(list1.pop(list1.index(min(list1))))
    end = time.time()
    time_list.append((end-start))
print(mean(time_list))
